premioJuan = int(input())
premioMateo = premioJuan * 2 + 4
premioAndres = (premioJuan + premioMateo) // 5

print(premioJuan,premioMateo,premioAndres)

if 0 <= premioAndres <= 20:
  print("Uno")
elif 21 <= premioAndres <= 30:
  print("Dos")
elif 31 <= premioAndres <= 50:
  print("Tres")
elif premioAndres >= 51:
  print("Cuatro")
  