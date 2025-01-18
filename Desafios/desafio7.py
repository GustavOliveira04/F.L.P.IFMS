def movimentos_para_balancear_pilhas(pilhas):
    # Calcular o total de blocos e a altura média das pilhas
    total_blocos = sum(pilhas)
    n = len(pilhas)
    altura_media = total_blocos // n
    
    # Contabilizar os movimentos necessários (movimentos = blocos excedentes)
    movimentos = 0
    for pilha in pilhas:
        if pilha > altura_media:
            movimentos += pilha - altura_media
    
    return movimentos

def main():
    conjunto_num = 1
    while True:
        n = int(input())  # Número de pilhas
        if n == 0:
            break  # Se n for 0, termina a execução
        
        pilhas = list(map(int, input().split()))  # Leitura das alturas das pilhas
        
        # Calcular e imprimir os resultados
        movimentos = movimentos_para_balancear_pilhas(pilhas)
        print(f"Conjunto {conjunto_num}:")
        print(f"The minimum number of moves is {movimentos}.")
        print()  # Linha em branco após cada conjunto
        
        conjunto_num += 1

# Chama a função principal
main()
