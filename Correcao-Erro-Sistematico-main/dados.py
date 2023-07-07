import matplotlib.pyplot as plt
import numpy as np
import sig

plt.style.use("_mpl-gallery")

def leitura(nome):
    arquivo  = open(nome, "r")
    esquerda = []
    direita  = []
    cont     = 0
    for i in arquivo:
        cont += 1
        linha = i.replace("\n", "").replace(";", "")
        linha = linha.split(" ")
        auxE, auxD = [], []
        auxE.append(float(linha[0]))
        auxE.append(float(linha[1]))
        auxE.append(float(linha[2]))
        auxD.append(float(linha[3]))
        auxD.append(float(linha[4]))
        auxD.append(float(linha[5]))
        esquerda.append(auxE)
        direita.append(auxD)

    return (esquerda, direita)

def media(lista):
    r, g, b, cont = 0, 0, 0, 0
    for linha in lista:
        cont += 1
        r += linha[0]
        g += linha[1]
        b += linha[2]
    return (r / cont, g / cont, b / cont)

def separacao():
    lista = [
        "branco.sce",
        "cinza.sce",
        "verde.sce",
        "creme.sce",
        "preto.sce",
        "vermelho.sce",
        "amarelo.sce",
        "azul.sce",
    ]
    vermelhoE, verdeE, azulE = [], [], []
    vermelhoD, verdeD, azulD = [], [], []

    for i in range(len(lista)):
        vermelhoE.append(media(leitura(lista[i])[0])[0])
        verdeE.append(media(leitura(lista[i])[0])[1])
        azulE.append(media(leitura(lista[i])[0])[2])
        vermelhoD.append(media(leitura(lista[i])[1])[0])
        verdeD.append(media(leitura(lista[i])[1])[1])
        azulD.append(media(leitura(lista[i])[1])[2])
    return vermelhoE, verdeE, azulE, vermelhoD, verdeD, azulD

def Z(y, x, teta):
    z1 = np.zeros(y.shape[0])

    for i in range(y.shape[0]):
        z1[i] = y[i] - (teta[0] * x[i] + teta[1])

    return z1

def J(x, teta):
    J1 = np.zeros((x.shape[0], teta.shape[0]))

    for i in range(x.shape[0]):
        J1[i, :] = [-x[i], -1]

    return J1

def GaussNewtonI(Y, X, valorInicial, n):
    estado = valorInicial.copy()

    for i in range(n):
        Z1 = Z(Y, X, estado)
        J1 = J(X, estado)
        incremento = -np.linalg.inv(J1.T @ J1) @ J1.T @ Z1
        estado = estado + incremento

    return estado

def grafico():
    vermelhoE, verdeE, azulE, vermelhoD, verdeD, azulD = separacao()
    valorInicial = np.array([1, 0])
    # define os dados para a correcao
    estadoVermelho = GaussNewtonI((np.array(vermelhoD) - np.array(vermelhoE)),np.array(vermelhoE),valorInicial, 100,)
    estadoVerde = GaussNewtonI((np.array(verdeD) - np.array(verdeE)), np.array(verdeE), valorInicial, 100)
    estadoAzul = GaussNewtonI((np.array(azulD) - np.array(azulE)), np.array(azulD), valorInicial, 100)
    # intancia o grafico
    fig, axs = plt.subplots(3, 3, figsize=(8, 10))
    for i in range(len(vermelhoE)):
        # grafico errado
        axs[0][0].scatter(vermelhoE[i], vermelhoE[i], c="red")
        axs[0][0].scatter(vermelhoE[i], vermelhoD[i], facecolor="white", edgecolors="red")
        axs[1][0].scatter(verdeE[i], verdeE[i], c="green")
        axs[1][0].scatter(verdeE[i], verdeD[i], facecolor="white", edgecolors="green")
        axs[2][0].scatter(azulE[i], azulE[i], c="blue")
        axs[2][0].scatter(azulE[i], azulD[i], facecolor="white", edgecolors="blue")

        # gráfico corrigido
        axs[0][1].scatter(vermelhoE[i], vermelhoE[i], c="red")
        axs[0][1].scatter(vermelhoE[i],vermelhoD[i] - (estadoVermelho[0] * vermelhoD[i] + estadoVermelho[1]),facecolor="white", edgecolors="red",
        )
        axs[1][1].scatter(verdeE[i], verdeE[i], c="green")
        axs[1][1].scatter(verdeE[i], verdeD[i] - (estadoVerde[0] * verdeD[i] + estadoVerde[1]),facecolor="white",edgecolors="green",        )
        axs[2][1].scatter(azulE[i], azulE[i], c="blue")
        axs[2][1].scatter(azulE[i],azulD[i] - (estadoAzul[0] * azulD[i] + estadoAzul[1]),facecolor="white", edgecolors="blue",)
        # Coeficientes da linha linear
        m = 1  # inclinação
        b = 0  # intercepto

        # gráfico linear
        x_line = np.linspace(min(vermelhoE), max(vermelhoE), 100)
        y_line = m * x_line + b
        axs[0][2].plot(x_line, y_line, color="red", label="Linha Linear")
        axs[0][2].scatter(vermelhoE[i],vermelhoD[i] - (estadoVermelho[0] * vermelhoD[i] + estadoVermelho[1]),facecolor="white",edgecolors="red",)
        
        x_line = np.linspace(min(verdeE), max(verdeE), 100)
        y_line = m * x_line + b

        axs[1][2].plot(x_line, y_line, color="green", label="Linha Linear")
        axs[1][2].scatter(verdeE[i],verdeD[i] - (estadoVerde[0] * verdeD[i] + estadoVerde[1]),facecolor="white",edgecolors="green",)
        
        x_line = np.linspace(min(azulE), max(azulE), 100)
        y_line = m * x_line + b

        axs[2][2].plot(x_line, y_line, color="blue", label="Linha Linear")
        axs[2][2].scatter(azulE[i],azulD[i] - (estadoAzul[0] * azulD[i] + estadoAzul[1]),facecolor="white",edgecolors="blue",)
        plt.tight_layout()
    plt.show()

grafico()
