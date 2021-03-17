import socket, os

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 8881
socket_servidor.bind((host, porta))
socket_servidor.listen()

(socket_cliente, addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

# Recebe pedido do cliente:
msg_bytes = "informe o diretorio".encode('utf-8')
socket_cliente.send(msg_bytes)
diretorio = socket_cliente.recv(400).decode('utf-8')


arquivos = [i for i in os.listdir(diretorio)]

socket_cliente.send(f'{arquivos}'.encode('utf-8'))



