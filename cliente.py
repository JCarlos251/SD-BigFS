import socket

HOST = 'localhost'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Conectado ao servidor. Use comandos: ls, rm, cp, get")

while True:
    cmd = input(">>> ")

    if not cmd:
        continue

    client.send(cmd.encode())  # envia comando ao servidor

    if cmd.startswith('get'):
        print("get em construção")
    else:
        resposta = client.recv(1024).decode()  # recebe resposta
        print(resposta)
