class Novedad:
    def __init__(self, id_novedad, id_tipo_novedad, descripcion_novedad, id_empleado, nombre_empleado, valor_novedad, fecha_novedad):
        self._id_novedad = id_novedad
        self._id_tipo_novedad = id_tipo_novedad
        self._descripcion_novedad = descripcion_novedad
        self._id_empleado = id_empleado
        self._nombre_empleado = nombre_empleado
        self._valor_novedad = valor_novedad
        self._fecha_novedad = fecha_novedad

    # Métodos getter
    def get_id_novedad(self):
        return self._id_novedad

    def get_id_tipo_novedad(self):
        return self._id_tipo_novedad

    def get_descripcion_novedad(self):
        return self._descripcion_novedad

    def get_id_empleado(self):
        return self._id_empleado

    def get_nombre_empleado(self):
        return self._nombre_empleado

    def get_valor_novedad(self):
        return self._valor_novedad

    def get_fecha_novedad(self):
        return self._fecha_novedad

    # Métodos setter
    def set_id_novedad(self, id_novedad):
        self._id_novedad = id_novedad

    def set_id_tipo_novedad(self, id_tipo_novedad):
        self._id_tipo_novedad = id_tipo_novedad

    def set_descripcion_novedad(self, descripcion_novedad):
        self._descripcion_novedad = descripcion_novedad

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_nombre_empleado(self, nombre_empleado):
        self._nombre_empleado = nombre_empleado

    def set_valor_novedad(self, valor_novedad):
        self._valor_novedad = valor_novedad

    def set_fecha_novedad(self, fecha_novedad):
        self._fecha_novedad = fecha_novedad
# Crear una instancia de la clase Novedad
novedad1 = Novedad(id_novedad=1, id_tipo_novedad=2, descripcion_novedad="Novedad importante",
                   id_empleado=101, nombre_empleado="Juan Pérez", valor_novedad=50.0,
                   fecha_novedad="2023-09-15")

# Ejemplo de uso de métodos getter para obtener valores
print("ID de la novedad:", novedad1.get_id_novedad())
print("ID del tipo de novedad:", novedad1.get_id_tipo_novedad())
print("Descripción de la novedad:", novedad1.get_descripcion_novedad())
print("ID del empleado:", novedad1.get_id_empleado())
print("Nombre del empleado:", novedad1.get_nombre_empleado())
print("Valor de la novedad:", novedad1.get_valor_novedad())
print("Fecha de la novedad:", novedad1.get_fecha_novedad())

# Ejemplo de uso de métodos setter para modificar valores
novedad1.set_descripcion_novedad("Nueva descripción de la novedad")
novedad1.set_valor_novedad(75.0)
print("Descripción de la novedad modificada:", novedad1.get_descripcion_novedad())
print("Valor de la novedad modificado:", novedad1.get_valor_novedad())
