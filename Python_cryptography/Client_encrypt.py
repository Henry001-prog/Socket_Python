#Cliente TCP
import socket #importando a biblioteca socket
from Crypto.Cipher import AES

def encrypt(raw):
	cipher = AES.new(b'my_merchant_key_', AES.MODE_CFB, b'This is an IV456' )
	return ( cipher.encrypt( raw ) )

    
def decrypt(enc):
	cipher = AES.new('my_merchant_key_', AES.MODE_CFB, 'This is an IV456')
	return (cipher.decrypt(enc))


SERVER = '127.0.0.1' # Endereço IP do Servidor
PORT = 8741 # Porta que o Servidor está escutando
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
print ('Para sair, você deve pressionar control x')
msg = input()
#mensagem_encriptada = rsa.encriptar(msg, chave_publica)
while msg != '\x18':
    #tcp.encode('utf-8')
    tcp.sendall(encrypt(msg.encode('utf-8')))
    #msg = (encrypt(msg).encode("utf-8"))
    msg = input()
tcp.close()