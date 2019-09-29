#Cliente TCP
import socket #importando a biblioteca socket
SERVER = '127.0.0.1' # Endereço IP do Servidor
PORT = 80 # Porta que o Servidor está escutando
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
print ('Para sair, você deve pressionar control x')
msg = input()
while msg != '\x18':
    tcp.send(msg.encode('utf-8'))
    msg = input()
tcp.close()