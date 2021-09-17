from plotly.graph_objects import Bar, Layout
from plotly import offline
from rollingdie import Rolldie

Die = Rolldie()
results = [Die.roll() for rolls in range(1000)]
frequencies =[results.count(value) for value in range(1,Die.sides + 1)]

#print(results)
#print(frequencies)
#Visualization
x_values = list(range(1, Die.sides + 1))
data = [Bar(x = x_values, y = frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = "Results of rolling D6 dies 1000 times", xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename = 'd6.html' )