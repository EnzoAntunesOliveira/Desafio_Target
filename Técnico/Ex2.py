#2) Verificação de Número na Sequência de Fibonacci

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

while True:
    try:
        num = int(input("Informe um número: "))
        break 
    except ValueError:
        print("Por favor, insira um número válido.")

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
