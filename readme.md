# QDraw - Simulación básica en Python

QDraw es un lenguaje de programación desarrollado por la Universidad Nacional de Quilmes, utilizado en el Ciclo Introductorio del Departamento de Ciencia y Tecnología para las carreras afines a programación.
En base a ello, este programa escrito en Python permite dibujar en una matriz utilizando algunos de los comandos primitivos de qDraw. Podés moverte dentro de la matriz y "pintar" celdas de diferentes colores. Para lograr este objetivo decidí basarme en la programación orientada a objetos.

## Uso

1. Para probarlo podrás clonar el repositorio o descargar los archivos en tu computadora.

2. Dentro del archivo `programa.txt` podrás escribir tu secuencia de comandos para dibujar en la matriz. Se pueden utilizar las siguientes instrucciones:

      - `CrearTablero(x, y)`: Recibe como parámetro dos enteros para establecer el tamaño de la matriz o tablero.
      - `ComentarEnPantalla('comentario')`: Recibe como parámetro un comentario para imprimir en pantalla.
      - `MoverArriba()`: Mueve la posición actual hacia arriba en la matriz.
      - `MoverArriba()`: Mueve la posición actual hacia arriba en la matriz.
      - `MoverAbajo()`: Mueve la posición actual hacia abajo en la matriz.
      - `MoverIzquierda()`: Mueve la posición actual hacia la izquierda en la matriz.
      - `MoverDerecha()`: Mueve la posición actual hacia la derecha en la matriz.
      - `PintarNegro()`: Pinta la celda actual de color negro.
      - `PintarRojo()`: Pinta la celda actual de color rojo.
      - `PintarVerde()`: Pinta la celda actual de color verde.
      - `Limpiar()`: Limpia la celda actual, volviéndola a su estado inicial.
      - `IrAlInicio()`: Mueve la posición actual al inicio de la matriz.
      - `DibujarTablero()`: Muestra en pantalla el estado actual de la matriz.

4. Ejecutar el archivo `main.py` para ver el resultado.

## Ejemplo

Dentro del archivo `programa.txt` hay un ejemplo de su funcionamiento. Este programa crea una matriz de 3x3 y dibuja una línea diagonal multicolor hacia la derecha.



