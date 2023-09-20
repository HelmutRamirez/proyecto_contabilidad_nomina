class SeguridadSocial:
    def __init__(self, id_empleado, id_seguridad_social, id_nomina, total_devengo, arl, total_prestaciones_empleado,
                 total_prestaciones_empresa, porcentaje_empleado_salud, porcentaje_empresa_salud,
                 porcentaje_empleado_pension, porcentaje_empresa_pension, salud_empresa, pension_empresa):
        self._id_empleado = id_empleado
        self._id_seguridad_social = id_seguridad_social
        self._id_nomina = id_nomina
        self._total_devengo = total_devengo
        self._arl = arl
        self._total_prestaciones_empleado = total_prestaciones_empleado
        self._total_prestaciones_empresa = total_prestaciones_empresa
        self._porcentaje_empleado_salud = porcentaje_empleado_salud
        self._porcentaje_empresa_salud = porcentaje_empresa_salud
        self._porcentaje_empleado_pension = porcentaje_empleado_pension
        self._porcentaje_empresa_pension = porcentaje_empresa_pension
        self._salud_empresa = salud_empresa
        self._pension_empresa = pension_empresa

    # Métodos getter
    def get_id_empleado(self):
        return self._id_empleado

    def get_id_seguridad_social(self):
        return self._id_seguridad_social

    def get_id_nomina(self):
        return self._id_nomina

    def get_total_devengo(self):
        return self._total_devengo

    def get_arl(self):
        return self._arl

    def get_total_prestaciones_empleado(self):
        return self._total_prestaciones_empleado

    def get_total_prestaciones_empresa(self):
        return self._total_prestaciones_empresa

    def get_porcentaje_empleado_salud(self):
        return self._porcentaje_empleado_salud

    def get_porcentaje_empresa_salud(self):
        return self._porcentaje_empresa_salud

    def get_porcentaje_empleado_pension(self):
        return self._porcentaje_empleado_pension

    def get_porcentaje_empresa_pension(self):
        return self._porcentaje_empresa_pension

    def get_salud_empresa(self):
        return self._salud_empresa

    def get_pension_empresa(self):
        return self._pension_empresa

    # Métodos setter
    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_id_seguridad_social(self, id_seguridad_social):
        self._id_seguridad_social = id_seguridad_social

    def set_id_nomina(self, id_nomina):
        self._id_nomina = id_nomina

    def set_total_devengo(self, total_devengo):
        self._total_devengo = total_devengo

    def set_arl(self, arl):
        self._arl = arl

    def set_total_prestaciones_empleado(self, total_prestaciones_empleado):
        self._total_prestaciones_empleado = total_prestaciones_empleado

    def set_total_prestaciones_empresa(self, total_prestaciones_empresa):
        self._total_prestaciones_empresa = total_prestaciones_empresa

    def set_porcentaje_empleado_salud(self, porcentaje_empleado_salud):
        self._porcentaje_empleado_salud = porcentaje_empleado_salud

    def set_porcentaje_empresa_salud(self, porcentaje_empresa_salud):
        self._porcentaje_empresa_salud = porcentaje_empresa_salud

    def set_porcentaje_empleado_pension(self, porcentaje_empleado_pension):
        self._porcentaje_empleado_pension = porcentaje_empleado_pension

    def set_porcentaje_empresa_pension(self, porcentaje_empresa_pension):
        self._porcentaje_empresa_pension = porcentaje_empresa_pension

    def set_salud_empresa(self, salud_empresa):
        self._salud_empresa = salud_empresa

    def set_pension_empresa(self, pension_empresa):
        self._pension_empresa = pension_empresa


# Crear una instancia de la clase SeguridadSocial
seguridad_social1 = SeguridadSocial(id_empleado=101, id_seguridad_social=1, id_nomina=2023, total_devengo=2500.0,
                                     arl=120.0, total_prestaciones_empleado=200.0, total_prestaciones_empresa=180.0,
                                     porcentaje_empleado_salud=4.0, porcentaje_empresa_salud=8.0,
                                     porcentaje_empleado_pension=3.0, porcentaje_empresa_pension=6.0,
                                     salud_empresa=160.0, pension_empresa=120.0)

# Ejemplo de uso de métodos getter para obtener valores
print("ID del empleado:", seguridad_social1.get_id_empleado())
print("ID de seguridad social:", seguridad_social1.get_id_seguridad_social())
print("ID de la nómina:", seguridad_social1.get_id_nomina())
print("Total devengado:", seguridad_social1.get_total_devengo())
print("ARL:", seguridad_social1.get_arl())
print("Total prestaciones para el empleado:", seguridad_social1.get_total_prestaciones_empleado())
print("Total prestaciones para la empresa:", seguridad_social1.get_total_prestaciones_empresa())
print("Porcentaje de empleado en salud:", seguridad_social1.get_porcentaje_empleado_salud())
print("Porcentaje de empresa en salud:", seguridad_social1.get_porcentaje_empresa_salud())
print("Porcentaje de empleado en pensión:", seguridad_social1.get_porcentaje_empleado_pension())
print("Porcentaje de empresa en pensión:", seguridad_social1.get_porcentaje_empresa_pension())
print("Salud a cargo de la empresa:", seguridad_social1.get_salud_empresa())
print("Pensión a cargo de la empresa:", seguridad_social1.get_pension_empresa())

# Ejemplo de uso de métodos setter para modificar valores
seguridad_social1.set_total_devengo(2600.0)
seguridad_social1.set_arl(130.0)
print("Total devengado modificado:", seguridad_social1.get_total_devengo())
print("ARL modificado:", seguridad_social1.get_arl())
