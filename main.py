from ConvertirGradosSR_V1_1 import  ConversorAngulos

if __name__ == '__main__':
    # Ejemplo de uso
    angulo_grados = float(input("Ingrese el ángulo en grados: "))
    conversor = ConversorAngulos()
    angulo_radianes = conversor.grados_a_radianes(angulo_grados)
    print("El ángulo en radianes es: {:.2f}".format(angulo_radianes))

    angulo_radianes = float(input("Ingrese el ángulo en radianes: "))
    angulo_grados = conversor.radianes_a_grados(angulo_radianes)
    print("El ángulo en grados es: {:.2f}".format(angulo_grados))