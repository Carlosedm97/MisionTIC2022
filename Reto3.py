productos = list(map(str,input("").split(" ")))
productos_list = ''.join(productos)

iw = [0] + [i+1 for i in range(len(productos_list)-1) if productos_list[i] != productos_list[i+1]] + [len(productos_list)]

dw = [productos_list[i] for i in range(len(productos_list)-1) if productos_list[i] != productos_list[i+1]] + [productos_list[-1]]

cw = [ iw[j] - iw[j-1] for j in range(1, len(iw))]

caracteres = " ".join(dw)
print(caracteres)
digitos = " ".join(map(str, cw))
print(digitos)