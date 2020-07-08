import plotly.graph_objects as go
import plotly.io as pio
import sqlite3

""" Creates a plot showing poker winnings (net winnings per game, buy-in per game, and cumulative net winnings)
    Both renders the plot in the web browser immediately, and writes to an html file. """

pio.renderers.default='browser'
fig = go.Figure()

netLabel = ' - Net'
buyinLabel = ' - Buy-in'
cumulativeLabel = ' - Cumulative'

""" Color set from https://colorbrewer2.org/#type=qualitative&scheme=Set1&n=8 """
colors = ['red',
          'blue',
          'green',
          'black',
          'purple',
          'pink',
          'teal',
          'yellow',
          'orange',
          'magenta',
          'cyan',
          'brown']

conn = sqlite3.connect("c:/Users/greg/databases/PokerHistory.sqlite3")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


cursor.execute("SELECT DISTINCT Date FROM Results")
dateRows = cursor.fetchall()
dates = []
for row in dateRows:
    dates.append(row[0])

print(dates)

cursor.execute("SELECT DISTINCT Name FROM Results")
nameRows = cursor.fetchall()
names = []
for row in nameRows:
    names.append(row[0])

offset = 0
for name in names:
    net = []
    buyin = []
    cumulative = []
    datesPlayed = []
    for date in dates:
        cursor.execute("SELECT * FROM Results WHERE Date=? AND Name=?", (date, name))
        row = cursor.fetchone()
        if row != None:
            net.append(row["Net"])
            buyin.append(-row["BuyIn"])
            cumulative.append(round(sum(filter(None, net)), 2))
            datesPlayed.append(date)




    color = colors[offset]

    print(name)
    print(datesPlayed)
    print(net)
    print(buyin)
    print(cumulative)

    fig.add_trace(go.Bar(x=datesPlayed,
        y=net,
        name=name + netLabel,
        marker_color=color,
        offsetgroup=offset,
        legendgroup=netLabel))
    fig.add_trace(go.Bar(x=datesPlayed,
        y=buyin,
        name=name + buyinLabel,
        marker_color=color,
        offsetgroup=offset,
        opacity=0.15,
        legendgroup=buyinLabel))
    fig.add_trace(go.Line(x=datesPlayed,
        y=cumulative,
        name=name + cumulativeLabel,
        marker_color=color,
        legendgroup=cumulativeLabel,
        ))

    offset += 1

conn.close()

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