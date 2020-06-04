import plotly.graph_objects as go
import plotly.io as pio

""" Creates a plot showing poker winnings (net winnings per game, buy-in per game, and cumulative net winnings)
    Both renders the plot in the web browser immediately, and writes to an html file. """

pio.renderers.default='browser'
fig = go.Figure()

net = ' - Net'
buyin = ' - Buy-in'
cumulative = ' - Cumulative'

""" Color set from https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=8 """

greg_color = 'rgb(228,26,28)'
greg = 'Greg'
greg_offset = 0

bill_color = 'rgb(55, 126, 184)'
bill = 'Bill'
bill_offset = 1

hall_color = 'rgb(77, 175, 74)'
hall = "Hall"
hall_offset = 2

sean_color = 'rgb(106, 61, 154)'
sean = "Sean"
sean_offset = 3

gummel_color = 'rgb(152, 78, 163)'
gummel = "Gummel"
gummel_offset = 4

mantione_color = 'rgb(255, 127, 0)'
mantione = "Mantione"
mantione_offset = 5

jann_color = 'rgb(255, 255, 51)'
jann = "Jann"
jann_offset = 6

figaniak_color = 'rgb(166, 86, 40)'
figaniak = "Fig"
figaniak_offset = 7

sykes_color = 'rgb(106, 61, 154)'
sykes = "Sykes"
sykes_offset = 8

mcgilloway_color = 'rgb(247, 129, 191)'
mcgilloway = "Mcgilloway"
mcgilloway_offset = 9

dates = [
    "4/1/2020" ,
    "4/8/2020",
    "4/15/2020",
    "4/22/2020",
    "4/29/2020",
    "5/6/2020",
    "5/13/2020",
    "5/20/2020",
    "5/27/2020",
    "6/3/2020"]

""" Net Winnings """
fig.add_trace(go.Bar(x=dates,
                y=[-20.00, 70.00, -20.00, -10.91, 88.90, 22.40, -2.30, 32.60, 24.88, 42.31],
                name=greg + net,
                marker_color=greg_color,
                offsetgroup=greg_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[20.00, 0, 0, 20.75, -40.00, 0, -9.94, 0, -37.16, 0],
                name=bill + net,
                marker_color=bill_color,
                offsetgroup=bill_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[104, -20, -60, 20.05, -36, 11.40, 3.69, 5.92, -23.54, -7.72],
                name=hall + net,
                marker_color=hall_color,
                offsetgroup=hall_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, -30, 120, 9.81, -15.3, 6.2, -5.19, -20, 0, -3.46],
                name=gummel + net,
                marker_color=gummel_color,
                offsetgroup=gummel_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, 0, -20, -36.56, -14.60, 0, 13.74, -18.52, 0, 1.71],
                name=jann + net,
                marker_color=jann_color,
                offsetgroup=jann_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, -20, -20, 4.18, 17, -40, 0, 0, 0, -20],
                name=mantione + net,
                marker_color=mantione_color,
                offsetgroup=mantione_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-4, 0, 0, 0, 0, 0, 0, 0, 0, -20],
                name=figaniak + net,
                marker_color=figaniak_color,
                offsetgroup=figaniak_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[0, 0, 0, -7.32, 0, 0, 0, 0, 0, 0],
                name=mcgilloway + net,
                marker_color=mcgilloway_color,
                offsetgroup=mcgilloway_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[0, 0, 0, 0, 0, 0, 0, 0, 35.82, 0],
                name=sean + net,
                marker_color=sean_color,
                offsetgroup=sean_offset,
                legendgroup=net
                ))
fig.add_trace(go.Bar(x=dates,
                y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 7.16],
                name=sykes + net,
                marker_color=sykes_color,
                offsetgroup=sykes_offset,
                legendgroup=net
                ))

""" Buy-ins """
opacity = 0.15
fig.add_trace(go.Bar(x=dates,
                y=[-20, -20, -20, -80, -20, -20, -20, -20, -20, -20],
                name=greg + buyin,
                marker_color=greg_color,
                opacity=opacity,
                offsetgroup=greg_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, 0, -20, -20, -40, 0, -20, 0, -60, 0],
                name=bill + buyin,
                marker_color=bill_color,
                opacity=opacity,
                offsetgroup=bill_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, -20, -60, -20, -40, -20, -20, -20, -40, -40],
                name=hall + buyin,
                marker_color=hall_color,
                opacity=opacity,
                offsetgroup=hall_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, -30, -20, -20, -40, -20, -20, -20, 0, -40],
                name=gummel + buyin,
                marker_color=gummel_color,
                opacity=opacity,
                offsetgroup=gummel_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, 0, -20, -40, -20, 0, -20, -40, 0, -20],
                name=jann + buyin,
                marker_color=jann_color,
                opacity=opacity,
                offsetgroup=jann_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, -20, -20, -20, -20, -40, 0, 0, 0, -20],
                name=mantione + buyin,
                marker_color=mantione_color,
                opacity=opacity,
                offsetgroup=mantione_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[-20, 0, 0, 0, 0, 0, 0, 0, 0, -20],
                name=figaniak + buyin,
                marker_color=figaniak_color,
                opacity=opacity,
                offsetgroup=figaniak_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[0, 0, 0, -20, 0, 0, 0, 0, 0, 0],
                name=mcgilloway + buyin,
                marker_color=mcgilloway_color,
                opacity=opacity,
                offsetgroup=mcgilloway_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[0, 0, 0, 0, 0, 0, 0, 0, -20, 0],
                name=sean + buyin,
                marker_color=sean_color,
                opacity=opacity,
                offsetgroup=sean_offset,
                legendgroup=buyin,
                ))
fig.add_trace(go.Bar(x=dates,
                y=[0, 0, 0, 0, 0, 0, 0, 0, 0, -40],
                name=sykes + buyin,
                marker_color=sykes_color,
                opacity=opacity,
                offsetgroup=sykes_offset,
                legendgroup=buyin,
                ))

""" Cumulative Winnings """
fig.add_trace(go.Line(x=dates,
                y=[-20.00, 50.00, 30.00, 19.09, 107.99, 130.39, 128.09, 160.69, 185.57, 227.88],
                name=greg + cumulative,
                marker_color=greg_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[-20, -20, -20, 0.75, -39.25, -39.25, -49.19, -49.19, -86.35, -86.35],
                name=bill + cumulative,
                marker_color=bill_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[104, 84, 24, 44.05, 8.05, 19.45, 23.14, 29.06, 5.52, -2.20],
                name=hall + cumulative,
                marker_color=hall_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[-20, -50, 70, 79.81, 64.51, 70.71, 65.52, 45.52, 45.52, 42.06],
                name=gummel + cumulative,
                marker_color=gummel_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[-20, -20, -40, -76.56, -91.16, -91.16, -77.42, -95.94, -95.94, -94.23],
                name=jann + cumulative,
                marker_color=jann_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[-20, -40, -60, -55.82, -38.82, -78.82, -78.82, -78.82, -78.82, -98.82],
                name=mantione + cumulative,
                marker_color=mantione_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[-4,-4,-4,-4,-4,-4,-4,-4, -4, -24],
                name=figaniak + cumulative,
                marker_color=figaniak_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[0, 0, 0, -7.32, -7.32, -7.32, -7.32, -7.32, -7.32, -7.32],
                name=mcgilloway + cumulative,
                marker_color=mcgilloway_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[0, 0, 0, 0, 0, 0, 0, 0, 35.82, 35.82],
                name=sean + cumulative,
                marker_color=sean_color,
                legendgroup=cumulative,
                ))
fig.add_trace(go.Line(x=dates,
                y=[0, 0, 0, 0, 0, 0, 0, 0, 0, 7.16],
                name=sykes + cumulative,
                marker_color=sykes_color,
                legendgroup=cumulative,
                ))


fig.update_layout(
    title='Poker',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Dollars',
        titlefont_size=16,
        tickfont_size=14,
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()

fig.write_html("./poker_plot.html")