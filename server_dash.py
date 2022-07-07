import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import json
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

#main settings
caution_threshold = 90
num_of_datapoints = 30
interval_seconds = 2
json_file = 'ListJson.json'

###########################################################
#axis creation - dont edit
#Create initial x axis
x_values = np.arange(1, num_of_datapoints + 1)
#Create initial y axis
with open(json_file) as f:
    y_values = json.load(f)
###########################################################

#viz variables
main_colors = {'background':'#111111', 'text': '#7FDBFF', 'axis': '#FFFFFF', 'title': '#FFFFFF'}
marker_size = 20
marker_symbol = 'circle'
safe_color = 'Green'
caution_color = 'Red'
viz_title = 'CPU Monitoring'
viz_id = 'cpu_monitoring_1'
xaxis_title = 'Time'
yaxis_title = 'CPU'
###########################################################

#dont edit these
marker_color = np.where(np.asarray(y_values) > caution_threshold, caution_color, safe_color)
line_color = np.where(max(y_values) > caution_threshold, caution_color, safe_color)

#Create App
app = dash.Dash(__name__)

#viz1 creation
app.layout = html.Div([dcc.Graph(id=viz_id,
                        figure = {'data':[
                                    go.Scatter(
                                        x=x_values,
                                        y=y_values,
                                        mode='lines+markers',
                                        marker = {
                                            'size':marker_size,
                                            'color': marker_color,
                                            'symbol':marker_symbol,
                                            'line': {'width':2}
                                        },
                                        line= {'color': str(line_color),
                                                'shape': 'spline',
                                                'smoothing': 1}
                                    )], 
                                    'layout':go.Layout(title=viz_title,
                                                title_font_color = main_colors['title'],
                                                paper_bgcolor = main_colors['background'],
                                                plot_bgcolor = main_colors['background'],
                                                xaxis={'title': xaxis_title, 'color': main_colors['axis']},
                                                yaxis={'title': yaxis_title, 'color': main_colors['axis']})}
                                                            

                        ),
                        dcc.Interval(id='interval_component',
                                    interval=interval_seconds * 1000,
                                    n_intervals=0
                        )                          
                    ])

@app.callback(
    Output(viz_id, 'figure'),
    Input('interval_component', 'n_intervals'))
def update_table(n_intervals):

    x_values = np.arange(1, num_of_datapoints + 1)
    with open(json_file) as f:
        y_values = json.load(f)
    line_color = np.where(max(y_values) > caution_threshold, caution_color, safe_color)
    marker_color = np.where(np.asarray(y_values) > caution_threshold, caution_color, safe_color)

    return {'data':[
                                    go.Scatter(
                                        x=x_values,
                                        y=y_values,
                                        mode='lines+markers',
                                        marker = {
                                            'size':marker_size,
                                            'color': marker_color,
                                            'symbol':marker_symbol,
                                            'line': {'width':2}
                                        },
                                        line= {'color': str(line_color),
                                                'shape': 'spline',
                                                'smoothing': 1}
                                    )], 
                                    'layout':go.Layout(title=viz_title,
                                                title_font_color = main_colors['title'],
                                                paper_bgcolor = main_colors['background'],
                                                plot_bgcolor = main_colors['background'],
                                                xaxis={'title': xaxis_title, 'color': main_colors['axis']},
                                                yaxis={'title': yaxis_title, 'color': main_colors['axis']})}

if __name__ == '__main__':
    app.run_server(debug=True)
