
#6º Observe os espaços sublinhados e complete o código.

import matplotlib.pyplot as plt  # 1º espaço: matplotlib
import numpy as np               # 2º espaço: np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")

for row in range(2):             # 3º espaço: row
    for col in range(2):         # 4º espaço: col
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5), 
                             transform=axs[row, col].transAxes,
                             ha='center', va='center', fontsize=18,  # 5º espaço: fontsize
                             color='darkgrey')
fig.suptitle('plt.subplots()')   # 6º espaço: plt
plt.show()