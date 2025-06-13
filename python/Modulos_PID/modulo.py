class Funciones_PID:
    """
    Controlador PID con varias implementaciones:
    - PID clasico
    - PID como filtro IIR
    - PID con filtro derivativo

    Parametros:
        Kp (float): Ganancia proporcional
        Ki (float): Ganancia integral
        Kd (float): Ganancia derivativa
        N (float): Factor de filtrado derivativo
        dt (float): Paso de tiempo (segundos)
    """
    def __init__(self,Kp,Ki,Kd,N,dt):
        # Constantes
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        self.N = N
        # Buffers
        self.error = [0,0,0]     # error -> [error pasado, error anterior , error actual]
        self.Derv_Buff = [0,0]
        self.fDerv_Buff = [0,0]
        # Inicializaciones necesarias
        self.Int = 0
        self.PI = 0



    def __ShiftErr__(self,SP,Medida):
        '''
        Metodo encapsulado para mover el buffer de error
        '''
        self.error = self.error[1:] + [SP-Medida]


    def PID(self,SP,Med):
        '''
        Iteracion de caluclo de salida PID
        '''
        self.__ShiftErr__(SP,Med)
        self.Int += self.error[2] * self.dt
        Der = (self.error[2] - self.error[1]) / self.dt
        u = self.Kp*self.error[2] + self.Ki*self.Int + self.Kd*Der
        return u


    def IIR(self,SP,Med):
        '''
        Iteracion de PID como filtro IIR
        '''
        A0 = self.Kp + self.Ki*self.dt + self.Kd/self.dt
        A1 = -self.Kp - 2*self.Kd/self.dt
        A2 = self.Kd/self.dt
        self.__ShiftErr__(SP,Med)
        u = A2*self.error[0] + A1*self.error[1] + A0*self.error[2]
        return u


    def PIDf(self,SP,Med):
        '''
        Iteracion de PID con filtro derivativo
        '''
        self.__ShiftErr__(SP,Med)
        # Accion proporcional-integral
        A0 = self.Kp + self.Ki*self.dt # K
        A1 = -self.Kp # K
        self.PI += A0 * self.error[2] + A1 * self.error[1]

        # Accion D Filtrada
        self.Derv_Buff[1] = self.Derv_Buff[0]
        A0d = self.Kd / self.dt # K
        A1d  = -2*A0d # K
        self.Derv_Buff[0] = A0d * self.error[2] + A1d * self.error[1] + A0d * self.error[0]

        self.fDerv_Buff[1] = self.fDerv_Buff[0]
        tau = self.Kd / (self.Kp*self.N) # K
        Alfa = self.dt / (2*tau+1e-6) # K
        Alfa_1 = Alfa / (Alfa+1) # K
        Alfa_2 = (Alfa-1) / (Alfa+1) # K
        self.fDerv_Buff[0] = Alfa_1 * (self.Derv_Buff[0] + self.Derv_Buff[1]) - Alfa_2 * self.fDerv_Buff[1]
        # Retornamos el resultado
        u = self.PI + self.fDerv_Buff[0]
        return u