__author_='Kevin Alonso'

Decimal=555


def ConvertirDecimalABinario(Decimal):
    Binario = ''
    while Decimal // 2 != 0:
        Binario = str(Decimal % 2) + Binario
        Decimal = Decimal // 2
    return str(Decimal) + Binario

lista=list(ConvertirDecimalABinario(Decimal))
print('Numero: ',Decimal)
print('Binario',lista)
