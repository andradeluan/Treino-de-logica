tempoGasto = int(input())
velocidadeMedia = int(input())
distancia = tempoGasto * velocidadeMedia
combustivelGasto = distancia / 12
print(f'{combustivelGasto:.3f}')