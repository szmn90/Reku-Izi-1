def ciag_razy_3(n):
    if n < 2:
        return ""
    elif n == 2:
        return 8
    else:
        return ciag_razy_3(n-1) * 3

lista = 7
if lista <=0:
    print("blad")
else:
    for i in range(lista):
        print(ciag_razy_3(i))
