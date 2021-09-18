import matplotlib.pyplot as plt
from rollingdie import Rolldie

Die1 = Rolldie()
Die2 = Rolldie()
results = [Die1.roll() + Die2.roll() for rolls in range(1000)]
max_result = Die1.sides + Die2.sides
frequencies =[results.count(value) for value in range(2,max_result + 1)]
x_values = list(range(2, max_result + 1))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.bar(x_values, frequencies)
ax.set_title("Barplot of a two D6 dies rolled 1000 time", fontsize = 18)
ax.set_xlabel("Outcome", fontsize = 15)
ax.set_ylabel("Frequencies of each outcome", fontsize = 15)
ax.set_xticks(x_values)
ax.tick_params(axis='both', labelsize = 15, )
plt.show()