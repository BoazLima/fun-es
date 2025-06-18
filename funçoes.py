# 1. Mostra uma mensagem de boas-vindas
def boas_vindas():
    print("Bem-vindo(a) disciplina ALLP")

# Exemplo de uso:
boas_vindas()


# 2. Retorna o quadrado de um número
def quadrado(numero):
    return numero * numero

# Exemplo de uso:
print(quadrado(4))  # Saída: 16


# 3. Soma dois números e retorna o resultado
def somar(a, b):
    return a + b

# Exemplo de uso:
print(somar(3, 5))  # Saída: 8


# 4. Mostra uma contagem do início até o fim
def contagem(inicio=1, fim=5):
    for i in range(inicio, fim + 1):
        print(i)

# Exemplo de uso:
contagem()         # Contagem de 1 a 5
contagem(3, 7)     # Contagem de 3 a 7


# 5. Calcula e retorna o IMC
def calcula_imc(peso=70, altura=1.75):
    return peso / (altura * altura)

# Exemplo de uso:
print(calcula_imc())           # Saída: 22.86 (aproximadamente)
print(calcula_imc(80, 1.80))   # Saída: 24.69 (aproximadamente)


# 6. Diz se o número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

# Exemplo de uso:
par_ou_impar(10)  # Saída: Par
par_ou_impar(7)   # Saída: Ímpar


# 7. Mostra uma saudação com o nome
def saudacao(nome="Visitante"):
    print("Olá,", nome)

# Exemplo de uso:
saudacao()           # Saída: Olá, Visitante
saudacao("Carlos")   # Saída: Olá, Carlos
