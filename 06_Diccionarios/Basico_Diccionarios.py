# Un diccionario es mas o menos una lista pero no tiene indices sino que se guarda por key, value donde key es como se llama el espacio de la memoria y value es el valor que se guarda en ese lugar

# Sintaxis de un diccionario estos pueden contener cualquier tipo de dato por ejemplo los mas normales (str, int, bool) y tambien los complejos (listas[], tuplas(), diccionarios{})
persona = {
    "nombre" : "Jesus",
    "apellido" : "Rodriguez",
    "altura" : 1.75,
    "sexo" : "Hombre",
    "vivo" : True
}

# Asi se accede a algun elemento de el diccionario
print(f"El nombre guardado en persona es: {persona["nombre"]}")