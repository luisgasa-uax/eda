# -*- coding: utf-8 -*-

import re 

class Utilidades:

    AUTOR = "Beatriz Nevado"
    def __init__(self):
        pass
    
    @staticmethod
    def autor():
        return Utilidades.AUTOR

    
class Validaciones:

    REGEXP = "[0-9]{8}[A-Z]"
    DIGITO_CONTROL = "TRWAGMYFPDXBNJZSQVHLCKE"
    INVALIDOS = {"00000000T", "00000001R", "99999999R"}

    def __init__(self):
        pass

    @staticmethod
    def validar_dni( dni: str) -> bool:
        return dni not in Validaciones.INVALIDOS and re.match(Validaciones.REGEXP, dni) is not None and dni[8] == Validaciones.DIGITO_CONTROL[int(dni[0:8]) % 23] 
    
    