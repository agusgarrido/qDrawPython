def ComentarioEnPantalla(comentario):
    print(comentario)


class QDraw:
    def __init__(self):
        self.filas = 0
        self.columnas = 0
        self.tablero = []
        self.posActualX = 0
        self.posActualY = 0

    def CrearTablero(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        for i in range(self.filas):
            self.tablero.append(["-"] * self.columnas)

    def DibujarTablero(self):
        # Recorro de forma inversa para que el origen sea la esquina inferior izquierda
        for fila in self.tablero[::-1]:
            print(fila)
        print(f'\n')

    def MoverDerecha(self):
        if self.posActualX >= 0:
            self.posActualX += 1

    def MoverIzquierda(self):
        if self.posActualX >= 0:
            self.posActualX -= 1

    def MoverArriba(self):
        if self.posActualY >= 0:
            self.posActualY += 1

    def MoverAbajo(self):
        if self.posActualY >= 0:
            self.posActualY -= 1

    def IrAlInicio(self):
        self.posActualX = 0
        self.posActualY = 0

    def IrAPosicion(self, x, y):
        self.posActualX = x
        self.posActualY = y

    def PintarRojo(self):
        self.tablero[self.posActualY][self.posActualX] = 'R'

    def PintarNegro(self):
        self.tablero[self.posActualY][self.posActualX] = 'N'

    def PintarVerde(self):
        self.tablero[self.posActualY][self.posActualX] = 'V'

    def Limpiar(self):
        self.tablero[self.posActualY][self.posActualX] = '-'

    def ejecutar(self, programa):
        primitivas = {
            "MoverArriba": self.MoverArriba,
            "MoverAbajo": self.MoverAbajo,
            "MoverIzquierda": self.MoverIzquierda,
            "MoverDerecha": self.MoverDerecha,
            "PintarNegro": self.PintarNegro,
            "PintarRojo": self.PintarRojo,
            "PintarVerde": self.PintarVerde,
            "PintarLimpiar": self.Limpiar,
            "IrAlInicio": self.IrAlInicio,
            "DibujarTablero": self.DibujarTablero,
            "CrearTablero": self.CrearTablero,
            "ComentarioEnPantalla": ComentarioEnPantalla
        }
        exec(programa, primitivas)


if __name__ == "__main__":
    print('Ejecución de prueba: \n')
    qDraw = QDraw()
    qDraw.CrearTablero(3, 3)
    qDraw.PintarVerde()
    qDraw.MoverDerecha()
    qDraw.MoverArriba()
    qDraw.PintarRojo()
    qDraw.MoverDerecha()
    qDraw.MoverArriba()
    qDraw.PintarNegro()
    qDraw.MoverIzquierda()
    qDraw.PintarVerde()
    qDraw.Limpiar()
    qDraw.IrAPosicion(0, 1)
    qDraw.PintarNegro()
    qDraw.DibujarTablero()
