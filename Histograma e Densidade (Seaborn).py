import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv('chicken.csv')

data.rename(columns={'weight': 'Peso', 'feed': 'Ração'}, inplace=True)
print(data.head())

group= data.groupby(['Ração'])['Peso'].sum()

horsebean = data.loc[data['Ração']=='horsebean'] #dataframe só com horsebean


plt.figure()
plt.subplot(3,2,1)
sb.distplot(data.loc[data['Ração']=='horsebean'].Peso, kde=True).set(title='Horsebean') #Ctrl + D (Copia a linha)
plt.subplot(3,2,2)
sb.distplot(data.loc[data['Ração']=='casein'].Peso).set(title='Casein')
plt.subplot(3,2,3)
sb.distplot(data.loc[data['Ração']=='linseed'].Peso).set(title='Linseed')
plt.subplot(3,2,4)
sb.distplot(data.loc[data['Ração']=='meatmeal'].Peso).set(title='meatmeal')
plt.subplot(3,2,5)
sb.distplot(data.loc[data['Ração']=='soybean'].Peso).set(title='Soybean')
plt.subplot(3,2,6)
sb.distplot(data.loc[data['Ração']=='sunflower'].Peso).set(title='Sunflower')
plt.tight_layout() #ajusta para não ter sobreposição
plt.show()