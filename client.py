from socket import *
from constCS import *
import pickle

# Cores
ROSA = "\033[95m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"


s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

#função para que o v1 e v2 sejaam validos
def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print(f"{VERMELHO}Entrada inválida! Digite um número válido.{RESET}")

#digitando nome e curso
print(f"\n{ROSA}Olá!{RESET} Bem-vindo a atividade Client-servidor com sockets\n")
nome = input("Digite seu nome: ")
cursos_validos = ["cc", "es", "ia", "si"]
curso = ""

while curso not in cursos_validos:
    print("Escolha o curso: cc, es, ia ou si")
    curso = input("Digite o curso: ").lower()
    if curso not in cursos_validos:
        print(f"{VERMELHO}Curso inválido! Tente novamente.{RESET}\n")

print(f"\nÓtimo! {VERDE}{nome}{RESET}, você está lecionando a matéria de Sistemas distribuídos para o curso de {curso}.\n")
print(f"Você pode fazer as seguintes operações: soma({AZUL}soma{RESET}), subtração({AZUL}sub{RESET}), multiplicação({AZUL}mult{RESET}), divisão({AZUL}div{RESET})\n\n")

while True:
    op = input("Escolha a operação a ser executada (soma, sub, mult, div, pare): ")
    #caso seja pare
    if op == "pare":
        data = {"OP": "pare"}
        msg = pickle.dumps(data)
        s.sendall(msg)
        print(f"{ROSA}Obrigada{RESET}, {nome} por executar o programa.\nEncerrando cliente...\n")
        break

    # se a operação for invalida
    elif op not in ["soma", "sub", "mult", "div"]:
        data = {"OP": op} 
        msg = pickle.dumps(data)
        s.sendall(msg)
        msg = s.recv(1024)
        data = pickle.loads(msg)
        print("Erro:", data["RES"])
        continue  # volta pro início do loop

    v1 = ler_float("Digite o valor do primeiro operando: ")
    v2 = ler_float("Digite o valor do segundo operando: ")
    data = {"OP": op, "V1": v1, "V2": v2}
    msg = pickle.dumps(data)
    s.sendall(msg)

    msg = s.recv(1024)
    data = pickle.loads(msg)

    if data["STATUS"] == "OK":
        print(f"{VERDE}Resultado:{RESET} {data['RES']}")
    else:
        print(f"{VERMELHO}Erro:{RESET} {data['RES']}")

s.close()
