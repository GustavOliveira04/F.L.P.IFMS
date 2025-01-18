# Lista permitida. Ler um número nn, seguido por nn palavras "permitidas". Depois, ler um número mm, seguido por m frases, 
# uma em cada linha. Para cada frase, escrever "PERMITIDO" ou "CENSURADO" caso contenha apenas palavras permitidas ou não.

n = int(input('quantas palavras proibidas?'))
print('digite cada palavra proibida em um linha')
proibidas = set()
for _ in range(n):
    proibidas.add(input())
m = int(input('quantas frases a filtrar?'))
print('digite cada frase em uma linha')
for _ in range(m):
    frase = input()
    permitido = True
    for palavra in frase.split():
        if palavra in proibidas:
            permitido = False
            break
    print("PERMITIDO" if permitido else "CENSURADO")