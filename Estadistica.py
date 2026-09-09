import random
import statistics

# 1. Generar 50 números aleatorios entre 1 y 100
# (Nota: Cada vez que corras el programa, los números cambiarán)
datos = [random.randint(150, 250) for _ in range(50)]

# 2. Realizar los cálculos estadísticos
media = statistics.mean(datos)
mediana = statistics.median(datos)
varianza = statistics.variance(datos)     # Varianza muestral
desviacion = statistics.stdev(datos)       # Desviación estándar muestral

# La moda puede fallar si todos los números se repiten las mismas veces
try:
    moda = statistics.mode(datos)
except statistics.StatisticsError:
    moda = "No hay una moda única"

# 3. Mostrar los resultados en consola
print("=== DATOS GENERADOS ===")
print(datos)
print("\n=== ANÁLISIS ESTADÍSTICO ===")
print(f"Media:              {media:.2f}")
print(f"Mediana:            {mediana:.2f}")
print(f"Moda:               {moda}")
print(f"Varianza:           {varianza:.2f}")
print(f"Desviación Estándar: {desviacion:.2f}")
