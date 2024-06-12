def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = 5

print(f'El factorial del {numero} es: {factorial(numero)}')