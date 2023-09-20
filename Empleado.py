class Empleado:
    def __init__(self, id_empleado, nombre_empleado, apellido_empleado, tipo_documento, documento,
                 correo, id_contrato, descrip_contrato, salario, id_banco, cuenta_bancaria, id_entidad,
                 entidad_salud, entidad_pension, entidad_cesantias, entidad_caja_compensacion, entidad_ARL):
        self._id_empleado = id_empleado
        self._nombre_empleado = nombre_empleado
        self._apellido_empleado = apellido_empleado
        self._tipo_documento = tipo_documento
        self._documento = documento
        self._correo = correo
        self._id_contrato = id_contrato
        self._descrip_contrato = descrip_contrato
        self._salario = salario
        self._id_banco = id_banco
        self._cuenta_bancaria = cuenta_bancaria
        self._id_entidad = id_entidad
        self._entidad_salud = entidad_salud
        self._entidad_pension = entidad_pension
        self._entidad_cesantias = entidad_cesantias
        self._entidad_caja_compensacion = entidad_caja_compensacion
        self._entidad_ARL = entidad_ARL

    # Métodos getter para obtener los valores de los atributos privados.

    def get_id_empleado(self):
        return self._id_empleado

    def get_nombre_empleado(self):
        return self._nombre_empleado

    def get_apellido_empleado(self):
        return self._apellido_empleado

    def get_tipo_documento(self):
        return self._tipo_documento

    def get_documento(self):
        return self._documento

    def get_correo(self):
        return self._correo

    def get_id_contrato(self):
        return self._id_contrato

    def get_descrip_contrato(self):
        return self._descrip_contrato

    def get_salario(self):
        return self._salario

    def get_id_banco(self):
        return self._id_banco

    def get_cuenta_bancaria(self):
        return self._cuenta_bancaria

    def get_id_entidad(self):
        return self._id_entidad

    def get_entidad_salud(self):
        return self._entidad_salud

    def get_entidad_pension(self):
        return self._entidad_pension

    def get_entidad_cesantias(self):
        return self._entidad_cesantias

    def get_entidad_caja_compensacion(self):
        return self._entidad_caja_compensacion

    def get_entidad_ARL(self):
        return self._entidad_ARL

    # Métodos setter para establecer los valores de los atributos privados.

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_nombre_empleado(self, nombre_empleado):
        self._nombre_empleado = nombre_empleado

    def set_apellido_empleado(self, apellido_empleado):
        self._apellido_empleado = apellido_empleado

    def set_tipo_documento(self, tipo_documento):
        self._tipo_documento = tipo_documento

    def set_documento(self, documento):
        self._documento = documento

    def set_correo(self, correo):
        self._correo = correo

    def set_id_contrato(self, id_contrato):
        self._id_contrato = id_contrato

    def set_descrip_contrato(self, descrip_contrato):
        self._descrip_contrato = descrip_contrato

    def set_salario(self, salario):
        self._salario = salario

    def set_id_banco(self, id_banco):
        self._id_banco = id_banco

    def set_cuenta_bancaria(self, cuenta_bancaria):
        self._cuenta_bancaria = cuenta_bancaria

    def set_id_entidad(self, id_entidad):
        self._id_entidad = id_entidad

    def set_entidad_salud(self, entidad_salud):
        self._entidad_salud = entidad_salud

    def set_entidad_pension(self, entidad_pension):
        self._entidad_pension = entidad_pension

    def set_entidad_cesantias(self, entidad_cesantias):
        self._entidad_cesantias = entidad_cesantias

    def set_entidad_caja_compensacion(self, entidad_caja_compensacion):
        self._entidad_caja_compensacion = entidad_caja_compensacion

    def set_entidad_ARL(self, entidad_ARL):
        self._entidad_ARL = entidad_ARL

# Crear una instancia de la clase Empleado
nuevo_empleado = Empleado(id_empleado=1, nombre_empleado="Juan", apellido_empleado="Pérez", tipo_documento="Cédula",
                          documento=123456789, correo="juan@example.com", id_contrato=101, descrip_contrato="Contrato A",
                          salario=5000.0, id_banco=201, cuenta_bancaria="1234567890", id_entidad=301,
                          entidad_salud="SaludCoop", entidad_pension="PensionCoop", entidad_cesantias="CesantíasCoop",
                          entidad_caja_compensacion="CajaCompCoop", entidad_ARL="ARLCoop")

# Utilizar los métodos getter para obtener los valores de los atributos
print("ID del empleado:", nuevo_empleado.get_id_empleado())
print("Nombre del empleado:", nuevo_empleado.get_nombre_empleado())
print("Apellido del empleado:", nuevo_empleado.get_apellido_empleado())
print("Tipo de documento:", nuevo_empleado.get_tipo_documento())
print("Documento:", nuevo_empleado.get_documento())
print("Correo:", nuevo_empleado.get_correo())
print("ID del contrato:", nuevo_empleado.get_id_contrato())
print("Descripción del contrato:", nuevo_empleado.get_descrip_contrato())
print("Salario:", nuevo_empleado.get_salario())
print("ID del banco:", nuevo_empleado.get_id_banco())
print("Cuenta bancaria:", nuevo_empleado.get_cuenta_bancaria())
print("ID de la entidad:", nuevo_empleado.get_id_entidad())
print("Entidad de salud:", nuevo_empleado.get_entidad_salud())
print("Entidad de pensión:", nuevo_empleado.get_entidad_pension())
print("Entidad de cesantías:", nuevo_empleado.get_entidad_cesantias())
print("Entidad de caja de compensación:", nuevo_empleado.get_entidad_caja_compensacion())
print("Entidad de ARL:", nuevo_empleado.get_entidad_ARL())

# Utilizar los métodos setter para cambiar los valores de los atributos
nuevo_empleado.set_salario(5500.0)
nuevo_empleado.set_cuenta_bancaria("9876543210")

# Verificar los cambios utilizando los métodos getter
print("\nDespués de la modificación:")
print("Salario:", nuevo_empleado.get_salario())
print("Cuenta bancaria:", nuevo_empleado.get_cuenta_bancaria())
