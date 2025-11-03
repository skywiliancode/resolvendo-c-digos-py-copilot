# Descrição: Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def soma_numeros(num1, num2):
    return num1 + num2

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
resultado = soma_numeros(numero1, numero2)
print("A soma dos números é:", resultado)