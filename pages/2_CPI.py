import streamlit as st
import streamlit.components.v1 as components
from plotly_charts import ecpi_chart, fcpi_chart
st. set_page_config(layout="wide",
    page_title='Effect on CPI',
    page_icon='💳'
)
st.sidebar.success('⬆️ Select a page above ⬆️')
st.title('Effect on the Consumer Price Index')

st.plotly_chart(ecpi_chart, use_container_width=True)

st.plotly_chart(fcpi_chart, use_container_width=True)

st.sidebar.header('What Effect did *COVID-19* and the *Ukraine Conflict* have on CPI?')


with st.sidebar:
    st.markdown('___')
    st.markdown("Developed by `Hamzah`  ⇨  [GitHub](https://github.com/HamzahJE), [Linkedin](https://www.linkedin.com/in/HamzahJE/).")
    st.markdown('___')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)