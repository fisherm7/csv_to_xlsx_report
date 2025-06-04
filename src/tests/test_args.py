import pytest
from csv_to_xlsx_report import csv_to_xlsx

testdir = 'src/tests/'
infile = f'{testdir}testinfile.csv'
outfile = f'{testdir}testoutfile.xlsx'
sheet_name = 'test sheet'
title_name = 'test title'
numeric_columns = ['device_id', 'device_count']
delimiter = ','
title_format = {'font_size': 16}

def test_no_args():
    with pytest.raises(ValueError):
        csv_to_xlsx()

def test_no_infile():
    with pytest.raises(ValueError, match='infile'):
        csv_to_xlsx(#infile = infile,
                    delimiter = delimiter,
                    outfile = outfile,
                    sheet_name = sheet_name,
                    title_name = title_name,
                    numeric_columns = numeric_columns,
                    title_format = title_format
        )

def test_no_outfile():
    with pytest.raises(ValueError, match='outfile'):
        csv_to_xlsx(infile = infile,
                    delimiter = delimiter,
                    #outfile = outfile,
                    sheet_name = sheet_name,
                    title_name = title_name,
                    numeric_columns = numeric_columns,
                    title_format = title_format
        )

def test_no_sheet_name():
    with pytest.raises(ValueError, match='sheet_name'):
        csv_to_xlsx(infile = infile,
                    delimiter = delimiter,
                    outfile = outfile,
                    #sheet_name = sheet_name,
                    title_name = title_name,
                    numeric_columns = numeric_columns,
                    title_format = title_format
        )

def test_no_title_name():
    with pytest.raises(ValueError, match='title_name'):
        csv_to_xlsx(infile = infile,
                    delimiter = delimiter,
                    outfile = outfile,
                    sheet_name = sheet_name,
                    #title_name = title_name,
                    numeric_columns = numeric_columns,
                    title_format = title_format
        )

