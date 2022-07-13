jugador1= input("")
jugador2 = input("")
urna = input("")

puntosJugador1 = 0
puntosJugador2 = 0

for i in urna:
    if i in jugador1 and not i in jugador2:
        puntosJugador1 += 1
    elif i in jugador2 and not i in jugador1:
        puntosJugador2 += 1
    else:
        puntosJugador1 += 1
        puntosJugador2 += 1
        
    if puntosJugador1 > puntosJugador2:
            print("C", end="")
    elif puntosJugador1 < puntosJugador2:
            print("E", end="")
    else:
            print("T", end="")
        