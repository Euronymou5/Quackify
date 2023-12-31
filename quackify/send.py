import time
from pynput.keyboard import Controller

velocidad_escritura = 0.01
final = False
teclado = Controller()

def escribir(texto):
    """
    Escribe el texto caracter por caracter con una velocidad de escritura específica.

    :parametro texto: El texto que se va a escribir.
    """
    
    for c in texto:
        teclado.type(c)
        time.sleep(velocidad_escritura)
    global final
    final = True

def send_text(texto):
    """
    Envía un texto utilizando la función 'escribir' y añade pausas para simular la escritura real.

    :parametro texto: El texto que se va a enviar.
    """
    
    time.sleep(0.001)
    escribir(texto)
    time.sleep(0.05)

def string(texto):
    """
    Función de conveniencia para escribir un texto utilizando 'send_text'.

    :parametro texto: El texto que se va a escribir.
    """
    
    send_text(texto)

def speed(nueva_velocidad):
    """
    Establece la velocidad de escritura a un valor específico.

    :parametro nueva_velocidad: La nueva velocidad de escritura (tiempo de espera entre caracteres).
    """
    
    global velocidad_escritura
    velocidad_escritura = nueva_velocidad