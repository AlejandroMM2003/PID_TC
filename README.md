# Funciones y métodos PID para Arduino y Micropython.
---
## Instalación y uso en Micropython.
Para la instalacion usamos el siguiente programa:
```python
import micropip

async def instalar():
    await micropip.install("git+https://github.com/AlejandroMM2003/PID_TC.git@main#subdirectory=python")
    import Modulo_PID

await instalar()
```
Este archivo incluye un objeto tipo Funciones_PID() con 3 metodos correspondientes a los 3 PID's propuestos.
En cada iteracion de bucle se hace una llamada a uno de los 3 metodos para calcular una salida en base a los datos proporcionados al constructor.
```python
import Modulo_PID

Kp = 2
Ki = 0.25
Kd = 20
N = 6
dt = 1e-3

Setpoint = 1

Controlador = Funciones_PID(Kp,Ki,Kd,N,dt)

while True:
    Medida = LeerDatos()
    Salida = Controlador.PIDf(Setpoint,Medida)
```
---
