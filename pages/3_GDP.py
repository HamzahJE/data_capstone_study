import streamlit as st
import streamlit.components.v1 as components
from functions import rgdp_chart, seaborn_chart
st. set_page_config(layout="wide",
    page_title='Effect on GDP',
    page_icon='🏦'
)
st.sidebar.success('👆 Select a page above 👆')


st.title('Effect on the Gross Domestic Product')

st.plotly_chart(rgdp_chart, use_container_width=True)

st.title('Further Reading:')
st.write('##### [Article by the Centre for Economic Policy Research](https://cepr.org/voxeu/columns/impact-war-ukraine-economic-uncertainty)')
st.write('##### [Article by the US Federal Reserve](https://www.federalreserve.gov/econres/notes/feds-notes/the-effect-of-the-war-in-ukraine-on-global-activity-and-inflation-20220527.html#:~:text=The%20increased%20geopolitical%20risks%20induced,central%20banks%20around%20the%20world.)')
st.markdown('# Code snipets:')
if st.checkbox('Click to view a Data cleaning code snipet:'):
    st.code("# Prices Dataframe Cleaning\nimport pandas as pd#importing pandas\nprices.dropna(inplace=True) #dropping missing values\nprices.columns=prices.columns.str.lower() #making all column names lowercased\nprices.date=pd.to_datetime(prices.date)#converting date column to datetime\nprices.index=pd.DatetimeIndex(data=prices.date)#setting the dates as the index\nprices.drop(columns='date',inplace=True)#dropping the data column since we now have the date as the index")
if st.checkbox('Click to view a simple Data visualization code snipet & the graph it creates:(using seaborn)'):
    st.code("import matplotlib.pyplot as plt#importing matplotlib\nimport seaborn as sns#importing seaborn\nplt.figure(figsize=(24,8))#declaring graph size\ngraph=sns.lineplot(prices_simple.wheat,label='Wheat Price  €')#making a seaborn line graph using prices of wheat(dates are in the index),and giving the graphed line a label\ngraph.axvline(pd.to_datetime('1/31/2020'),c='r',label='WHO Issues Global Health Emergency',ymin=.1,ymax=.55)#drawing a line on 1/31/2020 and giving it a label and a color\ngraph.axvline(pd.to_datetime('2/24/2022'),c='black',label='Russia Invades Ukraine',ymin=.3,ymax=.98,)#drawing a line on 2/24/2022 and giving it a label and a color\nplt.xlabel('')#removing the x axis label\nplt.ylabel('Wheat Price  €')#adding a y axis label\nprops = dict(boxstyle='round', facecolor='#7393B3', alpha=0.5)#decalaring textbox properties\nstring1='Wheat prices begin an upward trend'#string used for the text box\nstring2='Wheat prices hit a new record in March 2022'#string used for the text box\ntext1=graph.text(0.7,0.4,string1,fontsize=14,transform=graph.transAxes,verticalalignment='center', bbox=props)#adding the 1st textbox to the graph and setting its location\ntext2=graph.text(0.9,0.2,string2,fontsize=14,transform=graph.transAxes,verticalalignment='center', bbox=props)#adding the 2nd textbox to the graph and setting its location\ngraph.legend()#code to show the labels I created\nplt.show()#code used to show the graph")
    st.pyplot(seaborn_chart,use_container_width=True)
st.sidebar.header('What Effect did *COVID-19* and the *Ukraine Conflict* have on GDP?')

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