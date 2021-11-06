def ciag_3(n):
    if n < 2:
        return ""
    elif n == 2:
        return 2
    else:
        return ciag_3(n-1) + 3

lista = 7
if lista <=0:
    print("blad")
else:
    for i in range(lista):
        print(ciag_3(i))