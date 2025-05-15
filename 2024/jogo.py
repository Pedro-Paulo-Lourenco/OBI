"""
• se uma célula morta possui exatamente três vizinhas vivas, ela vira uma célula viva;
• se uma célula morta possui uma quantidade de vizinhas vivas diferente de três, ela continua morta;
• se uma célula viva possui duas ou três vizinhas vivas, ela continua viva;
• se uma célula viva possui menos que duas vizinhas vivas, ela morre;
• se uma célula viva possui mais que três vizinhas vivas, ela morre.
"""
from copy import deepcopy

tamanho, fases = [int(n) for n in input().split(" ")]
estado_jogo = []
for j in range(tamanho):
    estado_jogo.append([int(i) for i in input()])
novo_estado = deepcopy(estado_jogo)

for geracao in range(fases):
    for linha in range(tamanho):
        for coluna in range(tamanho):
            celula = estado_jogo[linha][coluna]
            vizinhos = 0
            for mod_vizinha in [-1, 0, 1]:
                linha_vizinha = linha + mod_vizinha
                for mod_coluna in [-1, 0, 1]:
                    coluna_vizinha = coluna + mod_coluna
                    if not(0 <= coluna_vizinha < tamanho and 0 <= linha_vizinha < tamanho):
                        continue
                    elif linha_vizinha == linha and coluna_vizinha == coluna:
                        continue

                    vizinhos += estado_jogo[linha_vizinha][coluna_vizinha]

            if celula == 0 and vizinhos == 3:
                    novo_estado[linha][coluna] = 1
            elif celula ==1 and not vizinhos in [2, 3]:
                    novo_estado[linha][coluna] = 0
            #print(vizinhos)
    estado_jogo = deepcopy(novo_estado)
print()
for a in estado_jogo:
    for b in a:
        print(b, end="")
    print()
print(estado_jogo)
