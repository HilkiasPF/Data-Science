import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv('trees.csv')
print(data.head())

x = np.histogram(data.iloc[:,1],bins=6)
print(x)
#
# plt.hist(data.iloc[:,1], bins=6)

sb.distplot(data.iloc[:,1],
            hist=True,
            kde=True,
            color='Grey',
            hist_kws={'edgecolor':'black'}) # kde = densidade
plt.xlabel('Altura')
plt.ylabel('Frequência')
plt.title('Árvore')
plt.show()
