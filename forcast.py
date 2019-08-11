import pandas as pd


data_xls = pd.read_excel('Data Scientists Data for Forecast.xlsx')

data_xls.to_csv('SoEagle_data.csv', encoding = 'utf-8', index = False)

data = pd.read_csv('SoEagle_data.csv')

#print(data)
print(data.head())
print(data.dtypes)