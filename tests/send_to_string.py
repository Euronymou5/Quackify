import re

def procesar_cadena(cadena):
    patron = r"\.send\('([^']+)'\)"
    coincidencias = re.search(patron, cadena)

    if coincidencias:
        texto_dentro_de_parentesis = coincidencias.group(1)
        print(f"Texto dentro de los paréntesis: {texto_dentro_de_parentesis}")
        print(f'Texto a ducky script:\nSTRING {texto_dentro_de_parentesis}')
    else:
        print("No se encontro una cadena con el patrón .send('...')")

user_input = "send_userinput.send('Holaa')"
procesar_cadena(user_input)