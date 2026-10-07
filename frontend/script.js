// Mismas reglas que en Python (modelos.py) para que ambos den el mismo resultado.
class ServicioTransporte {
    constructor(distancia, tarifaBase) {
        this.distancia = distancia;
        this.tarifaBase = tarifaBase;
    }
    obtenerTipo() { return "Servicio genérico"; }
    calcularTarifa() { return this.tarifaBase; }
}

class Motocicleta extends ServicioTransporte {
    obtenerTipo() { return "Motocicleta"; }
    calcularTarifa() { return this.tarifaBase + this.distancia * 0.35; }
}

class Automovil extends ServicioTransporte {
    obtenerTipo() { return "Automóvil"; }
    calcularTarifa() { return this.tarifaBase + this.distancia * 0.60; }
}

const TARIFA_BASE_MOTO = 1.00;
const TARIFA_BASE_AUTO = 2.00;

const inputDistancia = document.getElementById("distancia");
const boton = document.getElementById("btn-calcular");
const cajaResultado = document.getElementById("resultado");
const cajaError = document.getElementById("error");

function crearServicio(tipo, distancia) {
    if (tipo === "moto") return new Motocicleta(distancia, TARIFA_BASE_MOTO);
    return new Automovil(distancia, TARIFA_BASE_AUTO);
}

function calcularEstimacion() {
    const tipo = document.querySelector('input[name="servicio"]:checked').value;
    const distancia = parseFloat(inputDistancia.value);

    cajaResultado.classList.add("oculto");
    cajaError.classList.add("oculto");

    if (isNaN(distancia) || distancia <= 0) {
        cajaError.textContent = "Ingresa una distancia mayor a 0 km.";
        cajaError.classList.remove("oculto");
        return;
    }

    const servicio = crearServicio(tipo, distancia);

    cajaResultado.className = "resultado " + tipo;
    cajaResultado.innerHTML = `
    <p>${servicio.obtenerTipo()} · ${distancia} km</p>
    <p class="monto">$${servicio.calcularTarifa().toFixed(2)}</p>
    <p>Tarifa base $${servicio.tarifaBase.toFixed(2)} + distancia × factor</p>
  `;
}

boton.addEventListener("click", calcularEstimacion);
inputDistancia.addEventListener("keydown", (e) => {
    if (e.key === "Enter") calcularEstimacion();
});