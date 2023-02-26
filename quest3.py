import json

with open('faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)

menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

dias_no_mes = len(faturamento_diario)
faturamento_total = sum(faturamento_diario)
media_mensal = faturamento_total / dias_no_mes

superior à média mensal
dias_acima_da_media = 0
for valor in faturamento_diario:
    if valor > media_mensal:
        dias_acima_da_media += 1

print(f"Menor valor de faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento diário acima da média mensal: {dias_acima_da_media}")