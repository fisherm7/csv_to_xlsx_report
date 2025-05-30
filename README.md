Modularized conversion of a csv file into a presentable executive spreadsheet.  
With parameterized keyword arguments, designed as part of an automated process
to send weekly reports executed via cron.
  
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
