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


#correção
# from match import floor, sqrt

# tc = int(input())
# for _ in range(tc):
#     S_n = int(input())
#     # S_n <= n(a_1+a_n)/2
#     # S_n <= N(1+n)/2
#     # n^2 + n - 2S_n <= 0
#     # n <= (-b +- \sqrt{b^2-4ac})/2a
#     # n <= (-1 +- \sqrt{1+8S_n})/2 # como quero numeros
#     # positivos, entao calculo só a raiz positiva
#     i = ( -1 + sqrt(1 + 8 * S_n)) /2
#     print(floor(i)) 