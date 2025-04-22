# SD-BigFS
Projeto da disciplina de Sistemas Distribuídos

## Primeira versão:
---

## ls [CAMINHO]
Lista o conteúdo de um diretório ou exibe o nome de um arquivo.

- **Parâmetros**:
  - `CAMINHO` (opcional): caminho do diretório ou arquivo. Se omitido, o diretório atual (`.`) é listado.

---

## rm CAMINHO
Remove um arquivo ou todos os arquivos de um diretório.

- **Parâmetros**:
  - `CAMINHO` (obrigatório): caminho do arquivo ou diretório.
---

## cp ORIGEM [DESTINO]
Copia um arquivo da origem para o destino.

- **Parâmetros**:
  - `ORIGEM` (obrigatório): caminho do arquivo a ser copiado.
  - `DESTINO` (opcional): caminho de destino. Se omitido, o arquivo é copiado para o diretório atual.

---

## get CAMINHO
Faz o download de um arquivo do servidor para o cliente.
O arquivo será salvo no mesmo diretório onde o cliente está executando.

- **Parâmetros**:
  - `CAMINHO` (obrigatório): caminho do arquivo no servidor.

---

