# -*- coding: utf-8 -*-

from Habitacion import Habitacion
from Cliente import Cliente

class Reserva:
    def __init__(self, habitacion, cliente, fecha):
                 # "Habitación 101: 20/09/2023"
        self.id = self.calcula_clave_reserva(habitacion.get_id(), fecha)
        self.fecha = fecha
        self.id_cliente = cliente.get_id()
        self.id_habitacion = habitacion.get_id()
    
    
    @staticmethod
    def calcula_clave_reserva(num_habitacion, fecha):
        return (f"Habitación {num_habitacion}: {fecha}")
        

    def __str__(self) -> str:
        return f"{self.id} : {self.fecha} : {self.id_cliente}"
    
    def get_fecha(self):
        return self.fecha
    
    def get_id(self):
        return self.id

    def get_id_cliente(self):
        return self.id_cliente

    def get_id_habitacion(self):
        return self.id_habitacion
    
    
    
    
