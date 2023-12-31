# Modulo de pulsacion del click del mouse derecho, izquierdo y boton central.

# mouse_move.move()  =  MOUSE_MOVE

import pyautogui

def get_pos():
    """
    Esta función obtiene la posición actual del cursor y la imprime en la consola.
    """

    print(pyautogui.position())

def move(x, y):
    """
    Esta función mueve el cursor a las coordenadas especificadas (x, y).
    
    :parametro x: La coordenada x a la que se moverá el cursor.
    :parametro y: La coordenada y a la que se moverá el cursor.
    
    move() = MOUSE_MOVE X Y
    """

    pyautogui.moveTo(x, y)