import streamlit as st
from langchain_helper import get_few_shot_db_chain, db_name
import altair as alt

st.set_page_config(
    page_title = "Text2SQL",
    layout = "wide",
    initial_sidebar_state="expanded")


with st.sidebar:
    st.title('Text2SQL')
    st.write("Created by: ")
    linkedIn_url = "https://www.linkedin.com/in/karan-thakur-profile/"

    st.markdown(f'''<a href="{linkedIn_url}" target="_blank" style="text-decoration: none; color: inherit;">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; 
                margin-right: 10px;">Karan Thakur</a>''', unsafe_allow_html = True)

alt.themes.enable("dark")

st.title("Text2SQL")
question = st.text_input(f'Please input your prompt for the database: {db_name}')

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)