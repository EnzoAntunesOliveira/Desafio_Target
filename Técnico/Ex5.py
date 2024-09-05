#5)  Inverta os caracteres de um string.

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

while True:
    texto = input("Informe uma string (mínimo 2 caracteres): ")
    if len(texto) < 2:
        print("Erro: a string deve conter no mínimo 2 caracteres. Tente novamente.")
    else:
        resultado = inverter_string(texto)
        print(f"String invertida: {resultado}")
        break
