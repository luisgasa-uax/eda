# -*- coding: utf-8 -*-

from Hotel import Hotel
from Utilidades import U as u
from Utilidades import Validaciones as bv

#print("Bienvenido a la nueva aplicación de " + u.autor())

mihotel = Hotel(10)
dni = "28019049N"

mihotel.nuevo_cliente(dni, "Pepe", "Jiménez")

print(mihotel.reserva_num_habitacion_cliente(1, dni, "04/11/2023"))

mihotel.buscar_reserva(1, "04/11/2023")

dni2 = "28019049X"
print(mihotel.reserva_num_habitacion_cliente(1, dni, "04/11/2023"))


# BetterComments
# * Información importante
# ! Atención
# ? Consulta
# TODO: cosas pendientes



    


