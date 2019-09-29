#Cliente UDP
import socket
SERVER = '127.0.0.1' # Endereço IP do Servidor
PORT = 5002 # Porta que o Servidor está escutando
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (SERVER, PORT)
print ('Para sair, você deve pressionar control x')
msg = input()
while msg != '\x18':
	udp.sendto (msg.encode('utf-8'), dest)
	msg = input()
udp.close()