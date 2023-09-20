class Entidad:
    def __init__(self, id_entidad, id_tipo_identidad, tipo, nombre_entidad, NIT_entidad, id_empleado, nombre_empleado):
        self._id_entidad = id_entidad
        self._id_tipo_identidad = id_tipo_identidad
        self._tipo = tipo
        self._nombre_entidad = nombre_entidad
        self._NIT_entidad = NIT_entidad
        self._id_empleado = id_empleado
        self._nombre_empleado = nombre_empleado

    # Métodos getter para obtener los valores de los atributos privados.

    def get_id_entidad(self):
        return self._id_entidad

    def get_id_tipo_identidad(self):
        return self._id_tipo_identidad

    def get_tipo(self):
        return self._tipo

    def get_nombre_entidad(self):
        return self._nombre_entidad

    def get_NIT_entidad(self):
        return self._NIT_entidad

    def get_id_empleado(self):
        return self._id_empleado

    def get_nombre_empleado(self):
        return self._nombre_empleado

    # Métodos setter para establecer los valores de los atributos privados.

    def set_id_entidad(self, id_entidad):
        self._id_entidad = id_entidad

    def set_id_tipo_identidad(self, id_tipo_identidad):
        self._id_tipo_identidad = id_tipo_identidad

    def set_tipo(self, tipo):
        self._tipo = tipo

    def set_nombre_entidad(self, nombre_entidad):
        self._nombre_entidad = nombre_entidad

    def set_NIT_entidad(self, NIT_entidad):
        self._NIT_entidad = NIT_entidad

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_nombre_empleado(self, nombre_empleado):
        self._nombre_empleado = nombre_empleado

# Crear una instancia de la clase Entidad
nueva_entidad = Entidad(id_entidad=1, id_tipo_identidad=101, tipo="Tipo A", nombre_entidad="Entidad Ejemplo",
                        NIT_entidad=1234567890, id_empleado=201, nombre_empleado="Juan Pérez")

# Utilizar los métodos getter para obtener los valores de los atributos
print("ID de entidad:", nueva_entidad.get_id_entidad())
print("ID de tipo de identidad:", nueva_entidad.get_id_tipo_identidad())
print("Tipo de entidad:", nueva_entidad.get_tipo())
print("Nombre de entidad:", nueva_entidad.get_nombre_entidad())
print("NIT de entidad:", nueva_entidad.get_NIT_entidad())
print("ID de empleado:", nueva_entidad.get_id_empleado())
print("Nombre de empleado:", nueva_entidad.get_nombre_empleado())

# Utilizar los métodos setter para cambiar los valores de los atributos
nueva_entidad.set_tipo("Tipo B")
nueva_entidad.set_NIT_entidad(9876543210)

# Verificar los cambios utilizando los métodos getter
print("\nDespués de la modificación:")
print("Tipo de entidad:", nueva_entidad.get_tipo())
print("NIT de entidad:", nueva_entidad.get_NIT_entidad())
