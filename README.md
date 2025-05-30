Modularized conversion of a csv file into a presentable executive spreadsheet.  
With parameterized formatting arguments, this program can fit into an  
automation suite to send user-friendly reports with varying numbers of rows  
and columns. The result is an Excel spreadsheet with a large title on line  
zero, the table (a structured and formatted data range) beginning on line 3,  
and a spreadsheet tab with a custom name.  
  
Usage:  
```
csv_to_xlsx(infile=<infile>,
            outfile=<outfile>,
            [delimiter=<delimiter>],
            [sheet_name=<sheetname>],
            [title_name=<title>],
            [title_format=<titleformat>]
)

    infile: a string; the csv input filename
    outfile: a string; the xlsx output filename
    delimiter: optional one-character string; the record delimiter
        Default: '|'
    sheet_name: optional string; the spreadsheet's tab's name
        Example: 'weekly-sales'
    title_name: optional string; the formal name on row 0 of the report,
        Example: 'Weekly Sales Report for May 29'
    title_format: an optional xlsxwriter cell format object dictionary
        Default: {'bold': True, 'font_size': 14}
```
