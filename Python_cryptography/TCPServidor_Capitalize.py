#Servidor TCP
import socket
HOST = '' # Endereo IP do Servidor
PORT = 80 # Porta que o Servidor vai escutar
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Conectado por', cliente)
    while True:
        msg = con.recv(1024).decode('utf-8')
        if not msg: break
        msg = msg.capitalize()
        print(msg)
    print ('Finalizando conexao do cliente', cliente)
    con.close()