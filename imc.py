# * my_imc v1 (https://github.com/...//)
# * Copyright 2024 Cesar Aguas
# * Licensed under AGPL3.0 (https://github.com/.../LICENSE)
#   
#
import sys 
#   Se intenta calcular el indice de masa muscular, mediante una funcion,
#utilizando datos obtenidos mediante argumentos peso (k) y altura (cm)
def indice(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)

#  Se intenta definir los grados de obesidad.
#
#       IMC     Clasificación OMS
#       < 18.5     Bajo Peso
#       18.5, 25  Adecuado
#       25, 30    Sobrepeso
#       30, 35    Obesidad Grado I
#       35, 40    Obesidad Grado II
#       > 40      Obesidad Grado III

def escala(imc):

    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"

# Comenzando las rutinas

# La cantidad de argumentos debe ser 2, = nombre_binario argumento_1 argumento_2
if len(sys.argv) != 3:
    print("Por favor escriba: ./imc [kg] [cm]")
    sys.exit(1)

try:
    # Extraer argumentos
    peso = float(sys.argv[1])
    altura = float(sys.argv[2]) / 100
except Exception as e:
    print("Error: ", e.message, e.args)
    sys.exit(1)

# Realizar calculos
imc = indice(peso, altura)
oms = escala(imc)

print("Su IMC es:", imc)
print("La escala OMS es:", oms)


