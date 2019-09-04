#Hacer un gráfico de barras por cantidad de ambientes en Capital Federal quitando los outliers

from matplotlib import pyplot as plt
from pandas import DataFrame, read_csv
import numpy as np

data = read_csv('properati-AR-2018-02-01-properties-sell.csv')

depCapitalFederal = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms >0),['rooms']])
group_room = depCapitalFederal.groupby('rooms').size()[1:8]

print(type(group_room))

group_room.plot.bar()
plt.ylabel("cantidad de ocurrencias")
plt.title("Ambientes")
plt.show()

