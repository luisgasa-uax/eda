# -*- coding: utf-8 -*-

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.id = dni
        self.nombre = nombre
        self.apellido = apellido
        self.__historico_reservas = {}
    
    def __str__(self) -> str:
        return f"DNI: {self.id}, {self.nombre} {self.apellido}"
    
    def get_id(self) -> int :
        return self.id
    
    def get_nombre(self) -> str:
        return self.nombre
    
    def get_reservas_de_cliente(self):
        return self.historico_reservas

    def add_reserva(self, reserva):
        self.__historico_reservas[reserva.get_fecha()] = reserva
    
    def cancelar_reserva(self, reserva):
        self.__historico_reservas[reserva.get_fecha()] = None
