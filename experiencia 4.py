
#  Para aquellas propiedades de Capital Federal que tengan información geográfica se pide escribir un programa para hacer
#  un scatterplot de las propiedades que difieran a lo sumo en 0.05 grados en latitud y longitud respecto al centro geográfico de
#  la ciudad. Obs.: obtener las coordenadas del centro de la ciudad de modo aproximado con googlemaps).
#***********************************************************
from matplotlib import pyplot as plt
from pandas import DataFrame, read_csv
import numpy as np
import pandas as pd

data = read_csv('properati-AR-2018-02-01-properties-sell.csv')
coordLat=-34.6170222  
coordLong=-58.4451252 
margen=0.05 

filtro = (data.ix[(data.state_name == 'Capital Federal') & (data.lat >= (coordLat-margen)) & (data.lat <= (coordLat+margen)) & (data.lon >= (coordLong-margen)) & (data.lon <= (coordLong+margen)),['lat','lon']])

filtro.plot.scatter(x='lat',y='lon', color='g')
plt.show()