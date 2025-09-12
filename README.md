# Sistema Cliente-Servidor Simples

Este projeto implementa um **sistema cliente-servidor básico** utilizando Python e sockets.  
O sistema permite que um cliente envie requisições ao servidor para realizar **operações matemáticas** simples, recebendo o resultado de volta. Além disso, o cliente informa seu nome e o curso.

---

## Funcionamento do Sistema

1. **Servidor (`server.py`)**  
   - Aguarda conexões de clientes na porta especificada (`PORT` em `constCS.py`).  
   - Recebe requisições do cliente, processa operações matemáticas e envia o resultado de volta.  
   - Suporta as seguintes operações:
     - Soma (`soma`)  
     - Subtração (`sub`)  
     - Multiplicação (`mult`)  
     - Divisão (`div`) — com tratamento para divisão por zero  
   - Caso o cliente envie uma operação inválida, o servidor retorna a mensagem `"Operação não suportada"`.  
   - O servidor encerra quando o cliente envia a operação `pare`.

2. **Cliente (`client.py`)**  
   - Conecta ao servidor na mesma porta.  
   - Solicita o nome do usuário e o curso que ele está lecionando (`cc`, `es`, `ia`, `si`).  
   - Permite executar múltiplas operações matemáticas até que o usuário decida encerrar digitando `pare`.  
   - Colloca entradas das variáveis v1 e v2 

---

## Como executar

1. Abra um terminal e inicie o servidor:

```bash
python3 server.py
```

2. Depois  abra outro terminal e inicie o cliente

```bash
python3 client.py
```

3. Indique seu nome e o curso ao qual está lecionando

4. Escolha a operação a ser executada

5. Escolha os valores dos operandos v1 e v2

6. Repita o processo quantas vezes desejar

7. Quando quiser encerrar o programa indique pare