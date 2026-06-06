import numpy as np
import matplotlib.pyplot as plt
from funcoes import cabecalho, linha, pausar


# PARTE DE CÁLCULO — MODELAGEM MATEMÁTICA DO IRO


def calc_risco_q(T):
    r = 0.05 * T**2 - 0.5 * T + 5
    if r < 0: r = 0
    if r > 100: r = 100
    return r

def calc_risco_u(U):
    r = 100 - 28 * np.log(U + 1)
    return max(0, min(r, 100))

def iro_analitico(T, U):
    return (calc_risco_q(T) + calc_risco_u(U)) / 2


def analisar_funcoes():
    cabecalho("ANÁLISE DO MODELO DE RISCO (IRO)")

    T_vals = np.linspace(0, 60, 1000)
    R_q = np.array([calc_risco_q(t) for t in T_vals])

    T_v = 5.0
    R_v = calc_risco_q(T_v)

    linha()
    print("\n FUNÇÃO: queimada")
    linha()
    print(f" Temp minima da curva: {T_v}°C")
    print(f" Risco minimo: {R_v:.2f}")
    print(f" Faixa: {R_q.min():.1f} até {R_q.max():.1f}")

    for i, r in enumerate(R_q):
        if r >= 60:
            print(f" Risco alto a partir de ~{T_vals[i]:.1f}°C")
            break

    U_vals = np.linspace(0, 100, 1000)
    R_e = np.array([calc_risco_u(u) for u in U_vals])

    linha()
    print("\n FUNÇÃO: enchente")
    linha()
    print(f" Faixa: {R_e.min():.1f} até {R_e.max():.1f}")

    for i, r in enumerate(R_e):
        if r <= 30:
            print(f" Mais seguro acima de ~{U_vals[i]:.1f}% umidade")
            break

    linha()
    pausar()


def gerar_graficos():
    cabecalho("GRÁFICOS")

    T = np.linspace(0, 60, 500)
    U = np.linspace(0, 100, 500)
    R_q = np.array([calc_risco_q(t) for t in T])
    R_u = np.array([calc_risco_u(u) for u in U])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("IRO - Risco Ambiental")

    # grafico queimada
    ax1.axhspan(0, 30, alpha=0.2, color="green")
    ax1.axhspan(30, 60, alpha=0.2, color="yellow")
    ax1.axhspan(60, 100, alpha=0.2, color="red")
    ax1.plot(T, R_q)
    ax1.set_title("Queimada x Temperatura")
    ax1.set_xlabel("Temperatura (°C)")
    ax1.set_ylabel("Risco")
    ax1.set_ylim(0, 100)
    ax1.grid(True)

    # grafico enchente
    ax2.axhspan(0, 30, alpha=0.2, color="green")
    ax2.axhspan(30, 60, alpha=0.2, color="yellow")
    ax2.axhspan(60, 100, alpha=0.2, color="red")
    ax2.plot(U, R_u)
    ax2.set_title("Enchente x Umidade")
    ax2.set_xlabel("Umidade (%)")
    ax2.set_ylabel("Risco")
    ax2.set_ylim(0, 100)
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig("graficos_iro.png")
    print("salvo")
    plt.show()
    pausar()