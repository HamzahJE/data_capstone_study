import streamlit as st
import streamlit.components.v1 as components
from plotly_charts import prices_simple_chart,prices_simple_norm_chart,copper_price_chart,wheat_price_chart,gasoline_price_chart,pairplot_chart,corr_chart,regression_chart
st. set_page_config(layout="wide",
    page_title='Effect on Prices',
    page_icon='💲'
)
st.sidebar.success('⬆️ Select a page above ⬆️')

st.title('Effect on Prices')

# @st.cache
# def load_data():
#     from plotly_charts import prices_chart,prices_simple_chart,prices_simple_norm_chart,copper_price_chart,wheat_price_chart
#     return prices_chart,prices_simple_chart,prices_simple_norm_chart,copper_price_chart,wheat_price_chart

data_load_state = st.text('Loading data...')
# prices_chart,prices_simple_chart,prices_simple_norm_chart,copper_price_chart,,wheat_price_chart=load_data()
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show normalized chart of all products'):
    st.plotly_chart(prices_simple_norm_chart, use_container_width=True)

# st.subheader('Price of Copper')
st.plotly_chart(copper_price_chart, use_container_width=True)

# st.subheader('Price of Wheat')
st.plotly_chart(wheat_price_chart, use_container_width=True)

# st.subheader('Price of Gasoline')
st.plotly_chart(gasoline_price_chart, use_container_width=True)


st.title('Machine Learning')
col1, col2 = st.columns((1,1))
with col1:
    st.plotly_chart(pairplot_chart )
with col2:
    st.plotly_chart(corr_chart)
st.plotly_chart(regression_chart)



