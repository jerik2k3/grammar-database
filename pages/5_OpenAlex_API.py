import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import sqlalchemy
import requests

##engine = sqlalchemy.create_engine("mssql+pyodbc://admin:JYADzncw132MnajClFrF@crawlerdatabase.c61596xtihb7.ap-southeast-1.rds.amazonaws.com/nlpresults?driver=ODBC+Driver+17+for+SQL+Server", fast_executemany=True, connect_args={'charset':'utf8', 'convert_unicode': True})
##df = pd.read_sql_table('grammar', engine)
#df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

# Number of rows per page
rows_per_page = 25

# Define the grid options
##grid_options = GridOptionsBuilder.from_dataframe(df)
##grid_options.configure_pagination(paginationPageSize=rows_per_page)
##grid_options.configure_side_bar()

st.title('OpenAlex API')

with st.form("alex_form"):
    title = st.text_input('Search for Articles here', '')
    submitted = st.form_submit_button("Search")
    st.write('Keyword is', title)

    genre = st.radio(
        "Category",
        [":rainbow[Abstract]", "***Full Text***", "Title :movie_camera:", "Display Name"],
        index=0,
    )

    st.write("You selected:", genre)    

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
            max-width: 100% !important;        
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    data = {}

    if submitted:
        st.write("Searching:", title)
        if genre == ':rainbow[Abstract]':
            data = requests.get("https://api.openalex.org/works?filter=abstract.search:" + title).json()

    st.json(data, expanded=False)