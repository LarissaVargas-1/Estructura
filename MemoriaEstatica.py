# Simulación del comportamiento de memoria estática en Python

# Reservamos exactamente 5 espacios en memoria inicializados en 0
calificaciones = [0] * 5  

print("--- Memoria Estática (Simulación) ---")
for i in range(5):
    # En Java se usa JOptionPane para capturar y se convierte con Integer.parseInt()
    # En Python capturamos con input() y convertimos directamente usando int()
    entrada = input(f"Capture la calificación para la posición {i}: ")
    calificaciones[i] = int(entrada)

# Al terminar el ciclo, la memoria estática simulada no puede crecer más
print("\nCalificaciones almacenadas de forma fija:")
print(calificaciones)