import streamlit as st
import sqlite3
import pandas as pd
import sqlglot

# Sidebar - Choose source SQL dialect
st.sidebar.title("Settings")
dialect = st.sidebar.selectbox(
    "Input SQL Dialect",
    options=[
       "mysql", "postgres", "tsql", "hive", "spark", 
        "bigquery", "redshift", "databricks", "snowflake", "oracle"
    ],
    index=0
)

# Main UI
st.title("SQL Runner")
st.image("chinook_schema.png", caption="Chinook Database Schema", use_column_width=True)
sql_input = st.text_area("Enter SQL query:", height=100)
run_query = st.button("Run")

# Load Chinook SQLite DB
conn = sqlite3.connect("Chinook_Sqlite.sqlite")

if run_query and sql_input.strip():
    try:
        translated_sql = sqlglot.transpile(sql_input, read=dialect, write="sqlite")[0]
        # st.code(translated_sql, language="sql")
        df = pd.read_sql_query(translated_sql, conn)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {e}")
