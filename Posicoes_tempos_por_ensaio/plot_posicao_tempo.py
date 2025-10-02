import matplotlib.pyplot as plt
import numpy as np
import os

def ajustar_e_plotar(tempo, posicao, legenda, marcador, cor):
    coef = np.polyfit(tempo, posicao, 2)  # retorna [a, b, c]
    polinomio = np.poly1d(coef)

    t_fit = np.linspace(min(tempo), max(tempo), 200)
    p_fit = polinomio(t_fit)

    # plot dos pontos experimentais
    plt.scatter(tempo, posicao, label=legenda, marker=marcador, edgecolors='black')

    # plot da curva 
    plt.plot(t_fit, p_fit, color=cor, linestyle='--', linewidth=2)


base_path = os.path.dirname(os.path.abspath(__file__))

# pega os dados
dados1 = np.loadtxt(os.path.join(base_path, 'ensaio1_M5.txt'), skiprows=1)
tempo1 = dados1[:, 2]
posicao1 = dados1[:, 0] / 100

dados2 = np.loadtxt(os.path.join(base_path, 'ensaio1_M10.txt'), skiprows=1)
tempo2 = dados2[:, 2]
posicao2 = dados2[:, 0] / 100

dados3 = np.loadtxt(os.path.join(base_path, 'ensaio1_M15.txt'), skiprows=1)
tempo3 = dados3[:, 2]
posicao3 = dados3[:, 0] / 100

dados4 = np.loadtxt(os.path.join(base_path, 'ensaio1_M20.txt'), skiprows=1)
tempo4 = dados4[:, 2]
posicao4 = dados4[:, 0] / 100

dados5 = np.loadtxt(os.path.join(base_path, 'ensaio1_M25.txt'), skiprows=1)
tempo5 = dados5[:, 2]
posicao5 = dados5[:, 0] / 100

dados6 = np.loadtxt(os.path.join(base_path, 'ensaio1_M30.txt'), skiprows=1)
tempo6 = dados6[:, 2]
posicao6 = dados6[:, 0] / 100

# cores para cada experimento
cores = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']

plt.figure(figsize=(10,6))

ajustar_e_plotar(tempo1, posicao1, 'Mt = 228,6 g', 'o', cores[0])
ajustar_e_plotar(tempo2, posicao2, 'Mt = 233,8 g', 's', cores[1])
ajustar_e_plotar(tempo3, posicao3, 'Mt = 239,1 g', '^', cores[2])
ajustar_e_plotar(tempo4, posicao4, 'Mt = 244,4 g', 'D', cores[3])
ajustar_e_plotar(tempo5, posicao5, 'Mt = 249,5 g', 'x', cores[4])
ajustar_e_plotar(tempo6, posicao6, 'Mt = 254,7 g', '*', cores[5])

plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Posição do carrinho ao longo do tempo com ajuste quadrático')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
