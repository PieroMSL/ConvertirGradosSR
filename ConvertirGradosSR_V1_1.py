import math

class ConversorAngulos:
    @staticmethod
    def grados_a_radianes(grados):
        """Convierte un ángulo de grados a radianes."""
        return grados * math.pi / 180

    @staticmethod
    def radianes_a_grados(radianes):
        """Convierte un ángulo de radianes a grados."""
        return radianes * 180 / math.pi