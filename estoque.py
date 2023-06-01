tipos, tamanhos = input().split()

tipos = int(tipos)
tamanhos = int(tamanhos)

vendas = int(0)

i = int(0)

estoque = []

while (i < tipos):
    coluna = input().split()

    j = int(0)
    while (j < tamanhos):
        coluna[j] = int(coluna[j])
        j += 1

    estoque.insert(i, coluna)
    i += 1

pedidos = int(input())

j = 0

while (j < pedidos):
    positionI, positionJ = input().split()


    positionI = int(positionI)
    positionJ = int(positionJ)

    
    if estoque[positionI - 1][positionJ - 1] > 0:
        vendas += 1
        if estoque[positionI - 1][positionJ - 1] > 0:
            estoque[positionI - 1][positionJ - 1] -= 1
    
    j += 1


print(vendas)

