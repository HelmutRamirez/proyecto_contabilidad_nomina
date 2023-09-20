class ProvisionesParafiscales:
    def __init__(self, id_parafiscales, id_empleado, id_nomina, total_devengo, caja_compensacion, ICBF, Sena,
                 porcentaje_caja_compensacion, porcentaje_ICBF, porcentaje_SENA, total_parafiscales):
        self._id_parafiscales = id_parafiscales
        self._id_empleado = id_empleado
        self._id_nomina = id_nomina
        self._total_devengo = total_devengo
        self._caja_compensacion = caja_compensacion
        self._ICBF = ICBF
        self._Sena = Sena
        self._porcentaje_caja_compensacion = porcentaje_caja_compensacion
        self._porcentaje_ICBF = porcentaje_ICBF
        self._porcentaje_SENA = porcentaje_SENA
        self._total_parafiscales = total_parafiscales

    # Métodos getter
    def get_id_parafiscales(self):
        return self._id_parafiscales

    def get_id_empleado(self):
        return self._id_empleado

    def get_id_nomina(self):
        return self._id_nomina

    def get_total_devengo(self):
        return self._total_devengo

    def get_caja_compensacion(self):
        return self._caja_compensacion

    def get_ICBF(self):
        return self._ICBF

    def get_Sena(self):
        return self._Sena

    def get_porcentaje_caja_compensacion(self):
        return self._porcentaje_caja_compensacion

    def get_porcentaje_ICBF(self):
        return self._porcentaje_ICBF

    def get_porcentaje_SENA(self):
        return self._porcentaje_SENA

    def get_total_parafiscales(self):
        return self._total_parafiscales

    # Métodos setter
    def set_id_parafiscales(self, id_parafiscales):
        self._id_parafiscales = id_parafiscales

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_id_nomina(self, id_nomina):
        self._id_nomina = id_nomina

    def set_total_devengo(self, total_devengo):
        self._total_devengo = total_devengo

    def set_caja_compensacion(self, caja_compensacion):
        self._caja_compensacion = caja_compensacion

    def set_ICBF(self, ICBF):
        self._ICBF = ICBF

    def set_Sena(self, Sena):
        self._Sena = Sena

    def set_porcentaje_caja_compensacion(self, porcentaje_caja_compensacion):
        self._porcentaje_caja_compensacion = porcentaje_caja_compensacion

    def set_porcentaje_ICBF(self, porcentaje_ICBF):
        self._porcentaje_ICBF = porcentaje_ICBF

    def set_porcentaje_SENA(self, porcentaje_SENA):
        self._porcentaje_SENA = porcentaje_SENA

    def set_total_parafiscales(self, total_parafiscales):
        self._total_parafiscales = total_parafiscales
# Crear una instancia de la clase ProvisionesParafiscales
provisiones1 = ProvisionesParafiscales(id_parafiscales=1, id_empleado=101, id_nomina=2023, total_devengo=1500.0,
                                       caja_compensacion=75.0, ICBF=50.0, Sena=45.0,
                                       porcentaje_caja_compensacion=5.0, porcentaje_ICBF=3.33, porcentaje_SENA=3.0,
                                       total_parafiscales=123.33)

# Ejemplo de uso de métodos getter para obtener valores
print("ID de provisiones parafiscales:", provisiones1.get_id_parafiscales())
print("ID del empleado:", provisiones1.get_id_empleado())
print("ID de la nómina:", provisiones1.get_id_nomina())
print("Total devengado:", provisiones1.get_total_devengo())
print("Caja de compensación:", provisiones1.get_caja_compensacion())
print("ICBF:", provisiones1.get_ICBF())
print("SENA:", provisiones1.get_Sena())
print("Porcentaje de caja de compensación:", provisiones1.get_porcentaje_caja_compensacion())
print("Porcentaje de ICBF:", provisiones1.get_porcentaje_ICBF())
print("Porcentaje de SENA:", provisiones1.get_porcentaje_SENA())
print("Total de parafiscales:", provisiones1.get_total_parafiscales())

# Ejemplo de uso de métodos setter para modificar valores
provisiones1.set_total_devengo(1600.0)
provisiones1.set_porcentaje_caja_compensacion(6.0)
print("Total devengado modificado:", provisiones1.get_total_devengo())
print("Porcentaje de caja de compensación modificado:", provisiones1.get_porcentaje_caja_compensacion())
