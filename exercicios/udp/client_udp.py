import socket, time, pickle

# Função que imprime a lista formatada
from multiprocessing.dummy import Process

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

udp.settimeout(5)

tentativas = 0

while tentativas < 5:

    udp.sendto(b'', dest)

    try:

        (pacote, remetente) = udp.recvfrom(1024)
        break
    except Exception as error:
        print(error)
        tentativas += 1
        continue

if pacote:
    msg = pickle.loads(pacote)
else:
    msg = 'FIM'

print(msg)
udp.close()
