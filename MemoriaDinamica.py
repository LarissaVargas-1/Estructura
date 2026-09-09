# Demostración de memoria dinámica en Python utilizando listas nativas

# Creamos una lista vacía, sin necesidad de definir un tamaño inicial
frutas = []  

# Agregamos elementos de forma dinámica usando append() (equivalente a .add())
frutas.append("mango")
frutas.append("manzana")
frutas.append("donada") 
frutas.append("uvas")   
print("Contenido inicial de la lista dinámica:")
print(frutas)

# Eliminamos elementos dinámicamente usando pop() (equivalente a .remove())
# Al eliminar el índice 0 ("mango"), los índices del resto de elementos se recorren automáticamente.
frutas.pop(0)  # Elimina "mango" (índice 0)
frutas.pop(1)  # Elimina "donada" (que pasó al índice 1 tras borrar "mango")

# Agregamos un nuevo elemento que expande la memoria nuevamente
frutas.append("sandía")

print("\nContenido final tras modificar la lista:")
print(frutas)