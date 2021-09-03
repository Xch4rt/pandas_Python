import pandas as pd
import os
pd.set_option('display.width',1000) # para mantener el formato

#Task#1: Agregando los archivos de 12 meses en uno solo

#df = pd.read_csv("./Sales_Data/Sales_April_2019.csv")

# Agrego todos los files csv a la variable files
files = [file for file in os.listdir('./Sales_Data')] 

all_months_data = pd.DataFrame()
# por cada csv se ira agregando al dataframe all_months_data para tener un archivo con todos los datos
'''
for file in files:
    df = pd.read_csv("./Sales_Data/"+file)
    all_months_data = pd.concat([all_months_data, df])
print(all_months_data.head())

all_months_data.to_csv('all_data.csv') #guardandolo como archivo csv
'''

all_data = pd.read_csv("all_data.csv")
#print(all_data.head())

#Task#2: Agregando columna de meses

#Q1: What was the best month for sales? How much was earned that month?

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
print(all_data.head())

