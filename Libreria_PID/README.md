## Instalacion y uso en Arduino IDE.
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