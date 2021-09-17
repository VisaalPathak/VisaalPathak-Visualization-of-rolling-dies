from plotly.graph_objects import Bar, Layout
from plotly import offline
from rollingdie import Rolldie

Die1 = Rolldie()
Die2 = Rolldie()
results = [Die1.roll() + Die2.roll() for rolls in range(1000)]
max_result = Die1.sides + Die2.sides
frequencies =[results.count(value) for value in range(2,max_result + 1)]

#print(results)
#print(frequencies)
#Visualization
x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = "Results of rolling two D6 dies 1000 times", xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout':my_layout}, filename = 'd6_d6.html' )