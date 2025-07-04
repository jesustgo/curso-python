list_origin = [1,2,3]
list_copy1 = list_origin[:]
list_copy2 = list_origin.copy()
referencia = list_origin
referencia[0] = 10

print(f"Esta es la lista original: {list_origin}")
print(f"Esta es la copia con slicing: {list_copy1}")
print(f"Esta es la lista con copy: {list_copy2}")
print(f"Esta es la referencia de la lista original: {referencia}")