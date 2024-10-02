import random

def sorte():
    numSorteados = []
    for x in range(15):
        x = random.randint(1,25)
        numSorteados.append(x)
    numSorteados.sort()
    print (numSorteados)
sorte()