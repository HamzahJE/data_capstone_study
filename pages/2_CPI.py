import streamlit as st
import streamlit.components.v1 as components
from functions import ecpi_chart, fcpi_chart
st. set_page_config(layout="wide",
    page_title='Effect on CPI',
    page_icon='💳'
)
st.sidebar.success('👆 Select a page above 👆')
st.title('Effect on the Consumer Price Index')

st.plotly_chart(ecpi_chart, use_container_width=True)

st.plotly_chart(fcpi_chart, use_container_width=True)

st.sidebar.header('What Effect did *COVID-19* have on CPI?')


with st.sidebar:
    st.markdown('___')
    st.markdown("Developed by `Hamzah`  ⇨  [GitHub Repo](https://github.com/HamzahJE/data_capstone_study).")
    st.markdown('___')

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)