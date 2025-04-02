
# 7º  Observe os espaços sublinhados e complete o código.

import numpy as np
import matplotlib as mpl          # 1º espaço: matplotlib
import matplotlib.pyplot as plt  # 2º espaço: matplotlib.pyplot

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # 3º espaço: linspace
y = np.sin(x)                    # 4º espaço: sin

fig, ax = plt.subplots()         # 5º espaço: fig, ax
ax.plot(x, y)                    # 6º espaço: plot(x, y)
plt.show()