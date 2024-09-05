#3) Calcule o menor faturamento, o maior faturamento, a média de faturamento diário e quantos dias tiveram faturamento acima da média.

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('dados/dados.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

valores_validos = [dado['valor'] for dado in dados if dado['valor'] > 0]

menor_valor = min(valores_validos)
maior_valor = max(valores_validos)

media_mensal = sum(valores_validos) / len(valores_validos)

dias_acima_media = len([valor for valor in valores_validos if valor > media_mensal])

print(f"Menor faturamento: {menor_valor:.2f}")
print(f"Maior faturamento: {maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")