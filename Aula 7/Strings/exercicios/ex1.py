# Receber uma string. Retorná-la de trás para frente.

def inverter_string(string):
    return string[::-1]

entrada = input("Digite uma frase: ")
resultado = inverter_string(entrada)

print("String invertida:", resultado) 
