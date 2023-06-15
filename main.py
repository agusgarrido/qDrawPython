from qDraw import QDraw


def Ejecutar():
    qDraw = QDraw()
    archivo = open('programa.txt', 'r')
    programa = archivo.read()
    archivo.close()
    qDraw.ejecutar(programa)


if __name__ == '__main__':
    Ejecutar()
