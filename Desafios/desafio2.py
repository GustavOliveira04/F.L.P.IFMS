def quantas_filas(n):
    filas = 0
    guerreiros = 0

    while guerreiros <= n:
        filas += 1
        guerreiros += filas

    return filas - 1

teste = int(input("Quantos testes deseja fazer?"))

for _ in range(teste):
    n = int(input())
    resultado = quantas_filas(n)
    print(resultado)
