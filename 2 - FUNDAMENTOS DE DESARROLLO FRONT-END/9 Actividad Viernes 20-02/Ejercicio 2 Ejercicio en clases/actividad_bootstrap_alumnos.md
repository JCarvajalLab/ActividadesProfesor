
---

Objetivo

Construir una página HTML que:

* Incorpore Bootstrap vía CDN
* Utilice container
* Use sistema de grilla básico
* Cree una tabla con estilos Bootstrap
* Aplique clases contextuales
* Sea responsive con `.table-responsive`

---

ETAPA 1 — Crear el archivo base (10 min)

Paso 1

Crear archivo:

laboratorio_bootstrap.html

Copiar estructura mínima:

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Laboratorio Bootstrap</title>
</head>
<body>

</body>
</html>
```

Explicación

* `<!doctype html>` define que el documento utiliza HTML5.
* `<meta name="viewport">` permite que el diseño sea adaptable a distintos tamaños de pantalla.
* Sin viewport, Bootstrap no aplica correctamente su comportamiento responsivo.

Verificación

Abrir en navegador.
Debe verse una página en blanco sin errores.

---

ETAPA 2 — Incorporar Bootstrap (10 min)

Dentro del `<head>` agregar:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet">
```

Explicación

CDN significa Content Delivery Network.
Bootstrap se carga desde un servidor externo sin necesidad de descargar archivos localmente.

Verificación

1. Abrir F12
2. Ir a la pestaña Network
3. Recargar la página
4. Verificar que bootstrap.min.css se cargue correctamente

---

ETAPA 3 — Container + Grid básico (15 min)

Dentro del `<body>` escribir:

```html
<div class="container mt-5">

  <div class="row">
    <div class="col">
      <h1 class="text-center">Inventario de Productos</h1>
      <p class="text-center">Laboratorio Bootstrap</p>
    </div>
  </div>

</div>
```

Explicación

* `container` centra el contenido y define un ancho máximo.
* `mt-5` agrega margen superior.
* `row` representa una fila dentro del sistema de 12 columnas.
* `col` ocupa el ancho disponible dentro de la fila.
* `text-center` centra el texto horizontalmente.

Verificación

Reducir el ancho de la ventana.
El contenido debe mantenerse centrado.

---

ETAPA 4 — Agregar tabla básica (20 min)

Debajo del primer row agregar:

```html
<div class="row mt-4">
  <div class="col">

    <table class="table">
      <thead>
        <tr>
          <th>Producto</th>
          <th>Cantidad</th>
          <th>Precio</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Ratón</td>
          <td>15</td>
          <td>$100</td>
        </tr>
        <tr>
          <td>Teclado</td>
          <td>34</td>
          <td>$340</td>
        </tr>
      </tbody>
    </table>

  </div>
</div>
```

Explicación

La clase `.table` aplica estilos base a la tabla:

* Espaciado interno (padding).
* Líneas horizontales.
* Formato visual estándar Bootstrap.

Verificación

Comparar la tabla con y sin la clase `table`.
Deben notar diferencias visuales claras.

---

ETAPA 5 — Mejorar la tabla (15 min)

Modificar la etiqueta `<table>` a:

```html
<table class="table table-striped table-bordered table-hover">
```

Explicación

* `table-striped` agrega filas alternadas.
* `table-bordered` agrega bordes completos.
* `table-hover` aplica efecto visual al pasar el mouse.

Verificación

Pasar el cursor sobre las filas.
Debe observarse el efecto hover.

---

ETAPA 6 — Clases contextuales (10 min)

Modificar las filas:

```html
<tr class="table-warning">
```

```html
<tr class="table-primary">
```

Explicación

Las clases contextuales aplican significado visual:

* `table-primary`: acción importante.
* `table-warning`: advertencia.
* `table-danger`: situación crítica.
* `table-success`: acción correcta.

No es solo estética; comunica intención.

Verificación

Las filas deben cambiar de color automáticamente.

---

ETAPA 7 — Tabla Responsive (10 min)

Encerrar la tabla en:

```html
<div class="table-responsive">
  <!-- tabla aquí -->
</div>
```

Explicación

`.table-responsive` permite desplazamiento horizontal en pantallas pequeñas, evitando que la tabla se desborde.

Verificación

1. Abrir F12
2. Activar modo móvil
3. Reducir el ancho
4. Verificar que aparezca scroll horizontal

---

Cierre conceptual

Preguntas de reflexión:

1. ¿Qué hace `container`?
2. ¿Qué significa que la grilla sea de 12 columnas?
3. ¿Qué diferencia hay entre `table` y `table-striped`?
4. ¿Para qué sirve `table-responsive`?
5. ¿Bootstrap reemplaza CSS?


respuestas
1. El container encierra el contenido en el centro de la pantalla y le da un ancho maximo con margenes automaticos
2. Que la pagina se divide en 12 partes y se pueden combinar para organizar
3. table entrega un estilo basico y  table-striped agrega a las filas colores alternados
4. permite que la tabla se pueda desplazar en pantallas mas pequeñas 
5. no, boostrap entrega una base la cual facilita el desarrollo de la interfaz y el css podemos mejorar aun mas esta interfaz