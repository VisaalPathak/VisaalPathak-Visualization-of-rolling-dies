import matplotlib.pyplot as plt
from rollingdie import Rolldie

Die = Rolldie()
results = [Die.roll() for rolls in range(1000)]
frequencies =[results.count(value) for value in range(1,Die.sides + 1)]
xvalues = range(1, Die.sides + 1)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.bar(xvalues, frequencies)
ax.set_title("Barplot of a single die rolled 1000 time", fontsize = 18)
ax.set_xlabel("Sides", fontsize = 15)
ax.set_ylabel("Frequencies of each sides", fontsize = 15)
ax.tick_params(axis='both', labelsize = 15)
plt.show()