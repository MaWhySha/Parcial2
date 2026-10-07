# Sistema de Transporte – Escenario C

**Equipo:** Grupo 6

**Integrantes:**
- Robin Christopher Barrera Vasquéz
- Alexis Omar García Romero
- Daniela Ester López Varela
- Liliana Dalila Ulloa González
- Carlos Fernando Guardado García

**Escenario seleccionado:** C – Sistema de transporte (nivel avanzado)

## Descripción de la solución

Prototipo para estimar el costo de un viaje según el tipo de vehículo y la distancia.
La parte en **Python** modela los servicios con herencia y polimorfismo, y la parte
**frontend** (HTML, CSS y JavaScript) permite al usuario elegir el servicio, ingresar
la distancia y ver la estimación. Ambas partes usan las mismas reglas de tarifa:

| Servicio    | Tarifa base | Fórmula                          |
|-------------|-------------|----------------------------------|
| Motocicleta | $1.00       | tarifa base + distancia × 0.35   |
| Automóvil   | $2.00       | tarifa base + distancia × 0.60   |

## Cómo ejecutar

**Python:**
```bash
cd python
python main.py
```

**Frontend:** abrir `frontend/index.html` en el navegador.

## Programación orientada a objetos

- **Clase padre:** `ServicioTransporte`, con los atributos comunes `conductor`, `placa`,
  `distancia` y `tarifa_base`, y los métodos `obtener_tipo()`, `calcular_tarifa()` y
  `mostrar_resumen()`.
- **Clases hijas:** `Motocicleta` y `Automovil`. Heredan los atributos y `mostrar_resumen()`
  de la clase padre sin repetir código.
- **Métodos sobrescritos:** `calcular_tarifa()` (cada hija aplica su propio factor por km)
  y `obtener_tipo()` (cada hija devuelve su nombre).
- **Polimorfismo:** en `main.py` se guardan motocicletas y automóviles en una misma lista
  y se recorren con un solo ciclo `for`, llamando a `mostrar_resumen()` y
  `calcular_tarifa()` sin preguntar de qué tipo es cada objeto. Cada objeto responde
  según su propia clase, por eso la misma llamada produce tarifas diferentes.

## Función de HTML, CSS y JavaScript

- **HTML:** define la estructura con etiquetas semánticas (`header`, `main`, `section`,
  `footer`), las opciones de servicio, el campo de distancia y el botón
  "Calcular estimación".
- **CSS:** da la presentación y diferencia visualmente los servicios
  (verde azulado para Motocicleta, azul para Automóvil), además de adaptar la página a
  pantallas pequeñas.
- **JavaScript:** captura el clic del botón, valida la distancia, calcula la tarifa con
  las mismas reglas de Python (usando clases equivalentes) y muestra el resultado o un
  mensaje de error.

## Responsabilidades de frontend y backend

**Frontend (lo que ve y usa el usuario):**
- Mostrar las opciones de servicio y el formulario.
- Capturar los datos que ingresa el usuario.
- Validaciones básicas (que la distancia sea un número mayor a 0).
- Mostrar el resultado de forma clara.

**Backend (lo que se haría en el servidor en una aplicación real):**
- Contener la lógica oficial de cálculo de tarifas (las clases de Python).
- Validar de nuevo los datos, ya que el frontend puede ser manipulado.
- Asignar un conductor y vehículo disponible.
- Guardar los viajes en una base de datos.
- Devolver la respuesta al frontend.

> En este proyecto el frontend calcula la tarifa por su cuenta para la demostración,
> pero en una aplicación real ese cálculo lo haría el backend para que el precio no
> pueda ser alterado desde el navegador.

## Flujo Usuario → Frontend → Backend → Respuesta → Frontend

1. **Usuario:** elige "Automóvil", escribe 8 km y presiona "Calcular estimación".
2. **Frontend:** valida la distancia y envía una petición al backend, por ejemplo
   `POST /api/estimacion` con estos datos:
   ```json
   { "tipo_servicio": "automovil", "distancia_km": 8 }
   ```
3. **Backend:** recibe la petición, valida los datos, crea el objeto correspondiente
   (`Automovil`) y llama a `calcular_tarifa()`. Gracias al polimorfismo no necesita
   saber cómo calcula cada tipo; solo llama al método.
4. **Respuesta:** el backend devuelve el resultado, por ejemplo:
   ```json
   {
     "tipo_servicio": "Automóvil",
     "distancia_km": 8,
     "tarifa_base": 2.00,
     "tarifa_estimada": 6.80,
     "conductor_asignado": "Ana Torres",
     "placa": "ABC-4567"
   }
   ```
   Si los datos fueran inválidos, respondería con un error, por ejemplo
   `{ "error": "La distancia debe ser mayor a 0" }`.
5. **Frontend:** recibe la respuesta y la muestra al usuario (tipo de servicio,
   distancia, tarifa y conductor), o el mensaje de error si lo hubo.

## Estructura del repositorio

```
proyecto-parcial/
├── python/
│   ├── modelos.py
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md
```