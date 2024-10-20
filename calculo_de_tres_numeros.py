# Solicita ao usuário para digitar três valores reais (números com casas decimais)
A = float(input('Digite um valor real para A: '))
B = float(input('Digite um valor real para B: '))
C = float(input('Digite um valor real para C: '))

# Realiza a soma de A, B e C, e armazena o resultado em R1
R1 = A + B + C
# Exibe o valor de R1 com 3 casas decimais
print(f'R1 = {R1:.3f}')

# Calcula o produto (multiplicação) de A, B e C, e armazena em R2
R2 = A * B * C
# Exibe o valor de R2 com 3 casas decimais
print(f'R2 = {R2:.3f}')

# Calcula o valor da expressão 2 * (A + B) - C e armazena em R3
R3 = 2 * (A + B) - C
# Exibe o valor de R3 com 3 casas decimais
print(f'R3 = {R3:.3f}')

# Calcula a média aritmética de A, B e C, armazenando o valor em R4
R4 = (A + B + C) / 3
# Exibe o valor de R4 com 3 casas decimais
print(f'R4 = {R4:.3f}')

# Calcula a expressão (2 * B + 3 * C) / (5 * A), armazenando em R5
R5 = (2 * B + 3 * C) / (5 * A)
# Exibe o valor de R5 com 3 casas decimais
print(f'R5 = {R5:.3f}')

# Calcula a soma dos quadrados de A e B (A^2 + B^2), armazenando em R6
R6 = A ** 2 + B ** 2
# Exibe o valor de R6 com 3 casas decimais
print(f'R6 = {R6:.3f}')

