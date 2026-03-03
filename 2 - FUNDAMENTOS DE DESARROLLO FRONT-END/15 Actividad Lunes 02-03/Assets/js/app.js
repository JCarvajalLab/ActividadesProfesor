// app.js (jQuery)

$(function () {
    //=============================
    //1) Rereferencias jQuery DOM
    //=============================

    const $selProducto = $("#selProducto");
    const $txtPrecio = $("#txtPrecio");
    const $txtCantidad = $("#txtCantidad");
    const $chkFrecuente = $("#chkFrecuente");
    const $selPago = $("#selPago");
    const $btnCalcular = $("#btnCalcular");

    const $msg = $("#msg");

    const $spSubtotal = $("#spSubtotal");
    const $spDescuento = $("#spDescuento");
    const $spRecargo = $("#spRecargo");
    const $spIva = $("#spIva");
    const $spTotal = $("#spTotal");
    const $spResumen = $("#spResumen");

    console.log("jQuery conectado");

    // ========================
    // 2) Tabla de precios base
    // ========================

    const PRECIOS = {
        cafe: 1500,
        sandwich: 3500,
        jugo: 1200,
    };

    function autocompletarPrecio() {
        const producto = $selProducto.val();
        $txtPrecio.val(PRECIOS[producto]);
    }

    //==========================
    //3) Utilidades: validación
    //==========================

    function mostrarError(texto) {
        $msg.text(texto);
    }

    function limpiarError() {
        $msg.text("");
    }

    function leerNumero($input) {
        return Number($input.val());
    }

    function validarEntradas(precio, cantidad) {
        if (!Number.isFinite(precio) || precio <= 0) {
            mostrarError("Precio inválido. Debe ser mayor que 0.");
            return false;
        }

        if (!Number.isFinite(cantidad) || cantidad < 1) {
            mostrarError("Cantidad inválida. Debe ser 1 o más.");
            return false;
        }

        limpiarError();
        return true;
    }

    // =========================
    //4) Lógica de negocio
    //==========================
    function descuentoPorCantidad(cantidad) {
        // 1–2: 0% | 3–5: 5% | 6+: 10%
        if (cantidad >= 6) return 0.1;
        if (cantidad >= 3) return 0.05;
        return 0.0;
    }

    function recargoPorPago(metodo) {
        // tarjeta: 2% | efectivo: 0%
        if (metodo === "tarjeta") return 0.02;
        return 0.0;
    }

    function formatearCLP(valor) {
        return "$" + Math.round(valor).toLocaleString("es-CL");
    }

    function calcularTotales(precio, cantidad, esFrecuente, metodoPago) {
        const subtotal = precio * cantidad;

        const descCantidad = descuentoPorCantidad(cantidad);
        const descFrecuente = esFrecuente ? 0.03 : 0.0;
        const descPctTotal = descCantidad + descFrecuente;

        const descuento = subtotal * descPctTotal;

        const recPct = recargoPorPago(metodoPago);
        const recargo = subtotal * recPct;

        // Neto recomendado: subtotal - descuento + recargo
        const neto = subtotal - descuento + recargo;

        const iva = neto * 0.19;
        const total = neto + iva;

        return { subtotal, descuento, recargo, iva, total, descPctTotal, recPct };
    }

    // =========================
    // 5) Render UI
    // =========================
    function renderResultados(r) {
        $spSubtotal.text(formatearCLP(r.subtotal));
        $spDescuento.text(formatearCLP(r.descuento));
        $spRecargo.text(formatearCLP(r.recargo));
        $spIva.text(formatearCLP(r.iva));
        $spTotal.text(formatearCLP(r.total));
    }

    function construirResumen(productoNombre, cantidad, metodoPago, r) {
        return (
            `${productoNombre} x ${cantidad} | Pago: ${metodoPago} | ` +
            `Desc: ${(r.descPctTotal * 100).toFixed(0)}% | ` +
            `Rec: ${(r.recPct * 100).toFixed(0)}%`
        );
    }

    // =========================
    // 6) Acción principal
    // =========================
    function calcularYMostrar() {
        const precio = leerNumero($txtPrecio);
        const cantidad = leerNumero($txtCantidad);

        if (!validarEntradas(precio, cantidad)) return;

        const productoNombre = $selProducto.find(":selected").text();
        const esFrecuente = $chkFrecuente.is(":checked");
        const metodoPago = $selPago.val();

        const r = calcularTotales(precio, cantidad, esFrecuente, metodoPago);

        renderResultados(r);
        $spResumen.text(construirResumen(productoNombre, cantidad, metodoPago, r));
    }

    // =========================
    // 7) Recalculo inteligente
    // =========================
    function intentarRecalcular() {
        const precio = leerNumero($txtPrecio);
        const cantidad = leerNumero($txtCantidad);

        // Recalcula solo si ya hay datos válidos (evita NaN/errores)
        if (
            Number.isFinite(precio) &&
            precio > 0 &&
            Number.isFinite(cantidad) &&
            cantidad >= 1
        ) {
            calcularYMostrar();
        }
    }

    // =========================
    // 8) Eventos jQuery
    // =========================
    $selProducto.on("change", () => {
        autocompletarPrecio();
        intentarRecalcular();
    });

    $btnCalcular.on("click", calcularYMostrar);

    $txtCantidad.on("input", intentarRecalcular);
    $selPago.on("change", intentarRecalcular);
    $chkFrecuente.on("change", intentarRecalcular);

    // =========================
    // 9) Inicialización
    // =========================
    autocompletarPrecio();
    $spResumen.text("—");
});