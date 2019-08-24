from Clase2.funciones import sumatoria
import datetime

dato_prueba = 1000000000
tiempo_inicial = datetime.datetime.now()
resultado = sumatoria(dato_prueba)
tiempo_final = datetime.datetime.now()
tiempo_total = tiempo_final - tiempo_inicial

print(f'Al algoritmo le tomo {tiempo_total} en ejecutar con el dato {dato_prueba} '
      f'el resultado obtenido es {resultado}')