# Valor que joão tem
V = int(input())

# Contas para pagar

A = int(input())
F = int(input())
P = int(input())

num = int()

if A + F + P <= V:
    num = 3

elif A + F <= V and A + F + P > V:
    num = 2

elif A + P <= V and A + F + P > V:
    num = 2

elif P + F <= V and A + F + P > V:
    num = 2

elif A <= V and A + F + P > V and A + F > V and A + P > V and P + F > V:
    num = 1

elif F <= V and A + F + P > V and A + F > V and A + P > V and P + F > V:
    num = 1

elif P <= V and A + F + P > V and A + F > V and A + P > V and P + F > V:
    num = 1

else: 
    num = 0

print(num)