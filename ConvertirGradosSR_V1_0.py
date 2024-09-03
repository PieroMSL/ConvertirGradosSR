import math

def grados_a_radianes(grados):
  """Convierte un ángulo de grados a radianes.

  Args:
    grados: El ángulo en grados.

  Returns:
    El ángulo en radianes.
  """
  radianes = grados * math.pi / 180
  return radianes

def radianes_a_grados(radianes):
  """Convierte un ángulo de radianes a grados.

  Args:
    radianes: El ángulo en radianes.

  Returns:
    El ángulo en grados.
  """
  grados = radianes * 180 / math.pi
  return grados

# Ejemplo de uso
angulo_grados = float(input("Ingrese el ángulo en grados: "))
angulo_radianes = grados_a_radianes(angulo_grados)
print("El ángulo en radianes es: {:.2f}".format(angulo_radianes))

angulo_radianes = float(input("Ingrese el ángulo en radianes: "))
angulo_grados = radianes_a_grados(angulo_radianes)
print("El ángulo en grados es: {:.2f}".format(angulo_grados))