texto = str(input('Digite uma string para ser invertida: ')).strip()

invertida = ''

for i in range(-1, -len(texto)-1, -1):
    invertida += texto[i]

print(f'(Original) {texto.upper()}\t\t(Inversa) {invertida.upper()}')
