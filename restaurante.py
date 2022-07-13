def tiposproductos(lista):
    empty_list=[]
    for i in lista:
        if i not in empty_list:
            empty_list.append(i)
    return empty_list

def productosfaltantes(codigos, clases, producto):
    empty=[]
    for i in range(len(clases)):
        if producto == clases[i]:
            for j in codigos:
                if j == i:
                  empty.append(j)
    return empty

def novendo(competencia, restaurante):
    list_empty=[]
    for i in competencia:
            if i not in restaurante:
                list_empty.append(i)
    return list_empty
    
def cambio(olimpicon, restaurante):
    lista1_olimpicon= []
    lista2_restaurante=[]
    for i in olimpicon:
        if i not in restaurante:
            lista2_restaurante.append(i)
    for j in restaurante:
        if j not in olimpicon:
            lista1_olimpicon.append(j)
         
    if len(lista1_olimpicon) >= len(lista2_restaurante):
                   resultado=(len(lista2_restaurante))
    elif len(lista2_restaurante) >= len(lista1_olimpicon):
                   resultado=(len(lista1_olimpicon))
                   
    return resultado