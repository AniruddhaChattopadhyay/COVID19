import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.io as pio
from plotly.subplots import make_subplots
from pathlib import Path
from iexfinance.stocks import get_historical_data
import datetime
import plotly.graph_objects as go
from dateutil.relativedelta import relativedelta
import pandas as pd
import plotly.express as px
import dash_gif_component as Gif


#----------------------------Figure Functions-----------------------------------------------------------------

def world_plot(type, color):
    grouped = data.groupby('date')['date', 'confirmed', 'deaths', 'active', 'recovered'].sum().reset_index()

    fig = go.Figure()

    if (type == "confirmed + active"):
        fig.add_trace(go.Scatter(x=grouped["date"], y=grouped['confirmed'],
                                 mode='lines+markers', line=dict(color="#003EA9"), name="Confimed Cases"))

        fig.add_trace(go.Scatter(x=grouped["date"], y=grouped['active'],
                                 mode='lines+markers', line=dict(color="#44AFFE"), name="Active Cases"))

        fig.update_layout(title="Worldwide " + type + " Cases",
                          xaxis_title="Date",
                          yaxis_title=type + " Cases",
                          font=dict(color="#7f7f7f")
                          )
    else:
        fig.add_trace(go.Scatter(x=grouped["date"], y=grouped[type],
                                 mode='lines+markers', line=dict(color=color), name=type + " Cases"))
        fig.update_layout(title="Worldwide " + type + " Cases",
                          xaxis_title="Date",
                          yaxis_title=type + " Cases",
                          font=dict(color="#7f7f7f")
                          )
    return fig

def world_heatmap(type,color,scale=0.2):
    avg = latest_grouped[type].sum()/latest_grouped[type].count()
    max = latest_grouped[type].max()
    # fig = px.choropleth(latest_grouped, locations="country",
    #                     locationmode='country names', color=type,
    #                     hover_name="country", range_color=[0,max*scale],
    #                     color_continuous_midpoint = avg,
    #                     color_continuous_scale=color,
    #                     title="Countries with "+type +" Cases",height=1000)

    import pandas as pd
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

    for col in df.columns:
        df[col] = df[col].astype(str)

    df['text'] = df['state'] + '<br>' + \
                 'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
                 'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
                 'Wheat ' + df['wheat'] + ' Corn ' + df['corn']


    fig = go.Choropleth(
        locations=latest_grouped['country'],  # Spatial coordinates
        z=latest_grouped[type],  # Data to be color-coded
        locationmode='country names',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="Millions USD",
    )


    return fig


def world_animation(type, color):
    formated_gdf = data.groupby(['date', 'country'])['confirmed', 'deaths', 'active', 'recovered'].max()
    formated_gdf = formated_gdf.reset_index()
    formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
    formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
    formated_gdf['size'] = formated_gdf['recovered'].pow(0.3)

    fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
                         color=type, size='size', hover_name="country",
                         range_color=[0, 100],
                         projection="natural earth", animation_frame="date",
                         title='COVID-19: ' + type + ' Over Time', color_continuous_scale=color)
    #     fig.update(layout_coloraxis_showscale=False)
    return fig


#-------------------------------------Color Coding-------------------------------------------------------------
color_confirmed =['white','#CCD4DF','#AEBFD5','#96D1D3','#7898C0','#6287B6','#4B75A8','#3A679F',
                           '#2B5697','#0A3B78']
color_active = ['white','#EAD5F0','#DEBBE9','#CF9BDF','#C884DE','#B863D2','#AE4ACD','#9E31C0',
                '#9621BB','#8A07B3']

color_death = ['white','#FEE2DD','#FED0C7','#FEB5A8','#FFA190','#FE9683','#FE8670','#FB745C',
                           '#F3674E','#E95A40']

color_recovered = ['white','#E6F6B7','#E9FCAA','#E5FB9F','#E3FC91','#DBFE6F','#E9FE64','#D2FD50','#D3FF47','#CCFB39',
                   '#BDEA16']


#----------------------------------------Initialize----------------------------------------------------------------------


app = dash.Dash(__name__)

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

#df = pd.read_csv("AAPL.csv")
#
# trace_close = go.Scatter(x=list(df.index),
#                          y=list(df.Close),
#                          name= "Close",
#                          line= dict(color="#006EFF"))
#data = [trace_close]

#layout = dict(title="Chart",
#             showlegend=False)
# # fig = dict(data=data, layout=layout)


df = px.data.gapminder()

# fig = px.bar(df, x="continent", y="pop", color="continent",
#   animation_frame="year", animation_group="country", range_y=[0,4000000000])

#-----------------------------Dataset Processing-----------------------------------------------------------------

data = pd.read_csv('data_dir\covid_19_clean_complete.csv', parse_dates=['Date'],engine='python')
data.rename(columns={'Date': 'date',
                     'Province/State':'state',
                     'Country/Region':'country',
                     'Confirmed': 'confirmed',
                     'Deaths':'deaths',
                     'Recovered':'recovered'
                    }, inplace=True)


cases = ['confirmed', 'deaths', 'recovered', 'active']

# Active Case = confirmed - deaths - recovered
data['active'] = data['confirmed'] - data['deaths'] - data['recovered']

# replacing Mainland china with just China
data['country'] = data['country'].replace('Mainland China', 'China')

# filling missing values
data[['state']] = data[['state']].fillna('')
data[cases] = data[cases].fillna(0)
data.rename(columns={'Date':'date'}, inplace=True)

data['state'] = data['state'].fillna('')
temp = data[[col for col in data.columns if col != 'state']]

latest = temp[temp['date'] == max(temp['date'])].reset_index()
latest_grouped = latest.groupby('country')['confirmed', 'deaths','active','recovered'].sum().reset_index()






#-----------------Figure Plotting----------------------------------------------------------------------------------

print(type(go.Figure()))
print('***********************')
print(type(go.Scatter()))
print('***********************')
print(type(go.Candlestick()))
print('***********************')
print(type(go.Choropleth()))

avg = latest_grouped['deaths'].sum()/latest_grouped['deaths'].count()
max = latest_grouped['deaths'].max()
fig_test = px.choropleth(latest_grouped, locations="country",
                        locationmode='country names', color='deaths',
                        hover_name="country", range_color=[0,max*0.2],
                        color_continuous_midpoint = avg,
                        color_continuous_scale=color_confirmed,
                        title="Countries with "+'deaths' +" Cases",height=1000)


#-----------------Website Layout----------------------------------------------------------------------------------


app.layout  = html.Div([

    html.Div([
            html.H2("Stock App"),
            html.Img(src="/assets/stock-icon.png")
        ], className="banner"),

    html.Div([html.H1("Hello World", id="header",n_clicks=0),
        html.Div([
            html.Button("Confirmed",className="button",id="confBtn",n_clicks=0,name="confirmed"),
            html.Button("Active", className="button",id="activeBtn",n_clicks=0,name="active"),
            html.Button("Death", className="button",id="deathBtn",n_clicks=0,name="deaths"),
            html.Button("Recovered", className="button",id="recBtn",n_clicks=0,name="recovered"),
            dcc.Graph(id="home-graph",
                    config={'displayModeBar': False, 'staticPlot':False},
                      )],
            style={'width': '80%', 'display': 'inline-block', 'text-align':'left' }


    )], style={'text-align': 'center'}
    ),
    html.Div([

        Gif.GifPlayer(
            gif='assets/myAnimation.gif',
            still='assets/pic.png',
            autoplay=True,

        )
    ]),



], )

@app.callback(Output("home-graph", "figure"),
              [Input("header","n_clicks")]
              )
def conf_btn(nc):
    # fig_c = world_heatmap('confirmed', color_confirmed, 0.2)
    # fig_a = world_heatmap('active', color_active, 0.2)
    # fig_d = world_heatmap('deaths', color_death, 0.2)
    # fig_r = world_heatmap('recovered', color_recovered, 0.2)

    # fig_a = world_plot('active','blue')
    # fig_d = world_plot('active','blue')
    # fig_c = world_plot('confirmed','blue')
    # fig_r = world_plot('deaths','blue')

    # data_fig = [fig_c, fig_a, fig_d, fig_r]
    #
    # updatemenus = list([
    #     dict(
    #         buttons=list([
    #             dict(
    #                 args=[{'visible': [True, False, False,False]}],
    #                 label='Con',
    #                 method='update'
    #             ),
    #             dict(
    #                 args=[{'visible': [False, True, False,False]}],
    #                 label='Candle',
    #                 method='update'
    #             ),
    #             dict(
    #                 args=[{'visible': [False, False, True,False]}],
    #                 label='Bar',
    #                 method='update'
    #             ),
    #             dict(
    #                 args=[{'visible': [False, False, False ,True]}],
    #                 label='x',
    #                 method='update'
    #             ),
    #         ]),
    #     ),
    # ])
    #
    # fig_c.update_layout(
    #
    # )
    #
    # layout = dict(
    #     updatemenus=updatemenus
    # )
    #
    # return {'data':data_fig, 'layout':layout}

    df2 = pd.read_csv("AAPL.csv")
    #
    # trace_line = go.Scatter(x=list(df.index),
    #                         y=list(df['Close']),
    #                         # visible=False,
    #                         name="Close",
    #                         showlegend=False)
    #
    # trace_candle = go.Candlestick(x=df.index,
    #                               open=df["Open"],
    #                               high=df["High"],
    #                               low=df["Low"],
    #                               close=df["Close"],
    #                               # increasing=dict(line=dict(color="#00ff00")),
    #                               # decreasing=dict(line=dict(color="white")),
    #                               visible=False,
    #                               showlegend=False)
    #
    # trace_bar = go.Ohlc(x=df.index,
    #                     open=df["Open"],
    #                     high=df["High"],
    #                     low=df["Low"],
    #                     close=df["Close"],
    #                     # increasing=dict(line=dict(color="#888888")),
    #                     # decreasing=dict(line=dict(color="#888888")),
    #                     visible=False,
    #                     showlegend=False)
    #
    # data = [trace_line, trace_candle, trace_bar]


    # fig_a = world_plot('active', 'blue')
    # fig_d = world_plot('active','blue')
    # fig_c = world_plot('confirmed','blue')
    #
    fig_c = world_heatmap('confirmed', color_confirmed, 0.2)

    trace_candle = go.Candlestick(x=df.index,
                                                                open=df2["Open"],
                                                                high=df2["High"],
                                                                low=df2["Low"],
                                                                close=df2["Close"],
                                                                # increasing=dict(line=dict(color="#00ff00")),
                                                                # decreasing=dict(line=dict(color="white")),
                                                                visible=False,
                                                                showlegend=False)
    fig_r = world_heatmap('recovered',color_recovered,0.2)
    fig_a = trace_candle
    fig_d = world_heatmap('deaths', color_death, 0.2)

    data_fig = [fig_c, fig_r, fig_d]

    updatemenus = list([
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False]}],
                    label='Confirmed',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, False]}],
                    label='Recovered',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, False, True]}],
                    label='Deaths',
                    method='update'
                ),
            ]),
            direction='down',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=0,
            xanchor='left',
            y=1.05,
            yanchor='top'
        ),
    ])

    layout = dict(
        height = 800,
        title="Title",
        updatemenus=updatemenus,
        autosize=True,
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(count=1,
                         label='YTD',
                         step='year',
                         stepmode='todate'),
                    dict(count=1,
                         label='1y',
                         step='year',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type='date'
        )
    )

    return {
        "data": data_fig,
        "layout": layout
    }

if __name__=="__main__":
    app.run_server(debug=True)