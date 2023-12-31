# Modulo de espera
# delay.delay(0.3) = DELAY 300

import time

def delay(pausa):
    try:
        if pausa < 0:
            raise ValueError("El valor de pausa no puede ser negativo")
        time.sleep(pausa)
    except ValueError:
        raise ValueError("El valor de pausa no puede ser negativo")
    except TypeError:
        raise ValueError("'<' no es compatible entre instancias de 'str' e 'int'")
    except Exception as e:
        raise Exception(f"Error inesperado: {e}")