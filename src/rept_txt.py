# Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

def repete_texto(texto, vezes):
    return texto * vezes


texto = input("Digite uma string: ")
vezes = int(input("Digite um número inteiro: "))
resultado = repete_texto(texto, vezes)
print("Texto repetido:", resultado)