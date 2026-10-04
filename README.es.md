# Diapositivas de Python Brasil 2026 en Markdown

[Português](README.md) · [English](README.en.md) · Español

Escribe el contenido de tu charla para [Python Brasil 2026](https://2026.pythonbrasil.org.br/) a tu manera, en Markdown puro, y deja que un agente de IA se encargue de la forma. Tu agente favorito lee el [`AGENTS.md`](AGENTS.md) y da formato a las diapositivas con los diseños, los colores y las reglas de la marca. Con cada push, la presentación se publica en GitHub Pages, junto con un PDF.

Los bloques de código se colorean solos. Escribe ` ```python ` y el código, y el tema aplica los colores de Monokai en una tarjeta oscura, con la fuente Cascadia Mono, tanto en las diapositivas oscuras como en las claras. No hace falta copiar el código de otro sitio ni pegar una imagen.

![Diapositiva de código: una dataclass Palestra con resaltado de sintaxis Monokai en una tarjeta oscura, con el sticker del mago al lado](docs/codigo.png)

El tema usa [Marp](https://marp.app/) y la identidad visual del evento: colores, fuentes, logo y stickers.

¿Prefieres PowerPoint, LibreOffice o Google Slides? Usa la [plantilla en `.pptx`](https://github.com/rodbv/pybr2026-slides), que está en portugués.

Las diapositivas de ejemplo existen en tres idiomas, con los mismos consejos:

| Idioma | Archivo | Ver |
|---|---|---|
| Português | `slides.md` | [en el navegador](https://rodbv.github.io/pybr2026-marp/) · [PDF](https://rodbv.github.io/pybr2026-marp/slides.pdf) |
| English | `slides.en.md` | [en el navegador](https://rodbv.github.io/pybr2026-marp/en.html) · [PDF](https://rodbv.github.io/pybr2026-marp/slides.en.pdf) |
| Español | `slides.es.md` | [en el navegador](https://rodbv.github.io/pybr2026-marp/es.html) · [PDF](https://rodbv.github.io/pybr2026-marp/slides.es.pdf) |

![Las 39 diapositivas de ejemplo, en las versiones oscura y clara](docs/overview.png)

## Para empezar

1. Haz clic en **Use this template > Create a new repository**.
2. En el repositorio nuevo, abre **Settings > Pages** y elige **GitHub Actions** en **Source**. La copia ejecuta la Action una vez al crearse, antes de activar Pages, y esa primera ejecución falla. El siguiente push publica con normalidad.
3. Si tu charla es en español, edita `slides.es.md`. Si quieres, borra los archivos de los otros idiomas (`slides.md` y `slides.en.md`). Con cada push a `main`, la Action publica cada archivo con su PDF: el español en `https://TU-USUARIO.github.io/NOMBRE-DEL-REPOSITORIO/es.html`, el portugués (`slides.md`) en la raíz y el inglés en `.../en.html`.

Esa dirección sirve para el código QR del cierre: el público abre tus diapositivas en el celular.

Las cajas grises de las diapositivas de ejemplo marcan el lugar de las imágenes y muestran el tamaño que llena el espacio. Cambia la ruta de la imagen en el Markdown por la tuya.

La plantilla es un punto de partida: cambia lo que quieras. Para mantener el estilo del evento, usa los colores y las fuentes de la marca, que están en [`AGENTS.md`](AGENTS.md#regras-da-marca).

## Con un agente de IA

El contenido es tuyo: escribe el guion de tu charla en un archivo, en viñetas, como borrador o en texto corrido. Después, abre el repositorio en tu editor con el agente y pide la forma. Por ejemplo:

```
Mi guion está en guion.md. Arma las diapositivas en slides.es.md, en lugar de
los ejemplos, con los diseños y los colores de la plantilla: portada, agenda,
una sección para cada parte y el cierre. Una idea por diapositiva, el código en
bloques con resaltado, y lo que voy a decir en las notas. No inventes
contenido: si falta algo, pregúntame.
```

El `AGENTS.md` le dice al agente qué diseños existen, cómo escribir cada uno y cuáles son las reglas de la marca y del contenido: hasta 8 líneas de código por diapositiva, texto alternativo en cada imagen, lima como color de texto solo en el fondo oscuro, lenguaje neutro en cuanto al género. El `CLAUDE.md` apunta al mismo archivo.

Después, pide ajustes como se los pedirías a una persona: "divide la diapositiva 7 en dos", "cambia la tabla por un flujo", "acorta las notas".

## En VS Code

1. Abre la carpeta del repositorio. VS Code sugiere la extensión **Marp for VS Code**: instálala.
2. Abre `slides.es.md` y haz clic en el botón de vista previa, en la esquina superior. El tema ya viene configurado.
3. Para exportar, usa **Marp: Export Slide Deck** en la paleta de comandos y elige HTML, PDF o PPTX. El PDF y el PPTX necesitan Chrome, Edge o Firefox instalado.

También puedes editar `slides.es.md` directamente en GitHub, desde el navegador: la Action publica igual.

## Presentar

Abre la dirección de GitHub Pages o el HTML exportado en el navegador.

- **F**: pantalla completa.
- **P**: abre la vista del presentador en una ventana nueva, con las notas, la siguiente diapositiva y el cronómetro. Las dos ventanas avanzan juntas: deja la del presentador en tu pantalla y la de las diapositivas en el proyector. Para salir, cierra la ventana del presentador.
- Flechas o barra espaciadora: siguiente diapositiva.

Lleva también el PDF en una memoria USB: se abre en cualquier computadora, sin internet.

## Diseños

Cada diapositiva elige su diseño con un comentario al inicio, como `<!-- _class: secao -->`. Los ejemplos de `slides.es.md` los muestran todos, y el [`AGENTS.md`](AGENTS.md) trae el Markdown que espera cada uno. Los nombres de las clases están en portugués y no cambian según el idioma.

| Clase | Para |
|---|---|
| (ninguna) | Título y puntos, tabla, código o imagen |
| `capa` | Título de la charla, nombre y el sello con la fecha |
| `frase` | Una sola frase, grande |
| `secao` | Separador con el número en el disco lima |
| `duas-colunas` | Antes y después, problema y solución, dos fragmentos de código |
| `numeros` | Tres números grandes con etiqueta |
| `cartoes` | Tres bloques numerados con título y descripción |
| `fluxo` | Pasos en cajas unidas por flechas |
| `tres-imagens` | Tres capturas de pantalla con leyenda |
| `palestrante` | Foto, nombre, cargo y tres datos |
| `destaque` | Panel lima con el mensaje que la sala no puede perderse |
| `imagem-cheia` | Foto de fondo con franja de leyenda |
| `encerramento` | "¿Preguntas?" o "¡Gracias!", contactos y código QR |
| `figurinhas` | Logo, stickers, círculo pixelado y resaltador |
| `light` | Versión clara de cualquier diseño: `<!-- _class: frase light -->` |

Para poner texto al lado de una imagen, usa la sintaxis de Marp: `![bg right:42%](img/foto.png)`.

## Gráfico y código QR

Marp no tiene gráficos nativos. Los scripts de `scripts/` generan las imágenes con los colores de la marca, con [uv](https://docs.astral.sh/uv/):

```sh
uv run scripts/qr.py https://seu-usuario.github.io/sua-palestra/
uv run scripts/grafico.py
```

`qr.py` reemplaza `img/qr.png`. `grafico.py` genera el gráfico de ejemplo con matplotlib, al estilo del tema: cambia las etiquetas y los valores en el script y ejecútalo de nuevo.

## Accesibilidad

- El texto del cuerpo mide 36 px en una diapositiva de 1280 px, lo mismo que 20 pt en la plantilla `.pptx`. Nada por debajo de 18 pt, para quien se sienta lejos.
- Todas las combinaciones de colores del tema cumplen el nivel AA de WCAG 2.1. Los colores y el contraste de cada uno están en el [README de la plantilla `.pptx`](https://github.com/rodbv/pybr2026-slides#cores-e-contraste), en portugués.
- El idioma de cada documento está declarado en `lang:` (`es` en `slides.es.md`), para los lectores de pantalla.
- Escribe el texto alternativo entre los corchetes de cada imagen: `![Gráfico de barras: ...](img/grafico.png)`.

## ¿Encontraste un problema?

Abre un [issue en GitHub](https://github.com/rodbv/pybr2026-marp/issues) que cuente qué pasó y, si puedes, con una captura de pantalla.

## Licencias

- Plantilla, textos de ejemplo y código de este repositorio: [CC0 1.0](LICENSE) (dominio público). Úsalos, cámbialos y compártelos sin pedir permiso ni dar crédito.
- Logo, stickers e identidad visual: Python Brasil 2026 y APyB, del brandboard oficial del evento, creado por [Ana Terhorst](https://anaterhorstdesign.com).
- Fuentes Roboto y Cascadia Mono: SIL Open Font License 1.1, cargadas desde Google Fonts.
