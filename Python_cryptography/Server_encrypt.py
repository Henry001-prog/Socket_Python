#Servidor TCP
import socket
from Crypto.Cipher import AES


def encrypt(raw):
	cipher = AES.new( 'my_merchant_key_', AES.MODE_CFB, 'This is an IV456' )
	return ( cipher.encrypt( raw ) )

    
def decrypt(enc):
	cipher = AES.new('my_merchant_key_', AES.MODE_CFB, 'This is an IV456')
	return (cipher.decrypt(enc))



HOST = '' # Endereo IP do Servidor
PORT = 8741 # Porta que o Servidor vai escutar
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
#msg = tcp.recv(header_l)
while True:
    con, cliente = tcp.accept()
    print ('Conectado por', cliente)
    while True:
        msg = (decrypt(con.recv(1024)))
        #tcp.recv(rsa.desencriptar(msg, chave_privada).decode("utf-8"))
        if not msg: break
        print(msg.decode("utf-8"))
    print ('Finalizando conexao do cliente', cliente)
    con.close()