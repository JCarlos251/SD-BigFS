import socket

HOST = 'localhost'
PORT = 5000

# Cria o socket do cliente e conecta ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Conectado ao servidor. Use comandos: ls, rm, cp, get")

while True:
    cmd = input(">>> ")  # lê comando do usuário

    if not cmd:
        continue

    client.send(cmd.encode())  # envia comando ao servidor

    if cmd.startswith('get'):
        nome_arquivo = cmd.split()[1]
        dados = client.recv(100000)  # recebe o conteúdo do arquivo
        if dados.startswith(b'Arquivo'):
            print(dados.decode())
        else:
            with open(nome_arquivo, 'wb') as f:
                f.write(dados)
            print(f"Arquivo {nome_arquivo} baixado com sucesso.")
    else:
        resposta = client.recv(1024).decode()  # recebe resposta textual
        print(resposta)
