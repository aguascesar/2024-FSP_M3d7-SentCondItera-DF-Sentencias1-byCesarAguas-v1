# * my_cachipun v1 (https://github.com/aguascesar/2024-FSP_M3d7-SentCondItera-DF-Sentencias1-byCesarAguas-v1)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/aguascesar/2024-FSP_M3d7-SentCondItera-DF-Sentencias1-byCesarAguas-v1/LICENSE)
#   
#

import random
import sys
# Declaracion de funcion para jugar
def juego(user_op):
    alternativas = ['piedra', 'papel', 'tijera']
    
    if user_op not in alternativas:
        print("Argumento inválido: Debe ser piedra, papel o tijera.")
        return

    pc_op = random.choice(alternativas)
    
    print("Tu jugaste:", user_op.capitalize())
    print("Computador jugó:", pc_op.capitalize())

    if user_op == pc_op:
        print("Empate!")
    elif (user_op == 'piedra' and pc_op == 'tijera') or (user_op == 'papel' and pc_op == 'piedra') or (user_op == 'tijera' and pc_op == 'papel'):
        print("Ganaste!!")
    else:
        print("Perdiste!")


# Se necesitan algunas comprobaciones

# Comprobar cantidad de argumentos minimos
if len(sys.argv) != 2:
    print("Por favor escriba: python cachipun.py [piedra|papel|tijera]")
    sys.exit(1)

# Obtener alternativa del usuario, con todos los caracteres en minusculas
user_op = sys.argv[1].lower()

# Realizar jugada
juego(user_op)
