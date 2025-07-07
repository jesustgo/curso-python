# Un diccionario es mas o menos una lista pero no tiene indices sino que se guarda por key, value donde key es como se llama el espacio de la memoria y value es el valor que se guarda en ese lugar

# Sintaxis de un diccionario estos pueden contener cualquier tipo de dato por ejemplo los mas normales (str, int, bool) y tambien los complejos (listas[], tuplas(), diccionarios{})

# Las keys pueden ser tuplas, int, str pero no pueden ser listas ni sets
persona = {
    "nombre": "Jesus",
    "apellido" : "Rodriguez",
    "altura" : 1.75,
    "sexo" : "Hombre",
    "vivo" : True
}

# Asi se accede a algun elemento de el diccionario
print(f"El nombre guardado en persona es: {persona["nombre"]}")

# Metodo .keys sirve para devolver un iterable con las keys del diccionario
print(persona.keys())

# Metodo .get sirve para mostrar el value de una key que se le va a pasar como parametro ademas de que se usa para evitar errores en caso de que se le pase una key que no este dentro del diccionario
print(persona.get("nombre"))

# Metodo .clear sirve para eliminar todos los elementos del diccionario
# print(persona.clear())

# Metodo .pop sirve para eliminar un solo elemento y lo devuelve
print(f"El dato que usamos en el pop: {persona.pop("apellido")} y asi queda el diccionario {persona}")

# Metodo .items sirve para devolver un diccionario(keys, values) iterable
print(persona.items()) 

# Metodo .values sirve para devolver un iterable con los values del diccionario
print(persona.values())