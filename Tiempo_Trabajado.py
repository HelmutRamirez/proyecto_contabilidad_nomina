class TiempoTrabajado:
    def __init__(self, id_tiempo_trabajado, id_empleado, horas_extras_diurna, valor_extras_diurnas, horas_dominicales,
                 valor_dominicales, horas_festivas, valor_festivos, horas_extra_nocturnas, valor_extras_nocturnas,
                 cant_horas_deducidad, valor_deduccion_horas):
        self._id_tiempo_trabajado = id_tiempo_trabajado
        self._id_empleado = id_empleado
        self._horas_extras_diurna = horas_extras_diurna
        self._valor_extras_diurnas = valor_extras_diurnas
        self._horas_dominicales = horas_dominicales
        self._valor_dominicales = valor_dominicales
        self._horas_festivas = horas_festivas
        self._valor_festivos = valor_festivos
        self._horas_extra_nocturnas = horas_extra_nocturnas
        self._valor_extras_nocturnas = valor_extras_nocturnas
        self._cant_horas_deducidad = cant_horas_deducidad
        self._valor_deduccion_horas = valor_deduccion_horas

    # Métodos getter
    def get_id_tiempo_trabajado(self):
        return self._id_tiempo_trabajado

    def get_id_empleado(self):
        return self._id_empleado

    def get_horas_extras_diurna(self):
        return self._horas_extras_diurna

    def get_valor_extras_diurnas(self):
        return self._valor_extras_diurnas

    def get_horas_dominicales(self):
        return self._horas_dominicales

    def get_valor_dominicales(self):
        return self._valor_dominicales

    def get_horas_festivas(self):
        return self._horas_festivas

    def get_valor_festivos(self):
        return self._valor_festivos

    def get_horas_extra_nocturnas(self):
        return self._horas_extra_nocturnas

    def get_valor_extras_nocturnas(self):
        return self._valor_extras_nocturnas

    def get_cant_horas_deducidad(self):
        return self._cant_horas_deducidad

    def get_valor_deduccion_horas(self):
        return self._valor_deduccion_horas

    # Métodos setter
    def set_id_tiempo_trabajado(self, id_tiempo_trabajado):
        self._id_tiempo_trabajado = id_tiempo_trabajado

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_horas_extras_diurna(self, horas_extras_diurna):
        self._horas_extras_diurna = horas_extras_diurna

    def set_valor_extras_diurnas(self, valor_extras_diurnas):
        self._valor_extras_diurnas = valor_extras_diurnas

    def set_horas_dominicales(self, horas_dominicales):
        self._horas_dominicales = horas_dominicales

    def set_valor_dominicales(self, valor_dominicales):
        self._valor_dominicales = valor_dominicales

    def set_horas_festivas(self, horas_festivas):
        self._horas_festivas = horas_festivas

    def set_valor_festivos(self, valor_festivos):
        self._valor_festivos = valor_festivos

    def set_horas_extra_nocturnas(self, horas_extra_nocturnas):
        self._horas_extra_nocturnas = horas_extra_nocturnas

    def set_valor_extras_nocturnas(self, valor_extras_nocturnas):
        self._valor_extras_nocturnas = valor_extras_nocturnas

    def set_cant_horas_deducidad(self, cant_horas_deducidad):
        self._cant_horas_deducidad = cant_horas_deducidad

    def set_valor_deduccion_horas(self, valor_deduccion_horas):
        self._valor_deduccion_horas = valor_deduccion_horas
# Crear una instancia de la clase TiempoTrabajado
tiempo_trabajado1 = TiempoTrabajado(id_tiempo_trabajado=1, id_empleado=101, horas_extras_diurna=5.0,
                                     valor_extras_diurnas=50.0, horas_dominicales=2.0, valor_dominicales=30.0,
                                     horas_festivas=1.0, valor_festivos=20.0, horas_extra_nocturnas=3.0,
                                     valor_extras_nocturnas=45.0, cant_horas_deducidad=1.0,
                                     valor_deduccion_horas=10.0)

# Ejemplo de uso de métodos getter para obtener valores
print("ID de tiempo trabajado:", tiempo_trabajado1.get_id_tiempo_trabajado())
print("ID de empleado:", tiempo_trabajado1.get_id_empleado())
print("Horas extras diurnas:", tiempo_trabajado1.get_horas_extras_diurna())
print("Valor de horas extras diurnas:", tiempo_trabajado1.get_valor_extras_diurnas())
print("Horas dominicales:", tiempo_trabajado1.get_horas_dominicales())
print("Valor de horas dominicales:", tiempo_trabajado1.get_valor_dominicales())
print("Horas festivas:", tiempo_trabajado1.get_horas_festivas())
print("Valor de horas festivas:", tiempo_trabajado1.get_valor_festivos())
print("Horas extra nocturnas:", tiempo_trabajado1.get_horas_extra_nocturnas())
print("Valor de horas extra nocturnas:", tiempo_trabajado1.get_valor_extras_nocturnas())
print("Cantidad de horas deducidas:", tiempo_trabajado1.get_cant_horas_deducidad())
print("Valor de deducción de horas:", tiempo_trabajado1.get_valor_deduccion_horas())

# Ejemplo de uso de métodos setter para modificar valores
tiempo_trabajado1.set_horas_extras_diurna(6.0)
tiempo_trabajado1.set_valor_deduccion_horas(15.0)
print("Horas extras diurnas modificadas:", tiempo_trabajado1.get_horas_extras_diurna())
print("Valor de deducción de horas modificado:", tiempo_trabajado1.get_valor_deduccion_horas())

        