class Historico:
    def __init__(self, id_historico, id_nomina, año_mes, id_empleado, nombre_empleado, apellido_empleado,
                 id_contrato, tipo_contrato, salario, id_seguridad_social, salud_empleado, pension_empleado,
                 total_prestaciones_empleado, total_prestaciones_empresa, valor_arl, id_parafiscales, total_parafiscales,
                 id_novedad, id_tipo_novedad, descripcion_novedad, fecha_novedad, valor_novedad, id_tiempo_trabajado,
                 dias_pagados, horas_extras_diurnas, valor_extras_diurnas, horas_extras_nocturnas,
                 valor_extras_nocturnas, horas_festivas, valor_festivos, horas_dominicales, valor_horas_dominicales,
                 cant_horas_deducidad, valor_deduccion_horas, total_devengo, total_deducciones, total_sueldo):
        self._id_historico = id_historico
        self._id_nomina = id_nomina
        self._año_mes = año_mes
        self._id_empleado = id_empleado
        self._nombre_empleado = nombre_empleado
        self._apellido_empleado = apellido_empleado
        self._id_contrato = id_contrato
        self._tipo_contrato = tipo_contrato
        self._salario = salario
        self._id_seguridad_social = id_seguridad_social
        self._salud_empleado = salud_empleado
        self._pension_empleado = pension_empleado
        self._total_prestaciones_empleado = total_prestaciones_empleado
        self._total_prestaciones_empresa = total_prestaciones_empresa
        self._valor_arl = valor_arl
        self._id_parafiscales = id_parafiscales
        self._total_parafiscales = total_parafiscales
        self._id_novedad = id_novedad
        self._id_tipo_novedad = id_tipo_novedad
        self._descripcion_novedad = descripcion_novedad
        self._fecha_novedad = fecha_novedad
        self._valor_novedad = valor_novedad
        self._id_tiempo_trabajado = id_tiempo_trabajado
        self._dias_pagados = dias_pagados
        self._horas_extras_diurnas = horas_extras_diurnas
        self._valor_extras_diurnas = valor_extras_diurnas
        self._horas_extras_nocturnas = horas_extras_nocturnas
        self._valor_extras_nocturnas = valor_extras_nocturnas
        self._horas_festivas = horas_festivas
        self._valor_festivos = valor_festivos
        self._horas_dominicales = horas_dominicales
        self._valor_horas_dominicales = valor_horas_dominicales
        self._cant_horas_deducidad = cant_horas_deducidad
        self._valor_deduccion_horas = valor_deduccion_horas
        self._total_devengo = total_devengo
        self._total_deducciones = total_deducciones
        self._total_sueldo = total_sueldo

    # Métodos getter para obtener los valores de los atributos privados.

    def get_id_historico(self):
        return self._id_historico

    def get_id_nomina(self):
        return self._id_nomina

    def get_año_mes(self):
        return self._año_mes

    def get_id_empleado(self):
        return self._id_empleado

    def get_nombre_empleado(self):
        return self._nombre_empleado

    def get_apellido_empleado(self):
        return self._apellido_empleado

    def get_id_contrato(self):
        return self._id_contrato

    def get_tipo_contrato(self):
        return self._tipo_contrato

    def get_salario(self):
        return self._salario

    def get_id_seguridad_social(self):
        return self._id_seguridad_social

    def get_salud_empleado(self):
        return self._salud_empleado

    def get_pension_empleado(self):
        return self._pension_empleado

    def get_total_prestaciones_empleado(self):
        return self._total_prestaciones_empleado

    def get_total_prestaciones_empresa(self):
        return self._total_prestaciones_empresa

    def get_valor_arl(self):
        return self._valor_arl

    def get_id_parafiscales(self):
        return self._id_parafiscales

    def get_total_parafiscales(self):
        return self._total_parafiscales

    def get_id_novedad(self):
        return self._id_novedad

    def get_id_tipo_novedad(self):
        return self._id_tipo_novedad

    def get_descripcion_novedad(self):
        return self._descripcion_novedad

    def get_fecha_novedad(self):
        return self._fecha_novedad

    def get_valor_novedad(self):
        return self._valor_novedad

    def get_id_tiempo_trabajado(self):
        return self._id_tiempo_trabajado

    def get_dias_pagados(self):
        return self._dias_pagados

    def get_horas_extras_diurnas(self):
        return self._horas_extras_diurnas

    def get_valor_extras_diurnas(self):
        return self._valor_extras_diurnas

    def get_horas_extras_nocturnas(self):
        return self._horas_extras_nocturnas

    def get_valor_extras_nocturnas(self):
        return self._valor_extras_nocturnas

    def get_horas_festivas(self):
        return self._horas_festivas

    def get_valor_festivos(self):
        return self._valor_festivos

    def get_horas_dominicales(self):
        return self._horas_dominicales

    def get_valor_horas_dominicales(self):
        return self._valor_horas_dominicales

    def get_cant_horas_deducidad(self):
        return self._cant_horas_deducidad

    def get_valor_deduccion_horas(self):
        return self._valor_deduccion_horas

    def get_total_devengo(self):
        return self._total_devengo

    def get_total_deducciones(self):
        return self._total_deducciones

    def get_total_sueldo(self):
        return self._total_sueldo

    # Métodos setter para establecer los valores de los atributos privados.

    def set_id_historico(self, id_historico):
        self._id_historico = id_historico

    def set_id_nomina(self, id_nomina):
        self._id_nomina = id_nomina

    def set_año_mes(self, año_mes):
        self._año_mes = año_mes

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def set_nombre_empleado(self, nombre_empleado):
        self._nombre_empleado = nombre_empleado

    def set_apellido_empleado(self, apellido_empleado):
        self._apellido_empleado = apellido_empleado

    def set_id_contrato(self, id_contrato):
        self._id_contrato = id_contrato

    def set_tipo_contrato(self, tipo_contrato):
        self._tipo_contrato = tipo_contrato

    def set_salario(self, salario):
        self._salario = salario

    def set_id_seguridad_social(self, id_seguridad_social):
        self._id_seguridad_social = id_seguridad_social

    def set_salud_empleado(self, salud_empleado):
        self._salud_empleado = salud_empleado

    def set_pension_empleado(self, pension_empleado):
        self._pension_empleado = pension_empleado

    def set_total_prestaciones_empleado(self, total_prestaciones_empleado):
        self._total_prestaciones_empleado = total_prestaciones_empleado

    def set_total_prestaciones_empresa(self, total_prestaciones_empresa):
        self._total_prestaciones_empresa = total_prestaciones_empresa

    def set_valor_arl(self, valor_arl):
        self._valor_arl = valor_arl

    def set_id_parafiscales(self, id_parafiscales):
        self._id_parafiscales = id_parafiscales

    def set_total_parafiscales(self, total_parafiscales):
        self._total_parafiscales = total_parafiscales

    def set_id_novedad(self, id_novedad):
        self._id_novedad = id_novedad

    def set_id_tipo_novedad(self, id_tipo_novedad):
        self._id_tipo_novedad = id_tipo_novedad

    def set_descripcion_novedad(self, descripcion_novedad):
        self._descripcion_novedad = descripcion_novedad

    def set_fecha_novedad(self, fecha_novedad):
        self._fecha_novedad = fecha_novedad

    def set_valor_novedad(self, valor_novedad):
        self._valor_novedad = valor_novedad

    def set_id_tiempo_trabajado(self, id_tiempo_trabajado):
        self._id_tiempo_trabajado = id_tiempo_trabajado

    def set_dias_pagados(self, dias_pagados):
        self._dias_pagados = dias_pagados

    def set_horas_extras_diurnas(self, horas_extras_diurnas):
        self._horas_extras_diurnas = horas_extras_diurnas

    def set_valor_extras_diurnas(self, valor_extras_diurnas):
        self._valor_extras_diurnas = valor_extras_diurnas

    def set_horas_extras_nocturnas(self, horas_extras_nocturnas):
        self._horas_extras_nocturnas = horas_extras_nocturnas

    def set_valor_extras_nocturnas(self, valor_extras_nocturnas):
        self._valor_extras_nocturnas = valor_extras_nocturnas

    def set_horas_festivas(self, horas_festivas):
        self._horas_festivas = horas_festivas

    def set_valor_festivos(self, valor_festivos):
        self._valor_festivos = valor_festivos

    def set_horas_dominicales(self, horas_dominicales):
        self._horas_dominicales = horas_dominicales

    def set_valor_horas_dominicales(self, valor_horas_dominicales):
        self._valor_horas_dominicales = valor_horas_dominicales

    def set_cant_horas_deducidad(self, cant_horas_deducidad):
        self._cant_horas_deducidad = cant_horas_deducidad

    def set_valor_deduccion_horas(self, valor_deduccion_horas):
        self._valor_deduccion_horas = valor_deduccion_horas

    def set_total_devengo(self, total_devengo):
        self._total_devengo = total_devengo

    def set_total_deducciones(self, total_deducciones):
        self._total_deducciones = total_deducciones

    def set_total_sueldo(self, total_sueldo):
        self._total_sueldo = total_sueldo

# Crear una instancia de la clase Historico
historico1 = Historico(
    id_historico=1,
    id_nomina=1,
    año_mes='2023-09-01',
    id_empleado=1,
    nombre_empleado='Juan',
    apellido_empleado='Perez',
    id_contrato=1,
    tipo_contrato='Contrato de tiempo completo',
    salario=2500.0,
    id_seguridad_social=1,
    salud_empleado=100.0,
    pension_empleado=120.0,
    total_prestaciones_empleado=350.0,
    total_prestaciones_empresa=400.0,
    valor_arl=25.0,
    id_parafiscales=1,
    total_parafiscales=50.0,
    id_novedad=1,
    id_tipo_novedad=1,
    descripcion_novedad='Novedad de salario',
    fecha_novedad='2023-09-15',
    valor_novedad=50.0,
    id_tiempo_trabajado=1,
    dias_pagados=30.0,
    horas_extras_diurnas=10.0,
    valor_extras_diurnas=50.0,
    horas_extras_nocturnas=5.0,
    valor_extras_nocturnas=30.0,
    horas_festivas=8.0,
    valor_festivos=40.0,
    horas_dominicales=4.0,
    valor_horas_dominicales=60.0,
    cant_horas_deducidad=2.0,
    valor_deduccion_horas=10.0,
    total_devengo=3000.0,
    total_deducciones=200.0,
    total_sueldo=2800.0
) 

# Ejemplo de uso de los métodos getter
print("Nombre del empleado:", historico1.get_nombre_empleado())
print("Salario:", historico1.get_salario())

# Ejemplo de uso de los métodos setter
historico1.set_salario(3000.0)
print("Nuevo salario:", historico1.get_salario())
