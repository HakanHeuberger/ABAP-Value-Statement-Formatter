# ABAP-Value-Statement-Formatter

The standard "Copy as ABAP Value Statement..." function of Eclipses' ADT often is not enough to get a readable value statement.
While the standard format may be adequate enough for small data tables, larger ones definitely get unreadable, at least for me.

This script is a work around I created to automate my testing experience while mocking tables in ABAP. It is nowhere perfect, optimized or extensively tested. 
Feel free to copy, use and extend any part of the script. Have fun!

The script expects an Input.txt file filled with an unstructured abap value statement from ADT and formats it, putting the output into a Output.txt file.
It uses a combination of a RegEx statement and tokenization to reformat the input and give each table field an own line.
It can also handle multiple nested structured.

Limitation: All field values have to be in string format, i.e. inside ''. 



