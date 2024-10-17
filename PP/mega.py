import random
from itertools import combinations

def sortear_numeros_unicos(numeros_a_sortear, intervalo):
    numeros_sorteados = random.sample(range(1, intervalo + 1), numeros_a_sortear)
    return sorted(numeros_sorteados)

def calcular_probabilidade_acerto():
    # Definir parâmetros
    total_numeros = 60
    numeros_a_acertar = 6

    # Sorteio de 6 números únicos no intervalo de 1 a 60
    numeros_sorteados = sortear_numeros_unicos(numeros_a_acertar, total_numeros)

    # Calcular o número total de combinações possíveis
    total_combinacoes = len(list(combinations(range(1, total_numeros + 1), numeros_a_acertar)))

    # Calcular o número de combinações que resultam nos números sorteados
    combinacoes_corretas = len(list(combinations(numeros_sorteados, numeros_a_acertar)))

    # Calcular a probabilidade
    probabilidade = combinacoes_corretas / total_combinacoes

    # Exibir resultados
    print(f"Números sorteados: {numeros_sorteados}")
    print(f"Probabilidade de acertar exatamente 6 números: {probabilidade:.10f}")

# Chamar a função para calcular a probabilidade de acerto
calcular_probabilidade_acerto()
