class TipoContrato:
    def __init__(self, id_contrato, id_empleado, descrip_contrato, salario):
        self._id_contrato = id_contrato
        self._id_empleado = id_empleado
        self._descrip_contrato = descrip_contrato
        self._salario = salario

    # Métodos getter
    def get_id_contrato(self):
        return self._id_contrato

    def get_id_empleado(self):
        return self._id_empleado

    def get_descrip_contrato(self):
        return self._descrip_contrato

    def get_salario(self):
        return self._salario

    # Métodos setter
    def set_id_contrato(self, id_contrato):
        self._id_contrato = id_contrato

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_descrip_contrato(self, descrip_contrato):
        self._descrip_contrato = descrip_contrato

    def set_salario(self, salario):
        self._salario = salario
# Crear una instancia de la clase TipoContrato
tipo_contrato1 = TipoContrato(id_contrato=1, id_empleado=101, descrip_contrato="Contrato a término indefinido", salario=3500.0)

# Ejemplo de uso de métodos getter para obtener valores
print("ID de contrato:", tipo_contrato1.get_id_contrato())
print("ID de empleado:", tipo_contrato1.get_id_empleado())
print("Descripción de contrato:", tipo_contrato1.get_descrip_contrato())
print("Salario:", tipo_contrato1.get_salario())

# Ejemplo de uso de métodos setter para modificar valores
tipo_contrato1.set_descrip_contrato("Contrato a término fijo")
tipo_contrato1.set_salario(3200.0)
print("Descripción de contrato modificada:", tipo_contrato1.get_descrip_contrato())
print("Salario modificado:", tipo_contrato1.get_salario())
