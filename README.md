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
## Instalación y uso en Arduino IDE.
Simplemente descarga *.zip e instalala en el IDE con: Sketch > Include Library > Add .ZIP library...

Ejemplo de uso:
```cpp
#include <Libreria_PID.h>

// Parámetros PID (ejemplo)
float Kp = 1.0;
float Ki = 0.5;
float Kd = 0.1;
float N = 10.0;
float dt = 0.01;  // 10 ms

// Creamos instancia de PID
FuncionesPID pid(Kp, Ki, Kd, N, dt);

// Variables de ejemplo
float setpoint = 100.0;  // referencia
float medida = 0.0;      // valor medido, podría venir de un sensor
float salida = 0.0;

unsigned long last_time;

void setup() {
  Serial.begin(115200);
  last_time = millis();
}

void loop() {
  unsigned long now = millis();
  if (now - last_time >= dt * 1000) {  // ejecutar cada dt segundos
    last_time = now;

    // Simular una medida (por ejemplo, la salida anterior)
    // Aquí puedes leer de un sensor real
    medida += 0.5;  // ejemplo: la medida cambia con el tiempo

    // Calcular salida PID usando método clásico
    salida = pid.PID(setpoint, medida);

    // Mostrar resultados
    Serial.print("SP: "); Serial.print(setpoint);
    Serial.print(" Medida: "); Serial.print(medida);
    Serial.print(" Salida PID: "); Serial.println(salida);

    // Aquí usarías 'salida' para controlar actuadores, motores, etc.
  }
}

```
