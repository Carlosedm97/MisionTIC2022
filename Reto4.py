import json
letras = input("")
dict_letras=json.loads(letras)

string_player = (map(str,input("").split(" ")))
list_player = ''.join(string_player)

letters=[]
score=0

for i in list_player:
    for key, value in dict_letras.items():
        if i==key:
            letters.append(i)
            score+=value

print(score)
list=" ".join(letters)
print(list)