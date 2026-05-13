# Inverse Magnetic Billiards

Repositorio para simular y visualizar billares magnéticos inversos en una mesa cuadrada permeable. La partícula cargada se mueve por arcos de circunferencia dentro y fuera del cuadrado; al cruzar la frontera cambia entre el campo magnético interior `Bin` y el campo exterior `Bout`.

El proyecto contiene dos configuraciones:

- `paralelo/`: campos magnéticos interior y exterior con orientación paralela.
- `antiparalelo/`: campos magnéticos interior y exterior con orientación antiparalela.

Además de las trayectorias, los scripts guardan datos del espacio de fases usando las coordenadas:

- `s`: posición sobre el borde del cuadrado.
- `theta`: ángulo de la velocidad respecto a la frontera.

## Estructura

```text
.
├── README.md
├── paralelo/
│   ├── magnetic.py              # Funciones geométricas y dinámicas del caso paralelo
│   ├── parallel.py              # Simulación principal con salida de trayectoria y espacio de fases
│   ├── figs_paralelo.py         # Figura de trayectoria para pocos rebotes
│   ├── gui_inverse_parallel.py  # Exploración interactiva con slider
│   ├── ejemplo_*.py             # Ejemplos de simulación
│   └── Bi1Bo2/, plotBonitos/    # Datos y figuras generadas para casos específicos
└── antiparalelo/
    ├── magnetic.py              # Funciones geométricas y dinámicas del caso antiparalelo
    ├── antiparallel.py          # Simulación principal del caso antiparalelo
    ├── antiparalelo_figs.py     # Figura de trayectoria para pocos rebotes
    ├── diferentesTrayectorias.py
    ├── generarVideo.py          # Genera cuadros y video a partir de trayectorias
    └── Bi1Bo2/                  # Datos y figuras generadas para casos específicos
```

## Requisitos

El código usa Python 3 con:

```bash
pip install numpy matplotlib
```

Para generar videos con `generarVideo.py` también se necesita `ffmpeg` instalado en el sistema.

## Uso rápido

Ejecuta los scripts desde su propia carpeta. Esto es importante porque varios archivos importan `magnetic.py` localmente y escriben las salidas en el directorio actual.

### Caso paralelo

```bash
cd paralelo
python3 parallel.py
```

Este script usa los parámetros definidos al inicio de `parallel.py`:

```python
Bin, Bout = 2, 1
vAngle = 100
x, y = 0.6, 0.0
```

Salidas principales:

- `trajectory_plot.png`: trayectoria de la partícula.
- `sdata.txt`: datos `(s, theta)` del espacio de fases.
- `phase_space.png`: gráfico del espacio de fases.

También puedes usar:

```bash
python3 figs_paralelo.py
python3 gui_inverse_parallel.py
```

`figs_paralelo.py` genera una figura de trayectoria con pocos pasos. `gui_inverse_parallel.py` abre una ventana interactiva de Matplotlib.

### Caso antiparalelo

```bash
cd antiparalelo
python3 antiparallel.py
```

Este script usa los parámetros definidos al inicio de `antiparallel.py`:

```python
Bin, Bout = 2, 1
x, y = 0.13, 0
vx, vy = cos(45°), sin(45°)
```

Salidas principales:

- `sdata.dat`: datos `(s, theta)` del espacio de fases.
- `unfolded.dat`: datos de la trayectoria desplegada.
- una ventana de Matplotlib con la trayectoria.

Para generar una figura más cuidada del caso antiparalelo:

```bash
python3 antiparalelo_figs.py
```

## Modificar parámetros

Los parámetros se editan directamente al inicio de cada script:

- `Bin`: campo magnético dentro del cuadrado.
- `Bout`: campo magnético fuera del cuadrado.
- `x, y`: posición inicial sobre la frontera.
- `vAngle` o `vx, vy`: dirección inicial de la velocidad.
- número de iteraciones del bucle `for`: cantidad de cruces/rebotes simulados.

Como los radios son `Rin = 1 / Bin` y `Rout = 1 / Bout`, evita usar campos iguales a cero.

## Datos generados

Los archivos `sdata.txt` y `sdata.dat` guardan dos columnas:

```text
s    theta
```

donde `s` recorre el perímetro del cuadrado y `theta` está en grados. Estos datos se usan para construir los diagramas de espacio de fases.

Algunos directorios como `Bi1Bo2/` y `plotBonitos/` guardan resultados ya generados para combinaciones específicas de campos, por ejemplo `Bin = 1`, `Bout = 2` o `Bin = 10`, `Bout = 1`.

## Notas de desarrollo

- `magnetic.py` contiene las funciones compartidas por los scripts de cada caso: cálculo de centros de circunferencia, intersecciones con la frontera, ángulos, distancia `s` y dibujo de arcos.
- Los casos paralelo y antiparalelo tienen versiones separadas de `magnetic.py` porque el sentido de giro fuera del billar cambia.
- Los scripts actuales están pensados para exploración numérica y generación de figuras; no son todavía una librería empaquetada.
