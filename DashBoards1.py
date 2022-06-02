import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv('trees.csv')
data.rename(columns={'Girth':'Circun','Height':'Altura'}, inplace=True)
print(data)
plt.scatter(data.Circun,data.Volume)
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Cincunferência')

plt.plot(data.Circun, data.Volume)

plt.show()