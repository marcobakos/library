import pandas as pd
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


# Can open csv files as a dataframe

dframe = pd.read_csv('lotto-draw-history.csv')

# Show
# print(dframe)

arr1 = np.array(dframe)

arr_num = arr1[:, 1:6]  # seleciona parcialmente um array [startline:lastline,startcolumn:lastcolumn]
arr_play = arr1[:,6:7]  # seleciona parcialmente um array - somente os numeros do play

unique_elements, counts_elements = np.unique(arr_num, return_counts=True)

print(unique_elements)
print(counts_elements)


#
# plt.hist(unique_elements, bins=[0, 10, 20, 30, 40, 50, 60])
# acertar essa escala.......
#
#

# plt.title("Histogram - tst")
# plt.show()

x2 = unique_elements
y2 = counts_elements

plt.bar(x2, y2, color='r', align='center')
plt.title('Loto - Bar graph')
plt.ylabel('Y Ocorrencia')
plt.xlabel('X numeros')
plt.show()
