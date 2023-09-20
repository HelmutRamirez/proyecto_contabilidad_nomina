class Banco:
    def __init__(self, id_banco, id_empleado, descripcion, numero_cuenta):
        self._id_banco = id_banco
        self._id_empleado = id_empleado
        self._descripcion = descripcion
        self._numero_cuenta = numero_cuenta
    def get_id_banco(self):
        return self._id_banco

    def get_id_empleado(self):
        return self._id_empleado

    def get_descripcion(self):
        return self._descripcion

    def get_numero_cuenta(self):
        return self._numero_cuenta
    
    
    def set_id_banco(self, id_banco):
        self._id_banco = id_banco

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def set_numero_cuenta(self, numero_cuenta):
        self._numero_cuenta = numero_cuenta
        
nuevo_banco = Banco(id_banco=1, id_empleado=101, descripcion="Banco Ejemplo", numero_cuenta="1234567890")


print("ID del banco:", nuevo_banco.get_id_banco())
print("ID del empleado:", nuevo_banco.get_id_empleado())
print("Descripción:", nuevo_banco.get_descripcion())
print("Número de cuenta:", nuevo_banco.get_numero_cuenta())

nuevo_banco.set_id_banco(2)
nuevo_banco.set_id_empleado(102)
nuevo_banco.set_descripcion("Banco Modificado")
nuevo_banco.set_numero_cuenta("9876543210")


print("\nDespués de la modificación:")
print("ID del banco:", nuevo_banco.get_id_banco())
print("ID del empleado:", nuevo_banco.get_id_empleado())
print("Descripción:", nuevo_banco.get_descripcion())
print("Número de cuenta:", nuevo_banco.get_numero_cuenta())