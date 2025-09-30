import numpy as np

# pega os dados do arquivo .txt
dados = np.loadtxt('ensaio1_M30.txt', skiprows=1)

# Colunas
x = dados[:, 2]           # T (s)
y = dados[:, 0]           # X (cm)
sigma_y = dados[:, 1]     # σx (cm)
pesos = 1 / sigma_y       # pesos para ajuste ponderado

# Centraliza x
x_central = x - np.mean(x)

# Ajuste ponderado com covariância
p, cov = np.polyfit(x_central, y, 2, w=pesos, cov=True)

# Coeficientes
a, b, c = p
sigma_a = np.sqrt(cov[0, 0])

print(f"a = {a:.4f} ± {sigma_a:.4f} \n")
