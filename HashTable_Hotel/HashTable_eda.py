class HashTable_eda:
    def __init__(self, size, max_amount_collisions=5, auto_resize_new_size=1.5):     # size será el tamaño de la tabla hash
        self.size = size

        '''
        self.table = [{}] * size
        Al usar [{}] * size estaríamos creando una lista de diccionarios donde cada elemento es una referencia al mismo diccionario vacío. 
        Si modificamos uno de los diccionarios, todos los demás se modificarán de la misma manera porque son el mismo objeto. 
        En su lugar, debemos crear un nuevo diccionario para cada posición:# declaramos la tabla_hash con un diccionario vacío dentro de cada posición
        '''
        self.table = [{} for _ in range(size)]  # Crea una lista de 'size' diccionarios vacíos independientes
        self.WARNING_AMOUNT_COLLISONS = max_amount_collisions  
        self.AUTO_RESIZE_NEW_SIZE = auto_resize_new_size
    
    # Función hash
    def _hash_func(self, value):   # declaramos el método privado _metodo(self, ...)
        key = 0
        # PepitoPiscinas57   => 16 caracteres
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % self.size   # --> la posición de la tabla en la que debemos colocar el nodo

    # Metodo para ingresar elementos
    def insert(self, value, node): 
        hash = self._hash_func(value)  # --> hash es la posición de la tabla donde tenemos que insertar el nodo
 
        internal_key = self._internal_dict_key(value)  # "Habitación 101: 20/09/2023hash"

        '''
            Comprobamos la longitud de la lista interna de la posición en la tabla
            Que será la cantidad de elementos que tiene la lista interna
            Esta cantidad coincide con la siguiente posición libre de la lista interna 
            Posibles casos: 
                - la posición de la tabla aún no tiene elementos ==> internal_position = 0
                    Insertamos en el primer elmento de la lista interna
                - la posición de la tabla ya tenga elmementos ==> internal_position > 0
                    Insertamos en la primera posición libre de la lista interna, es decir en lista_interna[internal_position]
        '''

        self.table[hash][internal_key] = node   # insertamos el nodo en la primera posición libre
        

        # en caso de que la cantidad de elementos supere el límite establecido, redimensionamos la tabla
        if len(self.table[hash]) > self.WARNING_AMOUNT_COLLISONS:
            self.resize_myself()
        
   
    def search(self, value ): # Metodo para buscar elementos
        hash = self._hash_func(value)
        if len(self.table[hash]) == 0 :
            # no hay nodos en esa posición
            return None
        else:
            # sí hay nodos en la posición
            # el nodo que busco está en el diccionario interno de esta posición
            internal_key = self._internal_dict_key(value)
            if self.table[hash][internal_key]: 
                return self.table[hash][internal_key] 
            # ?? return hex(id(self.table[hash]))
            print("El usuario no se ha localizado")
            return None
        

    def remove(self, value): # Metodo para eleminar elementos
        nodo = self.search(value)
        if nodo != None :
            del nodo
            return 1
        else : 
            print("No se encontró el elemento con el valor: ", value)
            return None

    # redimensionar la tabla
    def resize_myself(self, multiplier):
        new_dimension = self.size * multiplier
        new_table = [{} for _ in range(new_dimension)] 
        
        for internal_dict in self.table:
            if len(internal_dict) != 0:
                for key, value in internal_dict.items:
                    new_index = self._hash_func(key)
                    new_table[new_index].update({key: value})
        self.size = new_dimension
        self.table = new_table
    
    def _check_hastable_collision_status(self):
        for internal_dict in self.table:
            if len(internal_dict) >= self.WARNING_AMOUNT_COLLISONS:
                self.resize_myself(self.AUTO_RESIZE_NEW_SIZE)

    # calcula la clave del diccionario interno de cada posición de la tabla hash, a partir del string value concatenándolo con el código hash
    def _internal_dict_key(self, value):
        hash = self._hash_func(value)
        return value + str(hash)  # "Habitación 101: 20/09/2023hash"

