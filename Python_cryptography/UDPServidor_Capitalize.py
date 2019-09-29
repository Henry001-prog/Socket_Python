#Servidor UDP
import socket

HOST = '' #Endereço IP do Servidor
PORT = 5002 #Porta que o Servidor vai escutar
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
	msg, cliente = udp.recvfrom(1024)
	msg = msg.capitalize().decode('utf-8')
	print (cliente, msg)
udp.close()