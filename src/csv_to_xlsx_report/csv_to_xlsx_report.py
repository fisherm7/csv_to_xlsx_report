# Standard libraries
import csv
from string import ascii_uppercase
from typing import TextIO

# Third party
import pandas
from pandas import DataFrame
import xlsxwriter
from xlsxwriter import Workbook, workbook

def get_data(infile: TextIO, delimiter: str) -> csv.reader:
    csv_reader = csv.reader(infile, delimiter=delimiter)
    return csv_reader

def clean_data(csv_reader: csv.reader) -> list[int | str]:
    clean_csv_report = []
    for csv_row in csv_reader:
        clean_row = [_col.strip() for _col in csv_row]
        if len(clean_row) > 1:
            clean_csv_report.append(clean_row)
    if not clean_csv_report:
        raise RuntimeError(
            'Report is empty, or there is only 1 column. ' \
            'Did you use the correct delimiter?'
        )
    return clean_csv_report

def import_data(clean_csv_report: list[int | str],
                numeric_columns: list[str]
) -> DataFrame:
    header_row = clean_csv_report[0]
    del(clean_csv_report[0])
    data_frame = DataFrame(clean_csv_report, columns=header_row)
    if numeric_columns is None:
        return data_frame
    for _col in numeric_columns:
        data_frame[_col] = pandas.to_numeric(data_frame[_col],
                                            errors='coerce'
        )
    return data_frame

def write_to_excel(data_frame: DataFrame,
                   xlsx_writer: xlsxwriter,
                   sheet_name: str
) -> tuple[Workbook, workbook.Worksheet]:
    data_frame.to_excel(xlsx_writer,
                        sheet_name=sheet_name,
                        index=False,
                        startrow=2
    )
    workbook = xlsx_writer.book
    worksheet = xlsx_writer.sheets[sheet_name]
    return (workbook, worksheet)

def add_data_as_table(data_frame: DataFrame,
                      worksheet: workbook.Worksheet
) -> None:
    start_table_at_row = 3
    table_start = ''.join(['A', str(start_table_at_row)])
    table_end = ''.join([ascii_uppercase[len(data_frame.columns) - 1],
                        str(data_frame.index[-1] + start_table_at_row + 1)]
    )
    table_span = ''.join([table_start, ':', table_end])
    table_header = [{'header': _col} for _col in data_frame.columns]
    worksheet.add_table(table_span, {'columns': table_header})

def auto_set_column_widths(data_frame: DataFrame,
                      worksheet: workbook.Worksheet
) -> None:
    for _index, _column in enumerate(data_frame):
        column_length = max(data_frame[_column].astype(str).map(len).max(),
                            len(_column)
        )
        worksheet.set_column(_index, _index, column_length + 1)

def write_title(workbook: Workbook,
                worksheet: workbook.Worksheet,
                title_name: str,
                title_format_dict: dict
) -> None:
    title_format = workbook.add_format(title_format_dict)
    worksheet.write_string(0, 0, title_name, title_format)

def csv_to_xlsx(*,
                infile: str = None,
                outfile: str = None,
                sheet_name: str = None,
                title_name: str = None,
                delimiter: str = '|',
                numeric_columns: list[str] = None,
                title_format: dict = None
) -> None:
    for kw_arg_name, kw_arg_value in {"infile": infile,
                                      "outfile": outfile,
                                      "sheet_name": sheet_name,
                                      "title_name": title_name
    }.items():
        if kw_arg_value is None:
            raise ValueError(f"The {kw_arg_name} keyword argument is required.")
    title_format = title_format or {'bold': True, 'font_size': 14}
    with open(infile) as csv_infile:
        csv_reader = get_data(csv_infile, delimiter)
        clean_csv_report = clean_data(csv_reader)
    data_frame = import_data(clean_csv_report, numeric_columns)
    with pandas.ExcelWriter(outfile, engine='xlsxwriter') as xlsx_writer:
        (workbook, worksheet) = write_to_excel(data_frame,
                                               xlsx_writer,
                                               sheet_name
        )
        add_data_as_table(data_frame, worksheet)
        auto_set_column_widths(data_frame, worksheet)
        write_title(workbook, worksheet, title_name, title_format)

if __name__ == '__main__':
    csv_to_xlsx()
