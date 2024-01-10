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
