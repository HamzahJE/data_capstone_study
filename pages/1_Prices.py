import streamlit as st
import streamlit.components.v1 as components
from plotly_charts import prices_simple_chart,prices_simple_norm_chart,copper_price_chart,wheat_price_chart,gasoline_price_chart,pairplot_chart,corr_chart,regression_chart
st. set_page_config(layout="wide",
    page_title='Effect on Prices',
    page_icon='💰'
)
st.sidebar.success('⬆️ Select a page above ⬆️')

st.title('Effect on Prices')

if st.checkbox('Show charts of all products'):
    col1,col2 = st.columns((1,1))
    with col1:
        st.plotly_chart(prices_simple_norm_chart, use_container_width=True)
    with col2:
        st.plotly_chart(prices_simple_chart, use_container_width=True)

# st.subheader('Price of Copper')
st.plotly_chart(copper_price_chart, use_container_width=True)

# st.subheader('Price of Wheat')
st.plotly_chart(wheat_price_chart, use_container_width=True)

# st.subheader('Price of Gasoline')
st.plotly_chart(gasoline_price_chart, use_container_width=True)


st.title('Machine Learning')
col1,col2,col3 = st.columns((1,1,1))
with col1:
    st.plotly_chart(pairplot_chart )
with col2:
    st.plotly_chart(corr_chart)
with col3:
    st.plotly_chart(regression_chart)

st.sidebar.header('What Effect did *COVID-19* and the *Ukraine Conflict* have on prices of goods?')

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

