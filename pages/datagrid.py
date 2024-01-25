from st_aggrid import AgGrid
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mssql+pyodbc://admin:JYADzncw132MnajClFrF@crawlerdatabase.c61596xtihb7.ap-southeast-1.rds.amazonaws.com/nlpresults?driver=ODBC+Driver+17+for+SQL+Server", fast_executemany=True, connect_args={'charset':'utf8', 'convert_unicode': True})
df = pd.read_sql_table('grammar', engine)
#df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)