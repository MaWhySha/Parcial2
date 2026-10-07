"""
Modelos del sistema de transporte (Escenario C).
Clase padre: ServicioTransporte
Clases hijas: Motocicleta, Automovil
"""


class ServicioTransporte:
    """Clase padre con los datos comunes a todo servicio de transporte."""

    def __init__(self, conductor, placa, distancia, tarifa_base):
        self.conductor = conductor
        self.placa = placa
        self.distancia = distancia      # en kilómetros
        self.tarifa_base = tarifa_base  # en dólares

    def obtener_tipo(self):
        return "Servicio genérico"

    def calcular_tarifa(self):
        # Comportamiento por defecto; cada clase hija lo sobrescribe.
        return self.tarifa_base

    def mostrar_resumen(self):
        # Este método es el mismo para todos, pero llama a métodos
        # sobrescritos: el resultado cambia según el tipo de objeto.
        return (
            f"Conductor: {self.conductor} | Placa: {self.placa}\n"
            f"Tipo: {self.obtener_tipo()} | Distancia: {self.distancia} km\n"
            f"Tarifa estimada: ${self.calcular_tarifa():.2f}"
        )


class Motocicleta(ServicioTransporte):
    FACTOR_KM = 0.35

    def obtener_tipo(self):
        return "Motocicleta"

    def calcular_tarifa(self):
        return self.tarifa_base + self.distancia * self.FACTOR_KM


class Automovil(ServicioTransporte):
    FACTOR_KM = 0.60

    def obtener_tipo(self):
        return "Automóvil"

    def calcular_tarifa(self):
        return self.tarifa_base + self.distancia * self.FACTOR_KM