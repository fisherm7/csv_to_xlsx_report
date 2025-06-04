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

def test_wrong_delimiter():
    with pytest.raises(RuntimeError, match='correct delimiter'):
        csv_to_xlsx(infile = infile,
                    delimiter = '|',
                    outfile = outfile,
                    sheet_name = sheet_name,
                    title_name = title_name,
                    numeric_columns = numeric_columns,
                    title_format = title_format
        )

