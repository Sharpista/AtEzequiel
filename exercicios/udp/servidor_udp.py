import pickle
from multiprocessing.dummy import Process

import psutil
import socket

HOST = socket.gethostname()  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está esperando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)


udp.settimeout(8)
(msg, cliente) = udp.recvfrom(1024)

memoria = psutil.virtual_memory()

resposta = {
    'qtd_total': memoria.total,
    'qtd_disp': memoria.used / memoria.total
}

bytes = pickle.dumps(resposta)

udp.settimeout(8)
udp.sendto(bytes, cliente)

udp.close()
