import re

def tiene_caracter_repetido(texto):
  """
  Verifica si una cadena contiene caracteres repetidos utilizando expresiones regulares.

  Args:
    texto: La cadena a verificar.

  Returns:
    True si la cadena contiene caracteres repetidos, False en caso contrario.
  """
  patron = r"(.)\1+"
  return bool(re.search(patron, texto))

# Ejemplos de uso
cadena1 = "hola mundo"
cadena2 = "abbbac"
cadena3 = "abcd"

print(f'"{cadena1}" tiene caracteres repetidos: {tiene_caracter_repetido(cadena1)}')
print(f'"{cadena2}" tiene caracteres repetidos: {tiene_caracter_repetido(cadena2)}')
print(f'"{cadena3}" tiene caracteres repetidos: {tiene_caracter_repetido(cadena3)}')