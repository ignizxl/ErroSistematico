import random

lista = random.sample(range(100), k=6)
arquivo = open("dados.txt", "a")
i = 0
while i < 101:
    lista = random.sample(range(100), k=6)
    arquivo.write(
        str(lista[0])
        + " "
        + str(lista[1])
        + " "
        + str(lista[2])
        + " "
        + str(lista[3])
        + " "
        + str(lista[4])
        + " "
        + str(lista[5])
        + ";\n"
    )
    i += 1
