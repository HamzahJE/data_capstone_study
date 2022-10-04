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

