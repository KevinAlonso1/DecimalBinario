__author_='Kevin Alonso'

Decimal=998766


def ConvertirDecimalABinario(Decimal):
    Binario = ''
    while Decimal // 2 != 0:
        Binario = str(Decimal % 2) + Binario
        Decimal = Decimal // 2
    return str(Decimal) + Binario


print('Numero: ',Decimal)
print(ConvertirDecimalABinario(Decimal))