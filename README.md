# Funciones y métodos PID

Librería y módulo de métodos PID para Arduino y Micropython respectivamente.
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
---
