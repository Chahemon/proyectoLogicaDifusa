import base_logica
from humedad import *
from temperatura import *
from base_logica import *

humedad_valor = float( input("Ingrese la humedad: " ) )
temperatura_valor = float( input("Ingrese la Temperatura: ") )

humedad_obj = Humedad(humedad_valor)
temperatura_obj = Temperatura(temperatura_valor)

print(humedad_obj.seco, humedad_obj.humedo, humedad_obj.muy_humedo)
print(temperatura_obj.tem_muy_baja, temperatura_obj.tem_fria, temperatura_obj.templado, temperatura_obj.tem_caliente, temperatura_obj.tem_muy_caliente)

resultado_humedad = base_logica.humedad_num_string(humedad_obj.seco, humedad_obj.humedo, humedad_obj.muy_humedo)
resultado_temperatura = base_logica.temperatura_num_string(temperatura_obj.tem_muy_baja, temperatura_obj.tem_fria, temperatura_obj.templado, temperatura_obj.tem_caliente, temperatura_obj.tem_muy_caliente)

resultado_parcial = (base_logica.determinar_regla(resultado_humedad, resultado_temperatura))

for regla in resultado_parcial:
    print(regla)