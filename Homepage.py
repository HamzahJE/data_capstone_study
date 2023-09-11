import streamlit as st
import streamlit.components.v1 as components
from functions import embeded_linkedin
st. set_page_config(layout="wide",
    page_title='Purpose',
    page_icon='👋'
)

st.title('About Me:')

col1,col2,col3 = st.columns((1,1,1))
with col1:
    st.markdown('#### Hey, My name is `Hamzah`!')
    st.markdown('#### I am a developer and data analyst based in the Detroit metropolitan area.')
with col3:
    components.html(embeded_linkedin['linkedin'],height=300)


st.write('# Purpose')
red_covid='<span style="color:red">COVID-19</span>'
st.markdown('### The goal of this study is to illustrate the effects that *COVID-19* and the *Russian invasion of Ukraine* had on `Prices`, `CPI`, and `GDP`')
st.markdown('##### 👈 Select a Page')

col1,col2 = st.columns((1,1))

with col1:
    st.write('# Sources:')
    st.write('### - [Commodity Prices Dataset](https://www.kaggle.com/datasets/debashish311601/commodity-prices)')
    st.write('### - [Quarterly Real Gross Domestic Product](https://www.statista.com/statistics/248154/quarterly-us-real-gross-domestic-product-gdp/)')
    st.write('### - [Consumer Price Index ](https://www.statista.com/statistics/716668/us-consumer-price-index-energy/)')
    st.write('### - [Monthly growth in consumer prices of food products](https://www.statista.com/statistics/1121060/cpi-food-at-home-monthly-growth-during-covid-us/)')

with col2:
    st.write('# Tech Used:')
    st.write('### - [Python](https://www.python.org/) | [Jupyter Notebook](https://jupyter.org/) | [Anaconda](https://www.anaconda.com/)')
    st.write('### - [Pandas](https://pandas.pydata.org/) | [Numpy](https://numpy.org/) | [Statsmodels](https://www.statsmodels.org/stable/index.html) | [Sklearn](https://scikit-learn.org/stable/#)')
    st.write('### - [Matplotlib](https://matplotlib.org/) | [Seaborn](https://seaborn.pydata.org/) | [Altair](https://altair-viz.github.io/) | [Plotly](https://plotly.com/python/)')


st.sidebar.success('👆 Select a page above 👆')
with st.sidebar:
    st.markdown('___')
    st.markdown("Developed by `Hamzah`  ⇨  [GitHub Repo](https://github.com/HamzahJE/data_capstone_study).")
    st.markdown("Check Out My` [Portfolio](https://hamzahje.github.io/). ")

    st.markdown('___')

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
