"""
Programa principal: crea varios servicios y los procesa
desde una misma colección usando polimorfismo.
"""
from modelos import Motocicleta, Automovil

# Tarifas base (las mismas que usa el frontend en script.js)
TARIFA_BASE_MOTO = 1.00
TARIFA_BASE_AUTO = 2.00


def main():
    servicios = [
        Motocicleta("Carlos Pérez", "MOT-123", 5, TARIFA_BASE_MOTO),
        Automovil("Ana Torres", "ABC-4567", 8, TARIFA_BASE_AUTO),
        Motocicleta("Luis Mendoza", "MOT-456", 12.5, TARIFA_BASE_MOTO),
        Automovil("María López", "XYZ-8910", 3, TARIFA_BASE_AUTO),
    ]

    print("=== Servicios de transporte ===\n")
    total = 0
    for servicio in servicios:
        # Misma llamada para todos; cada objeto responde según su clase.
        print(servicio.mostrar_resumen())
        print("-" * 45)
        total += servicio.calcular_tarifa()

    print(f"Total de los {len(servicios)} servicios: ${total:.2f}")


if __name__ == "__main__":
    main()