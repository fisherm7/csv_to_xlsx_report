Modularized conversion of a csv file into a presentable executive spreadsheet.  
With formatting keyword arguments, this program can fit into an automation  
suite to send user-friendly reports with varying numbers of rows and columns.  
The result is an Excel spreadsheet with a large title on line zero, the table  
(a structured and formatted data range) beginning on line 3, and a spreadsheet  
tab with a custom name.  
  
Usage:  
```
csv_to_xlsx(infile=<infile>,
            outfile=<outfile>,
            [delimiter=<delimiter>],
            [sheet_name=<sheet name>],
            [title_name=<title>],
            [numeric_columns=<numeric columns>],
            [title_format=<title format>]
)

All arguments are keyword arguments:
    infile: required string; the csv input filename
    outfile: required string; the xlsx output filename
    delimiter: optional one-character string; the record delimiter
        Default: '|'
    sheet_name: required string; the spreadsheet's tab's name
        Example: 'weekly-sales'
    title_name: required string; the formal name on row 0 of the report,
        Example: 'Weekly Sales Report for May 29'
    numeric_columns: optional list of strings; column names to be imported
    as numeric data. Excel defaults to importing everything as text.
        Example: ['user_id','customer_id']
    title_format: an optional xlsxwriter cell format object dictionary
        Default: {'bold': True, 'font_size': 14}
```
