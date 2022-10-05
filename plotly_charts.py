import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import plotly.express as px
def load_data():
    prices = pd.read_csv(r'dataframes/commodity_futures.csv')
    rGDP= pd.read_csv(r'dataframes/quarterly-rGDP.csv')
    eCPI=pd.read_csv(r'dataframes/energy-CPI.csv')
    fCPI=pd.read_csv(r'dataframes/monthly-food-CPI-covid.csv')
    return prices,rGDP,eCPI,fCPI
prices,rGDP,eCPI,fCPI = load_data() #importing Dataframes
# # # # # # # # # # # # # # # DATA CLEANING # # # # # # # # # # # # # # # # # # # # #
# Prices Dataframe Cleaning
prices.dropna(inplace=True) #dropping missing values 
prices.columns=prices.columns.str.lower() #making all column names lowercased
prices.date=pd.to_datetime(prices.date)
prices.date.describe()
prices.index=pd.DatetimeIndex(data=prices.date)
prices.drop(columns='date',inplace=True)
prices_simple=prices.loc[:,['copper','wheat','gasoline']]
prices_simple_norm=(prices_simple-prices_simple.mean())/prices_simple.std()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# rGDP Dataframe Cleaning
rGDP.columns=rGDP.columns.str.lower()
rGDP.quarter=rGDP.quarter.str.replace(" '",'20')
rGDP.quarter=rGDP.quarter.str.replace("Q1",'1/1/')
rGDP.quarter=rGDP.quarter.str.replace("Q2",'4/1/')
rGDP.quarter=rGDP.quarter.str.replace("Q3",'7/1/')
rGDP.quarter=rGDP.quarter.str.replace("Q4",'10/1/')
rGDP.quarter=pd.to_datetime(rGDP.quarter)
rGDP.index=pd.DatetimeIndex(data=rGDP.quarter)
rGDP.drop(columns='quarter',inplace=True)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# eCPI Dataframe Cleaning
eCPI.columns=eCPI.columns.str.lower()
eCPI.index=eCPI.year
eCPI.drop(columns='year',inplace=True)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# fCPI Dataframe Cleaning
fCPI.rename(columns={'Month/year':'date'},inplace=True)
fCPI.rename(columns={'percent change':'percent_change'},inplace=True)
fCPI.drop(columns='percent', inplace=True)
fCPI.index=fCPI.date

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
prices_simple_chart=px.line(data_frame=prices_simple,labels={'value':"Values",'date':''},title='Dataframe')
prices_simple_chart.add_vrect(x0=pd.to_datetime('1/31/2020'), x1=pd.to_datetime('2/24/2022'),line_width=0, fillcolor="red", opacity=0.2, annotation_text="WHO Issues Global Health Emergency", annotation_position="top left",annotation=dict(font_size=10))
prices_simple_chart.add_vrect(x0=pd.to_datetime('2/24/2022'), x1=pd.to_datetime(prices_simple.index.max()),line_width=0, fillcolor="blue", opacity=0.2, annotation_text="Russia Invades<br>Ukraine", annotation_position="top left",annotation=dict(font_size=10))
prices_simple_chart.update_xaxes(range=[pd.to_datetime('1/1/2014'), pd.to_datetime(prices_simple.index.max())])
prices_simple_chart.update_traces(mode="lines", hovertemplate=None)
prices_simple_chart.update_layout(hovermode="x unified", legend_title="Commodity Name")
prices_simple_chart.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(step="all",
                    label="View all Data"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
prices_simple_norm_chart=px.line(data_frame=prices_simple_norm,labels={'value':"Values",'date':''},title='Dataframe (normalized)' )
prices_simple_norm_chart.add_vrect(x0=pd.to_datetime('1/31/2020'), x1=pd.to_datetime('2/24/2022'),line_width=0, fillcolor="red", opacity=0.2, annotation_text="WHO Issues Global Health Emergency", annotation_position="top left",annotation=dict(font_size=10))
prices_simple_norm_chart.add_vrect(x0=pd.to_datetime('2/24/2022'), x1=pd.to_datetime(prices_simple.index.max()),line_width=0, fillcolor="blue", opacity=0.2, annotation_text="Russia Invades<br>Ukraine", annotation_position="top left",annotation=dict(font_size=10))
prices_simple_norm_chart.update_xaxes(range=[pd.to_datetime('1/1/2014'), pd.to_datetime(prices_simple.index.max())])
prices_simple_norm_chart.update_traces(mode="lines", hovertemplate=None)
prices_simple_norm_chart.update_layout(hovermode="x unified", legend_title="Commodity Name")
# Add range slider
prices_simple_norm_chart.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(step="all",label="View all Data"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
#graphing standerized dataframe 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
copper_price_chart=px.line(data_frame=prices_simple.copper ,labels={'value':"Copper Price  €",'date':''},title='' )
copper_price_chart.add_vrect(x0=pd.to_datetime('1/31/2020'), x1=pd.to_datetime('2/24/2022'),line_width=0, fillcolor="red", opacity=0.2, 
                annotation_text="WHO Issues Global<br>Health Emergency",annotation_position="top left",annotation=dict(font_size=12))
copper_price_chart.add_vrect(x0=pd.to_datetime('2/24/2022'), x1=pd.to_datetime(prices_simple.index.max()),line_width=0, fillcolor="blue", opacity=0.2, 
                annotation_text="Russia Invades<br>Ukraine", annotation_position="bottom right",annotation=dict(font_size=12))
copper_price_chart.update_xaxes(range=[pd.to_datetime('1/1/2014'), pd.to_datetime(prices_simple.index.max())])
copper_price_chart.update_traces(mode="lines", hovertemplate=None)
copper_price_chart.update_layout(hovermode="x unified" , legend_title="Commodity Name",showlegend=False)
# adding chart annotations 
copper_price_chart.add_annotation(
        x=pd.to_datetime('1/31/2020'),
        y=prices_simple.copper['1/31/2020'],
        xref="x",
        yref="y",
        text='Copper prices fall<br>slightly then they<br>increase exponentially',
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-30,ay=-80,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.9)
copper_price_chart.add_annotation(
        x=pd.to_datetime('2/24/2022'),
        y=prices_simple.copper.max(),
        xref="x",
        yref="y",
        text='Copper prices<br>hit a new record<br>in March 2022',
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-70,ay=130,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.9)

# Add range slider
copper_price_chart.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(step="all",
                    label="View all Data"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
wheat_price_chart=px.line(data_frame=prices_simple.wheat ,labels={'value':"Wheat Price  €",'date':''},title='' )
wheat_price_chart.add_vrect(x0=pd.to_datetime('1/31/2020'), x1=pd.to_datetime('2/24/2022'),line_width=0, fillcolor="red", opacity=0.2, 
                annotation_text="WHO Issues Global<br>Health Emergency",annotation_position="top left",annotation=dict(font_size=12))
wheat_price_chart.add_vrect(x0=pd.to_datetime('2/24/2022'), x1=pd.to_datetime(prices_simple.index.max()),line_width=0, fillcolor="blue", opacity=0.2, 
                annotation_text="Russia Invades<br>Ukraine", annotation_position="bottom right",annotation=dict(font_size=12))
wheat_price_chart.update_xaxes(range=[pd.to_datetime('1/1/2014'), pd.to_datetime(prices_simple.index.max())])
wheat_price_chart.update_traces(mode="lines", hovertemplate=None)
wheat_price_chart.update_layout(hovermode="x unified" , legend_title="Commodity Name",showlegend=False )
# adding wheat_price_chart annotations 
wheat_price_chart.add_annotation(
        x=pd.to_datetime('1/31/2020'),
        y=prices_simple.wheat['1/31/2020'],
        xref="x",
        yref="y",
        text='Wheat prices begin<br>an upward trend',
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-20,ay=-50,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.9)
wheat_price_chart.add_annotation(
        x=pd.to_datetime('2/24/2022'),
        y=prices_simple.wheat.max(),
        xref="x",
        yref="y",
        text="Wheat prices<br>hit a new record<br>in March 2022",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-120,ay=50,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.9)


# Add range slider
wheat_price_chart.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(step="all",
                    label="View all Data"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

gasoline_price_chart=px.line(data_frame=prices_simple.gasoline ,labels={'value':"Gasoline Price  €",'date':''},title='' )
gasoline_price_chart.add_vrect(x0=pd.to_datetime('1/31/2020'), x1=pd.to_datetime('2/24/2022'),line_width=0, fillcolor="red", opacity=0.2, 
                annotation_text="WHO Issues Global<br>Health Emergency",annotation_position="top left",annotation=dict(font_size=12))
gasoline_price_chart.add_vrect(x0=pd.to_datetime('2/24/2022'), x1=pd.to_datetime(prices_simple.index.max()),line_width=0, fillcolor="blue", opacity=0.2, 
                annotation_text="Russia Invades<br>Ukraine", annotation_position="bottom right",annotation=dict(font_size=12))
gasoline_price_chart.update_xaxes(range=[pd.to_datetime('1/1/2014'), pd.to_datetime(prices_simple.index.max())])
gasoline_price_chart.update_traces(mode="lines", hovertemplate=None)
gasoline_price_chart.update_layout(hovermode="x unified" , legend_title="Commodity Name",showlegend=False)
# adding gasoline_price_chart annotations 
gasoline_price_chart.add_annotation(
        x=pd.to_datetime('1/31/2020'),
        y=prices_simple.gasoline['1/31/2020'],
        xref="x",
        yref="y",
        text='Gasoline prices fall<br>slightly then they<br>increase exponentially',
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-30,ay=-85,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.9)
gasoline_price_chart.add_annotation(
        x=pd.to_datetime('6/1/2022'),
        y=prices_simple.gasoline.max(),
        xref="x",
        yref="y",
        text="Gasoline prices<br>hit a new record<br>in June 2022",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-150,ay=60,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.9)
# Add range slider
gasoline_price_chart.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(step="all",
                    label="View all Data"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
pairplot_chart=px.scatter_matrix(prices_simple)
pairplot_chart.update_layout(
    title='Pairplot',
    width=600,
    height=600,
    hovermode='closest',
)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
df_corr=prices_simple.corr()#making the correlation table
corr_chart=px.imshow(df_corr, text_auto=True, aspect="auto",color_continuous_scale='RdBu_r', origin='lower')
corr_chart.update_layout(
    title='Correlation Chart',
    dragmode='select',
    width=600,
    height=600,
)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# indendent variable
x_dep=prices_simple.wheat
# dependent variable
y=prices_simple.copper
equation=(0.0028*x_dep)+1.4694
regression_chart=px.scatter(y=y,x=x_dep,trendline='ols', trendline_color_override="red",labels={'y':"Price of Copper",'x':"Price of Wheat"},title='Machine Learning Regression Plot (Copper & Wheat)')
regression_chart.update_layout(
    dragmode='select',
    width=600,
    height=600,
)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

rgdp_chart=px.line(data_frame=rGDP.gdp ,labels={'value':"Monthly US Real GDP",'quarter':''},title='' )
rgdp_chart.add_vrect(x0=pd.to_datetime('1/31/2020'), x1=pd.to_datetime('2/24/2022'),line_width=0, fillcolor="red", opacity=0.2, 
                annotation_text="WHO Issues Global<br>Health Emergency",annotation_position="top left",annotation=dict(font_size=12))
rgdp_chart.add_vrect(x0=pd.to_datetime('2/24/2022'), x1=pd.to_datetime(rGDP.gdp.index.max()),line_width=0, fillcolor="blue", opacity=0.2)

rgdp_chart.add_vline(x=pd.to_datetime('1/31/2020'),line_width=2)
rgdp_chart.add_vline(x=pd.to_datetime('2/24/2022'),line_width=2)

rgdp_chart.update_xaxes(range=[pd.to_datetime('1/1/2014'), pd.to_datetime(rGDP.gdp.index.max())])
rgdp_chart.update_traces(mode="lines", hovertemplate=None)
rgdp_chart.update_layout(hovermode="x unified" , legend_title="Variable",showlegend=False)
# adding rgdp_chart annotations 
rgdp_chart.add_annotation(

        x=pd.to_datetime('1/1/2020'),
        y=rGDP.gdp['1/1/2020'],
        xref="x",
        yref="y",
        text="In the events leading up to COVID-19<br>we saw a dip in GDP",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#ffffff"
            ),
        align="center",arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-300,ay=70,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.8
        )
rgdp_chart.add_annotation(

        x=pd.to_datetime('1/1/2022'),
        y=rGDP.gdp['1/1/2022'],
        xref="x",
        yref="y",
        text="In the events leading up to the <br>Ukraine-Russian Conflict a downward<br>trend took place",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#ffffff"
            ),
        align="center",arrowhead=2,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-125,ay=100,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.8
        )
rgdp_chart.update_layout(

    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(step="all",
                    label="View all Data"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
ecpi_chart=px.line(data_frame=eCPI,labels={'value':"Energy CPI",'year':''},title='' )
ecpi_chart.add_vrect(x0=2020.16, x1=eCPI.index.max(),line_width=0, fillcolor="red", opacity=0.2, 
                annotation_text="WHO Issues Global<br>Health Emergency",annotation_position="top right",annotation=dict(font_size=12))
ecpi_chart.update_xaxes(range=[2012, eCPI.index.max()])
ecpi_chart.update_traces(mode="lines", hovertemplate=None)
ecpi_chart.update_layout(hovermode="x unified" , legend_title="Variable",showlegend=False)
# adding ecpi_chart annotations 
ecpi_chart.add_annotation(
        x=2020.16,
        y=101,
        xref="x",
        yref="y",
        text="Energy costs saw an upward<br>trend during COVID",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",arrowhead=1,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-100,ay=-150,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="gray",opacity=0.8
        )
ecpi_chart.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="-"
    )
)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
fcpi_chart=px.bar(fCPI.percent_change,text_auto=True,labels={'value':"Percentage Change",'date':'Percentage Change of Food CPI'},title='' )
fcpi_chart.update_layout(legend_title="Variable",showlegend=False)
fcpi_chart.add_annotation(
        x='Apr-20',
        y=-0.2 ,
        xref="x",
        yref="y",
        text="We saw a clear peak in the price of<br>food during the COVID months",
        showarrow=False,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="#ffffff"
            ),
        align="center",arrowhead=1,arrowsize=1,arrowwidth=2,arrowcolor="#636363",ax=-100,ay=-150,bordercolor="#c7c7c7",borderwidth=2,borderpad=4,bgcolor="purple",opacity=0.8
        )

fcpi_chart.update_traces(textposition='outside')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

embeded_linkedin={'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                    <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="hamzahje" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/hamzahje?trk=profile-badge"></a></div>"""}