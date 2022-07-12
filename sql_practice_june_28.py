import pyodbc
import pandas as pd

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
cnxn = pyodbc.connect('Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=database_june_2022;Trusted_Connection=True;')
# cursor = cnxn.cursor()
# cursor.execute('SELECT * FROM startups_1$')
#
# for i in cursor:
#     print(i)

dataframe = pd.read_sql_query('SELECT * FROM startups_1$', cnxn)
pd.options.display.max_rows = None
pd.options.display.max_columns = None
# print(dataframe)
print(dataframe.dtypes)

