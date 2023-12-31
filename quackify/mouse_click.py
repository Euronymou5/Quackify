# Modulo de pulsacion del click del mouse derecho, izquierdo y boton central.

# mouse_click.right()  =  RMOUSE
# mouse_click.left() = LMOUSE
# mouse_click.middle() = MMOUSE

import pyautogui

def right():
    """
    Simula un clic derecho del ratón utilizando la función rightClick de pyautogui.
    
    right  =  RMOUSE
    """
    pyautogui.rightClick()

def left():
    """
    Simula un clic izquierdo del ratón utilizando la función leftClick de pyautogui.
    
    left() = LMOUSE
    """
    
    pyautogui.leftClick()

def middle():
    """
    Simula un clic en el botón central del ratón utilizando la función click de pyautogui con el botón 'middle'.
    
    middle = MMOUSE
    """
    
    pyautogui.click(button='middle')