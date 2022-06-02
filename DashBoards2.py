import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv('co2.csv')
print(data) #conc = concentração uptake= quanto recebeu

x, y = data.conc, data.uptake

unicos = list(set(data.Treatment)) #refrigerados e não refrigerados

for c in range(len(unicos)):
    indice = data.Treatment == unicos[c]
    plt.scatter(x[indice], y[indice], label=unicos[c])

plt.legend(loc='lower right') #posição da legenda
plt.show()
