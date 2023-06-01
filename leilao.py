lances = int(input())

i = int(0)

nome = []
valor = []
valorNaOrdem = []

ganhador = ''


while (i < lances):
    nomeInput = input()
    valorInput = int(input())
    valorNaOrdemInput = valorInput
    nome.insert(i, nomeInput)
    valor.insert(i, valorInput)
    valorNaOrdem.insert(i, valorNaOrdemInput)
    i = i + 1




valorNaOrdem.sort()
index = valor.index(valorNaOrdem[lances - 1])
ganhador =  nome[index]

print(ganhador)
print(valorNaOrdem[lances - 1])
