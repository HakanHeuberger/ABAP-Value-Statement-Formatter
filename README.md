# ABAP-Value-Statement-Formatter

The standard "Copy as ABAP Value Statement..." function of Eclipses' ADT often is not enough to get a readable value statement.

While this format may be adequate enough for small data tables, larger one definitely get unreadable.
lt_q = VALUE #(
  ( mandt = '100' carrid = 'carrid1' carrname = 'carrname1' currcode = 'EUR' )
  ( mandt = '100' carrid = 'carrid2' carrname = 'carrname2' currcode = 'EUR' )
  ( mandt = '100' carrid = 'carrid3' carrname = 'carrname3' currcode = 'EUR' )
  ( mandt = '100' carrid = 'carrid4' carrname = 'carrname4' currcode = 'EUR' )
  ( mandt = '100' carrid = 'carrid5' carrname = 'carrname5' currcode = 'EUR' )
).

The script expects an Input.txt file filled with an unstructured abap value statement from ADT and formats it, putting the output into a Output.txt file:
lt_q = VALUE #(
  ( mandt = '100'
    carrid = 'carrid1'
    carrname = 'carrname1'
    currcode = 'EUR'
  )
  ( mandt = '100'
    carrid = 'carrid2'
    carrname = 'carrname2'
    currcode = 'EUR'
  )
  ( mandt = '100'
    carrid = 'carrid3'
    carrname = 'carrname3'
    currcode = 'EUR'
  )
  ( mandt = '100'
    carrid = 'carrid4'
    carrname = 'carrname4'
    currcode = 'EUR'
  )
  ( mandt = '100'
    carrid = 'carrid5'
    carrname = 'carrname5'
    currcode = 'EUR'
  )
)

The script is a work around I created to automate my testing experience while mocking tables in ABAP. It is nowhere perfect or optimized. 
Feel free to copy, use and extend any part of the script. Have fun!
