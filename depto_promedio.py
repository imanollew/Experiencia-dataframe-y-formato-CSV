
#Calcular el valor medio de los deptos 2 ambientes en Capital Federal


from pandas import DataFrame, read_csv
import numpy as np

data = read_csv('properati-AR-2018-02-01-properties-sell.csv')

depCapitalFederal = (data.ix[(data.state_name == 'Capital Federal') & (data.rooms == 2),['price']])
print ('El precio promedio de los departamentos de 2 ambientes es: ', np.mean(depCapitalFederal)[0])
