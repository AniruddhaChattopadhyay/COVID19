f = open("color.txt","r")
li = []
count=0
for a in f:
    count = count + 1
    if(count%10 ==1 or count%10==2 or count%10 == 3):
        continue
    li = li +  [str(a).strip('\n')]
print(li)
# import numpy as np
# import pandas as pd
#
# import plotly.graph_objects as go
# import plotly.express as px
# import plotly.io as pio
# # pio.templates.default = "plotly_dark"
# from plotly.subplots import make_subplots
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from pathlib import Path
# data_dir = Path('D:\PycharmProjects\Covid19\data_dir')
#
# import os
# os.listdir(data_dir)
#
# app =dash.Dash()
#
# data = pd.read_csv(data_dir/'covid_19_clean_complete.csv', parse_dates=['Date'],engine='python')
# data.head()
#
# data.info()
#
# data.rename(columns={'Date': 'date',
#                      'Province/State':'state',
#                      'Country/Region':'country',
#                      'Confirmed': 'confirmed',
#                      'Deaths':'deaths',
#                      'Recovered':'recovered'
#                     }, inplace=True)
#
#
# cases = ['confirmed', 'deaths', 'recovered', 'active']
#
# # Active Case = confirmed - deaths - recovered
# data['active'] = data['confirmed'] - data['deaths'] - data['recovered']
#
# # replacing Mainland china with just China
# data['country'] = data['country'].replace('Mainland China', 'China')
#
# # filling missing values
# data[['state']] = data[['state']].fillna('')
# data[cases] = data[cases].fillna(0)
# data.rename(columns={'Date':'date'}, inplace=True)
#
# print("External Data")
# print(f"Earliest Entry: {data['date'].min()}")
# print(f"Last Entry:     {data['date'].max()}")
# print(f"Total Days:     {data['date'].max() - data['date'].min()}")
#
# import plotly
# grouped = data.groupby('date')['date', 'confirmed', 'deaths'].sum().reset_index()
#
#
# fig_confirm = go.Figure()
#
# fig_confirm.add_trace(go.Scatter(x = grouped["date"],y = grouped["confirmed"],mode = 'lines+markers'))
# fig_confirm.update_layout(title="Worldwide Confirmed Cases",
#                  xaxis_title = "Date",
#                   yaxis_title = "Confirmed Cases",
#                   font = dict(color = "#7f7f7f")
#                  )
#
# fig_deaths = go.Figure()
# fig_deaths.update_layout(title="Worldwide Confirmed Cases",
#                  xaxis_title = "Date",
#                   yaxis_title = "Deaths",
#                  )
# fig_deaths.add_trace(go.Scatter(x = grouped["date"],y = grouped["deaths"], mode = 'lines+markers',line=dict(color='red')))
#
# formated_gdf = data.groupby(['date', 'country'])['confirmed', 'deaths'].max()
# formated_gdf = formated_gdf.reset_index()
# formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# formated_gdf['size'] = formated_gdf['confirmed'].pow(0.3)
#
#
# fig_anime = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
#                      color="deaths", size='size', hover_name="country",
#                      range_color= [0, 500],
#                      projection="natural earth", animation_frame="date", scope="asia",
#                      title='COVID-19: Deaths Over Time in EUROPE', color_continuous_scale="Viridis", height=1200)
# # fig_anime.update(layout_coloraxis_showscale=False)
# fig_anime.update_layout(geo = dict(countrywidth=1))
# # margin = {"r":500,"t":0,"l":500,"b":0}
#
#
# fig_new = px.scatter_geo(formated_gdf, locations="country",color="confirmed",hover_name='country',
#                      size="size",projection='natural earth',scope="europe" # size of markers, "pop" is one of the columns of gapminder
#                      )
# fig_new2 = go.Figure(go.Scattergeo())
# fig_new2.update_geos(projection_type="orthographic")
# fig_new2.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
#
#
# from urllib.request import urlopen
# import json
# with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
#     counties = json.load(response)
#
# print(counties)
# import pandas as pd
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                    dtype={"fips": str})
#
# print(df.head())
#
# fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
#                            color_continuous_scale="Viridis",
#                            range_color=(0, 12),
#                            mapbox_style="carto-positron",
#                            zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
#                            opacity=0.5,
#                            labels={'unemp':'unemployment rate'}
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()
#
#
#
# app.layout = html.Div([
#     html.H1("Confirm Cases"),
#     html.Div(
#     dcc.Graph(id = "Confirmed",figure = fig_confirm)
#     ),
#     html.H1("Deaths"),
#     html.Div(
#         dcc.Graph(id="deaths", figure=fig_deaths),
#     ),
#     html.H1("anime"),
#         html.Div(
#             dcc.Graph(id="anime", figure=fig_anime),
#         ),
#     html.H1("anime2"),
#         html.Div(
#             dcc.Graph(id="anime2", figure=fig_new),
#         )
# ])
# if __name__ == "__main__":
#     app.run_server(debug=True,port=8080,host="10.145.142.110")
#
# #
# # data['state'] = data['state'].fillna('')
# # temp = data[[col for col in data.columns if col != 'state']]
# #
# # latest = temp[temp['date'] == max(temp['date'])].reset_index()
# # latest_grouped = latest.groupby('country')['confirmed', 'deaths'].sum().reset_index()
# #
# # fig = px.choropleth(latest_grouped, locations="country",
# #                     locationmode='country names', color="confirmed",
# #                     hover_name="country", range_color=[1,5000],
# #                     color_continuous_scale="peach",
# #                     title='Countries with Confirmed Cases')
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # europe = list(['Austria','Belgium','Bulgaria','Croatia','Cyprus','Czechia','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Ireland',
# #                'Italy', 'Latvia','Luxembourg','Lithuania','Malta','Norway','Netherlands','Poland','Portugal','Romania','Slovakia','Slovenia',
# #                'Spain', 'Sweden', 'United Kingdom', 'Iceland', 'Russia', 'Switzerland', 'Serbia', 'Ukraine', 'Belarus',
# #                'Albania', 'Bosnia and Herzegovina', 'Kosovo', 'Moldova', 'Montenegro', 'North Macedonia'])
# #
# # europe_grouped_latest = latest_grouped[latest_grouped['country'].isin(europe)]
# #
# # fig = px.choropleth(europe_grouped_latest, locations="country",
# #                     locationmode='country names', color="confirmed",
# #                     hover_name="country", range_color=[1,2000],
# #                     color_continuous_scale='portland',
# #                     title='European Countries with Confirmed Cases', scope='europe', height=800)
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # fig = px.bar(latest_grouped.sort_values('confirmed', ascending=False)[:20][::-1],
# #              x='confirmed', y='country',
# #              title='Confirmed Cases Worldwide', text='confirmed', height=1000, orientation='h')
# # fig.show()
# #
# # fig = px.bar(europe_grouped_latest.sort_values('confirmed', ascending=False)[:10][::-1],
# #              x='confirmed', y='country', color_discrete_sequence=['#84DCC6'],
# #              title='Confirmed Cases in Europe', text='confirmed', orientation='h')
# # fig.show()
# #
# # fig = px.choropleth(latest_grouped, locations="country",
# #                     locationmode='country names', color="deaths",
# #                     hover_name="deaths", range_color=[1,100],
# #                     color_continuous_scale="peach",
# #                     title='Countries with Reported Deaths')
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # fig = px.choropleth(europe_grouped_latest, locations="country",
# #                     locationmode='country names', color="deaths",
# #                     hover_name="country", range_color=[1,100],
# #                     color_continuous_scale='portland',
# #                     title='Reported Deaths in EUROPE', scope='europe', height=800)
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # fig = px.bar(latest_grouped.sort_values('deaths', ascending=False)[:10][::-1],
# #              x='deaths', y='country',
# #              title='Confirmed Deaths Worldwide', text='deaths', orientation='h')
# # fig.show()
# #
# # fig = px.bar(europe_grouped_latest.sort_values('deaths', ascending=False)[:5][::-1],
# #              x='deaths', y='country', color_discrete_sequence=['#84DCC6'],
# #              title='Deaths in Europe', text='deaths', orientation='h')
# # fig.show()
# #
# # temp = data.groupby('date')['recovered', 'deaths', 'active'].sum().reset_index()
# # temp = temp.melt(id_vars="date", value_vars=['recovered', 'deaths', 'active'],
# #                  var_name='case', value_name='count')
# #
# #
# # fig = px.line(temp, x="date", y="count", color='case',
# #              title='Cases over time: Line Plot', color_discrete_sequence = ['cyan', 'red', 'orange'])
# # fig.show()
# #
# #
# # fig = px.area(temp, x="date", y="count", color='case',
# #              title='Cases over time: Area Plot', color_discrete_sequence = ['cyan', 'red', 'orange'])
# # fig.show()
# #
# # cleaned_latest = data[data['date'] == max(data['date'])]
# # flg = cleaned_latest.groupby('country')['confirmed', 'deaths', 'recovered', 'active'].sum().reset_index()
# #
# # flg['mortalityRate'] = round((flg['deaths']/flg['confirmed'])*100, 2)
# # temp = flg[flg['confirmed']>100]
# # temp = temp.sort_values('mortalityRate', ascending=False)
# #
# # fig = px.bar(temp.sort_values(by="mortalityRate", ascending=False)[:10][::-1],
# #              x = 'mortalityRate', y = 'country',
# #              title='Deaths per 100 Confirmed Cases', text='mortalityRate', height=800, orientation='h',
# #              color_discrete_sequence=['darkred']
# #             )
# # fig.show()
# #
# # flg['recoveryRate'] = round((flg['recovered']/flg['confirmed'])*100, 2)
# # temp = flg[flg['confirmed']>100]
# # temp = temp.sort_values('recoveryRate', ascending=False)
# #
# # fig = px.bar(temp.sort_values(by="recoveryRate", ascending=False)[:10][::-1],
# #              x = 'recoveryRate', y = 'country',
# #              title='Recoveries per 100 Confirmed Cases', text='recoveryRate', height=800, orientation='h',
# #              color_discrete_sequence=['#2ca02c']
# #             )
# # fig.show()
# #
# # formated_gdf = data.groupby(['date', 'country'])['confirmed', 'deaths'].max()
# # formated_gdf = formated_gdf.reset_index()
# # formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# # formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# # formated_gdf['size'] = formated_gdf['confirmed'].pow(0.3)
# #
# # fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
# #                      color="confirmed", size='size', hover_name="country",
# #                      range_color= [0, 1500],
# #                      projection="natural earth", animation_frame="date",
# #                      title='COVID-19: Spread Over Time', color_continuous_scale="portland")
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # formated_gdf = data.groupby(['date', 'country'])['confirmed', 'deaths'].max()
# # formated_gdf = formated_gdf.reset_index()
# # formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# # formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# # formated_gdf['size'] = formated_gdf['deaths'].pow(0.3)
# #
# # fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
# #                      color="deaths", size='size', hover_name="country",
# #                      range_color= [0, 100],
# #                      projection="natural earth", animation_frame="date",
# #                      title='COVID-19: Deaths Over Time', color_continuous_scale="peach")
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # formated_gdf = data.groupby(['date', 'country'])['confirmed', 'deaths', 'active', 'recovered'].max()
# # formated_gdf = formated_gdf.reset_index()
# # formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# # formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# # formated_gdf['size'] = formated_gdf['active'].pow(0.3)
# #
# # fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
# #                      color="active", size='size', hover_name="country",
# #                      range_color= [0, 1000],
# #                      projection="natural earth", animation_frame="date",
# #                      title='COVID-19: Active Cases Over Time', color_continuous_scale="portland")
# # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # formated_gdf = data.groupby(['date', 'country'])['confirmed', 'deaths', 'active', 'recovered'].max()
# # formated_gdf = formated_gdf.reset_index()
# # formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# # formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# # formated_gdf['size'] = formated_gdf['recovered'].pow(0.3)
# #
# # fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
# #                      color="recovered", size='size', hover_name="country",
# #                      range_color= [0, 100],
# #                      projection="natural earth", animation_frame="date",
# #                      title='COVID-19: Recoveries Over Time', color_continuous_scale="greens")
# # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # formated_gdf = data.groupby(['date', 'country'])['confirmed', 'deaths', 'active', 'recovered'].max()
# # formated_gdf = formated_gdf.reset_index()
# # formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# # formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# # formated_gdf['size'] = formated_gdf['confirmed'].pow(0.3) * 5
# #
# # fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
# #                      color="confirmed", size='size', hover_name="country",
# #                      range_color= [0, 5000],
# #                      projection="natural earth", animation_frame="date", scope="europe",
# #                      title='COVID-19: Spread Over Time in EUROPE', color_continuous_scale="portland", height=800)
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# # formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# # formated_gdf['size'] = formated_gdf['deaths'].pow(0.3)
# #
# # fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
# #                      color="deaths", size='size', hover_name="country",
# #                      range_color= [0, 500],
# #                      projection="natural earth", animation_frame="date", scope="europe",
# #                      title='COVID-19: Deaths Over Time in EUROPE', color_continuous_scale="peach", height=800)
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# # formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# # formated_gdf['size'] = formated_gdf['active'].pow(0.3) * 3.5
# #
# # fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
# #                      color="active", size='size', hover_name="country",
# #                      range_color= [0, 3000],
# #                      projection="natural earth", animation_frame="date", scope="europe",
# #                      title='COVID-19: Active Cases Over Time in EUROPE', color_continuous_scale="portland", height=800)
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
# #
# # formated_gdf['date'] = pd.to_datetime(formated_gdf['date'])
# # formated_gdf['date'] = formated_gdf['date'].dt.strftime('%m/%d/%Y')
# # formated_gdf['size'] = formated_gdf['recovered'].pow(0.3) * 3.5
# #
# # fig = px.scatter_geo(formated_gdf, locations="country", locationmode='country names',
# #                      color="recovered", size='size', hover_name="country",
# #                      range_color= [0, 100],
# #                      projection="natural earth", animation_frame="date", scope="europe",
# #                      title='COVID-19: Deaths Over Time in EUROPE', color_continuous_scale="greens", height=800)
# # # fig.update(layout_coloraxis_showscale=False)
# # fig.show()
#
