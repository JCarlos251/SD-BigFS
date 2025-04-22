import socket
import os
import shutil

HOST = 'localhost'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor aguardando conexão em {HOST}:{PORT}")
conn, addr = server.accept()
print(f"Conectado por {addr}")

while True:
    # Recebe comando do cliente
    comando = conn.recv(1024).decode()

    if not comando:
        break  # encerra se não receber nada

    comando_list = comando.split()

    if comando_list[0] == 'ls':
        caminho = comando_list[1] if len(comando_list) > 1 else '.'
        if os.path.exists(caminho):
            if os.path.isdir(caminho):
                conteudo = '\n'.join(os.listdir(caminho))
            else:
                conteudo = f"Arquivo encontrado com sucesso: {caminho}"
        else:
            conteudo = "Caminho não encontrado."
        conn.send(conteudo.encode())

    elif comando_list[0] == 'rm':
        caminho = comando_list[1]
        if os.path.isfile(caminho):
            os.remove(caminho)
            msg = f"{caminho} removido."
        elif os.path.isdir(caminho):
            for f in os.listdir(caminho):
                fp = os.path.join(caminho, f)
                if os.path.isfile(fp):
                    os.remove(fp)
            msg = f"Arquivos do diretório {caminho} removidos."
        else:
            msg = "Arquivo ou diretório não encontrado."
        conn.send(msg.encode())

    elif comando_list[0] == 'cp':
        origem = comando_list[1]
        destino = comando_list[2] if len(comando_list) > 2 else '.'
        if os.path.isfile(origem):
            shutil.copy(origem, destino)
            msg = f"{origem} copiado para {destino}"
        else:
            msg = "Arquivo de origem inválido."
        conn.send(msg.encode())

    elif comando_list[0] == 'get':
        caminho = comando_list[1]
        if os.path.isfile(caminho):
            with open(caminho, 'rb') as f:
                dados = f.read()
            conn.send(dados)  # envia o conteúdo do arquivo
        else:
            conn.send("Arquivo não encontrado.".encode())

    else:
        conn.send("Comando inválido.".encode())

conn.close()
server.close()
