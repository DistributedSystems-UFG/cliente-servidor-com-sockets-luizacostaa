from socket import *
from constCS import *
import pickle

s = socket(AF_INET, SOCK_STREAM) 
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   #faz com que a porta possa ser reutilizada logo após o fechamento. Fiz isso porque estava dando erro ao usar Ctrl+C
s.bind((HOST, PORT))  
s.listen(1)           
print("Servidor aguardando conexão...")
(conn, addr) = s.accept()  
print("Conectado a:", addr)

while True:
    msg = conn.recv(1024)    # recebe dados do cliente
    if not msg: 
        break                # cliente desconectou
    
    data = pickle.loads(msg)
    print("Recebido:", data)

    op = data.get("OP")      # usa .get() para não gerar erro se chave não existir

    # se o cliente pedir para parar, o servidor encerra
    if op == "pare":
        print("Servidor encerrando a pedido do cliente.")
        break

    # pega operandos, se existirem
    v1 = data.get("V1")
    v2 = data.get("V2")

    # operações suportadas
    if op == "soma" and v1 is not None and v2 is not None:
        res = v1 + v2
        status = "OK"
    elif op == "sub" and v1 is not None and v2 is not None:
        res = v1 - v2
        status = "OK"
    elif op == "mult" and v1 is not None and v2 is not None:
        res = v1 * v2
        status = "OK"
    elif op == "div" and v1 is not None and v2 is not None:
        if v2 == 0:
            status = "NOK"
            res = "Erro: divisão por zero"
        else:
            res = v1 / v2
            status = "OK"
    else:
        status = "NOK"
        res = "Operação não suportada\n"

    # envia resposta ao cliente
    response = {"STATUS": status, "RES": res}
    msg = pickle.dumps(response)
    conn.sendall(msg)

conn.close()
s.close()
