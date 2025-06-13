#ifndef LIBRERIA_PID_H
#define LIBRERIA_PID_H

#include <Arduino.h>

class FuncionesPID {
  public:
    // Constantes PID
    float Kp, Ki, Kd, dt, N;

    // Buffers
    float error[3];
    float Derv_Buff[2];
    float fDerv_Buff[2];
    float Int;
    float PI;

    // Constructor
    FuncionesPID(float kp, float ki, float kd, float n, float dt_s);

    // Métodos PID
    void shiftError(float SP, float Med);
    float PID(float SP, float Med);
    float IIR(float SP, float Med);
    float PIDf(float SP, float Med);
};

#endif
