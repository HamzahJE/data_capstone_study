import streamlit as st
import streamlit.components.v1 as components
from plotly_charts import rgdp_chart
st. set_page_config(layout="wide",
    page_title='Effect on GDP',
    page_icon='🏦'
)
st.sidebar.success('⬆️ Select a page above ⬆️')


st.title('Effect on the Gross Domestic Product')

st.plotly_chart(rgdp_chart, use_container_width=True)
