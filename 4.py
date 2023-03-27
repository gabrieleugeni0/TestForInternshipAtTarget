faturamento = {
    'sp': 67836.34,
    'rj': 36678.66,
    'mg': 29229.88,
    'es': 27165.48,
    'outros': 19849.53,
}

total = 0
for valor in faturamento.values():
    total += valor

for key, value in faturamento.items():
    print(f'Estado: {key.upper()}\tFaturamento: {value}\tRepresentacao: {(value/total)*100:.2f}')
