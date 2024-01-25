import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mssql+pyodbc://admin:JYADzncw132MnajClFrF@crawlerdatabase.c61596xtihb7.ap-southeast-1.rds.amazonaws.com/nlpresults?driver=ODBC+Driver+17+for+SQL+Server", fast_executemany=True, connect_args={'charset':'utf8', 'convert_unicode': True})
df = pd.read_sql_table('grammar', engine)
#df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

# Number of rows per page
rows_per_page = 5

# Define the grid options
grid_options = GridOptionsBuilder.from_dataframe(df)
grid_options.configure_pagination(paginationPageSize=rows_per_page)
grid_options.configure_side_bar()

st.title('Grammar Database')

# Custom CSS to set width to 100%
st.markdown(
    """
    <style>
    .ag-theme-alpine {
        width: 100%;        
    }
    .st-emotion-cache-1y4p8pa {
        width: 100%;
        padding: 6rem 1rem 10rem;
        max-width: "100% !importnant";        
    }
    </style>
    """,
    unsafe_allow_html=True
)

AgGrid(df,
    gridOptions=grid_options.build(),    
    custom_css={
        "#gridToolBar": {
            "padding-bottom": "0px !important",
        }
    })