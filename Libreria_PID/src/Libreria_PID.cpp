#include "Libreria_PID.h"

FuncionesPID::FuncionesPID(float kp, float ki, float kd, float n, float dt_s) {
  Kp = kp;
  Ki = ki;
  Kd = kd;
  N = n;
  dt = dt_s;
  for (int i = 0; i < 3; i++) error[i] = 0.0;
  for (int i = 0; i < 2; i++) {
    Derv_Buff[i] = 0.0;
    fDerv_Buff[i] = 0.0;
  }
  Int = 0.0;
  PI = 0.0;
}

void FuncionesPID::shiftError(float SP, float Med) {
  error[0] = error[1];
  error[1] = error[2];
  error[2] = SP - Med;
}

float FuncionesPID::PID(float SP, float Med) {
  shiftError(SP, Med);
  Int += error[2] * dt;
  float Der = (error[2] - error[1]) / dt;
  return Kp * error[2] + Ki * Int + Kd * Der;
}

float FuncionesPID::IIR(float SP, float Med) {
  shiftError(SP, Med);
  float A0 = Kp + Ki * dt + Kd / dt;
  float A1 = -Kp - 2 * Kd / dt;
  float A2 = Kd / dt;
  return A2 * error[0] + A1 * error[1] + A0 * error[2];
}

float FuncionesPID::PIDf(float SP, float Med) {
  shiftError(SP, Med);

  float A0 = Kp + Ki * dt;
  float A1 = -Kp;
  PI += A0 * error[2] + A1 * error[1];

  Derv_Buff[1] = Derv_Buff[0];
  float A0d = Kd / dt;
  float A1d = -2 * A0d;
  Derv_Buff[0] = A0d * error[2] + A1d * error[1] + A0d * error[0];

  fDerv_Buff[1] = fDerv_Buff[0];
  float tau = Kd / (Kp * N);
  float Alfa = dt / (2 * tau + 1e-6);
  float Alfa_1 = Alfa / (Alfa + 1);
  float Alfa_2 = (Alfa - 1) / (Alfa + 1);
  fDerv_Buff[0] = Alfa_1 * (Derv_Buff[0] + Derv_Buff[1]) - Alfa_2 * fDerv_Buff[1];

  return PI + fDerv_Buff[0];
}
