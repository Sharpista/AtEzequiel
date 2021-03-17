import socket, time

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Tenta se conectar ao servidor
    s.connect((socket.gethostname(), 8881))

    msg = s.recv(400).decode('utf-8')

    nome_diretorio = input(msg)
    nome_diretorio_bytes = nome_diretorio.encode('utf-8')
    s.send(nome_diretorio_bytes)

    arquivos = s.recv(1000).decode('utf-8')

    print(arquivos)


except Exception as erro:
    print(str(erro))

# Fecha o socket
s.close()

input("Pressione qualquer tecla para sair...")
