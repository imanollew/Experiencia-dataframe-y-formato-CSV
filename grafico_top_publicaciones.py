
# Hacer un gráfico de barras horizontal de los 10 barrios 
#  con mayor cantidad de publicaciones de deptos. de 2 ambientes
#  en Capital Federal

from matplotlib import pyplot as plt
from pandas import DataFrame, read_csv
import numpy as np

data = read_csv('properati-AR-2018-02-01-properties-sell.csv')

barrios = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms == 2),['place_name']])

print(type(barrios))

top10_barrios = barrios.groupby('place_name').size().sort_values(ascending=False).head(10)

print(top10_barrios[0:])

top10_barrios.plot.barh(align = 'center', color = 'r')
plt.ylabel('Barrio')
plt.xlabel('Cantidad 2 ambientes')
plt.title('10 barrios con mayor Dep. 2 ambientes')
plt.show()
