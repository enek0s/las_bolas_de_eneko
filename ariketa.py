from bola import Bola
from balanza import Balanza

def encontrar_bola_pesada(bolas, balanza):
    while len(bolas) > 1:
        tercio = (len(bolas) + 2) // 3

        grupo1 = bolas[:tercio]
        grupo2 = bolas[tercio:2*tercio]
        grupo3 = bolas[2*tercio:]

        resultado = balanza.pesar(grupo1, grupo2)

        if resultado == 1:
            bolas = grupo1
        elif resultado == -1:
            bolas = grupo2
        else:
            bolas = grupo3

    return bolas[0]

# Crear 9 bolas que pesan 1
bolas = [Bola(1) for _ in range(9)]

# Hacer que una pese más
bolas[4].peso = 2

# Resolver
balanza = Balanza()
bola = encontrar_bola_pesada(bolas, balanza)
print(balanza.emaitza(bola))
