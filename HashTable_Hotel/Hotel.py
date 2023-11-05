# -*- coding: utf-8 -*-

from Cliente import Cliente
from Habitacion import Habitacion
from Reserva import Reserva
from HashTable_eda import HashTable_eda

class Hotel:
    # Constantes de error
    OK = 1
    HABITACION_NO_EXISTE = -1
    CLIENTE_NO_EXISTE = -2
    RESERVA_NO_EXISTE = -3
    HABITACIONES_NO_DISPONIBLES = -4
    CLIENTE_NO_TIENE_RESERVAS = -5
    FECHA_NO_DISPONIBLE = -6
    NO_RESERVAS = -7
    HABITACION_NO_DISPONIBLE = -8

    def __init__(self, num_habitaciones):
        self._num_habitaciones = num_habitaciones
        self._habitaciones = []
        self._clientes = []

        '''
        Reservas: Utiliza una tabla hash donde la 
            CLAVE sea una combinación del número de habitación y la fecha (por ejemplo, "Habitación 101: 20/09/2023") 
                --> clave para el cálculo del código hash
            y el 
            VALOR esté compuesto por el número de habitación, la fecha de reserva y el nombre del cliente. 
                --> nodo
        '''
        self.TAMANO_RESERVAS = num_habitaciones * 10
        self._reservas = HashTable_eda(self.TAMANO_RESERVAS)
        
        for i in range(num_habitaciones):
            self.nueva_habitacion(i)
        
    def __str__(self):
        pass

    def nuevo_cliente(self, dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        self.__agregar_cliente(cliente)
    
    def __agregar_cliente(self, cliente ):
        self._clientes.append(cliente)

    def nueva_habitacion(self, num_habitacion):
        habitacion = Habitacion(num_habitacion)
        self.__agregar_habitacion(habitacion)
    
    def __agregar_habitacion(self, habitacion ):
        self._habitaciones.append(habitacion)

    def reserva_habitacion(self, habitacion, cliente, fecha):
        # Creamos la reserva y lo reflejamos en el hotel y en los históricos de la habitación y del cliente
        reserva = Reserva(habitacion, cliente, fecha)
        self._reservas.insert(reserva.get_id(), reserva)
        habitacion.add_reserva(reserva)
        cliente.add_reserva(reserva)
        return reserva

    def reserva_num_habitacion_cliente(self, num_habitacion, dni_cliente, fecha):

        # comprobamos que la habitación existe
        habitacion = self.buscar_habitacion(num_habitacion)
        if not habitacion:
            return self.HABITACION_NO_EXISTE
        
        # comprbamos que la habitación está disponible        
        if habitacion.esta_reservada(fecha):
            self.imprime_errores(self.HABITACION_NO_DISPONIBLE)
            return self.HABITACION_NO_DISPONIBLE
        
        # comprobamos que el cliente existe
        cliente = self.buscar_cliente( dni_cliente )
        if not cliente:
            self.imprime_errores(self.CLIENTE_NO_EXISTE)
            return self.CLIENTE_NO_EXISTE

        return self.reserva_habitacion( habitacion, cliente, fecha)
        

    def reservar_una_habitacion_disponible_cliente(self, dni_cliente, fecha):
        cliente = self.buscar_cliente(dni_cliente)
        if cliente == None:
            self.imprime_errores(self.CLIENTE_NO_EXISTE)
            return self.CLIENTE_NO_EXISTE
        
        habitacion = self.obtener_habitacion_disponible_en_fecha(fecha)
        if habitacion == None:
            self.imprime_errores(self.HABITACIONES_NO_DISPONIBLES)
            return self.HABITACIONES_NO_DISPONIBLES

        return self.reserva_habitacion(self, habitacion, cliente, fecha)
        
    
    def get_reservas_habitacion(self, num_habitacion):
        habitacion = self.buscar_habitacion(num_habitacion)
        if habitacion == None:
            self.imprime_errores(self.HABITACION_NO_EXISTE)
            return self.HABITACION_NO_EXISTE
        
        return habitacion.get_historico_reservas()
    

    def get_reservas_de_cliente(self, dni):
        cliente = self.buscar_cliente(dni)
        if cliente == None:
            self.imprime_errores(self.CLIENTE_NO_EXISTE)
            return self.CLIENTE_NO_EXISTE
        
        return cliente.get_reservas_de_cliente()
    
    
    def buscar_habitacion(self, num_habitacion) -> Habitacion:
        for habitacion in self._habitaciones:
            if habitacion.get_id() == num_habitacion:
                return habitacion
        self.imprime_errores(self.HABITACION_NO_EXISTE)
        return self.HABITACION_NO_EXISTE
    
    def buscar_cliente(self, dni) -> Cliente:
        for cliente in self._clientes:
            if cliente.get_id() == dni :
                return cliente
        self.imprime_errores(self.CLIENTE_NO_EXISTE)
        return self.CLIENTE_NO_EXISTE

    # este método solo sirve cuando tenemos las reservas almacenadas en una lista, pero no en un hashtable
    def buscar_reserva_en_lista(self, num_reserva) -> Reserva:
        for reserva in self._reservas:
            if reserva.get_id() == num_reserva :
                return reserva
        self.imprime_errores(self.RESERVA_NO_EXISTE)
        return self.RESERVA_NO_EXISTE
    
    def buscar_reserva(self, num_habitacion, fecha) -> Reserva:
        codigo_hash = Reserva.calcula_clave_reserva(num_habitacion, fecha)
        return self._reservas.search(codigo_hash)  # la reserva o None 

    @staticmethod
    def imprime_errores(cod_error):
        errores = { Hotel.HABITACION_NO_EXISTE: "Habitación no existente", 
                    Hotel.CLIENTE_NO_EXISTE: "Cliente no existenete", 
                    Hotel.RESERVA_NO_EXISTE: "Reserva no existente", 
                    Hotel.HABITACIONES_NO_DISPONIBLES: "Todas las habitaciones ocupadas",  
                    Hotel.OK: "Todo bien", 
                    Hotel.CLIENTE_NO_TIENE_RESERVAS: "El cliente no tiene reservas", 
                    Hotel.FECHA_NO_DISPONIBLE: "Fecha no disponible",
                    Hotel.NO_RESERVAS: "No se han realizado reservas", 
                    Hotel.HABITACION_NO_DISPONIBLE: "Habitación no disponible"
                    }
        print(errores[cod_error])

    def obtener_habitacion_disponible_en_fecha(self, fecha):
        for habitacion in self._habitaciones:
            if not habitacion.esta_reservada(fecha):
                return habitacion
        return self.HABITACIONES_NO_DISPONIBLES

    def cancelar_reserva(self, habitacion, cliente, fecha ):
        reserva = self.buscar_reserva( habitacion.get_id(), fecha)
        if reserva == None:
            self.imprime_errores(self.RESERVA_NO_EXISTE)
            return self.RESERVA_NO_EXISTE

        habitacion.cancelar_reserva(reserva)
        cliente.cancelar_reserva(reserva)
        return self._reservas.remove(reserva.get_id())
        
    def cancelar_reserva_habitacion_cliente_fecha(self, num_habitacion, dni_cliente, fecha):
        # comprobamos que la habitación existe
        habitacion = self.buscar_habitacion(num_habitacion)
        if not habitacion:
            return self.HABITACION_NO_EXISTE
        
        # comprbamos que la habitación está disponible        
        if habitacion.esta_reservada(fecha):
            self.imprime_errores(self.HABITACION_NO_DISPONIBLE)
            return self.HABITACION_NO_DISPONIBLE
        
        # comprobamos que el cliente existe
        cliente = self.buscar_cliente( dni_cliente )
        if not cliente:
            self.imprime_errores(self.CLIENTE_NO_EXISTE)
            return self.CLIENTE_NO_EXISTE
        
        return self.cancelar_reserva(self, habitacion, cliente, fecha)

