import socket
import select
import errno
import sys
from Crypto.Cipher import AES
import base64

def encrypt(raw):
	cipher = AES.new( 'my_merchant_key_', AES.MODE_CFB, 'This is an IV456' )
	return ( cipher.encrypt( raw ) )

    
def decrypt(enc):
	cipher = AES.new('my_merchant_key_', AES.MODE_CFB, 'This is an IV456')
	return (cipher.decrypt(enc))

    
'''def prompt() :
	sys.stdout.write('<You> \n')
	sys.stdout.flush()'''


HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

#print("Ola mundo")
my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

while True:
	message = input(f"{my_username} > ")
	#sockets_list = [sys.stdin, client_socket]

	#read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

	if message:
		message = encrypt(message.encode("utf-8"))
		message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
		client_socket.send(message_header + message)

	try:
            while True:
		#for sock in read_sockets:
			#if sock == client_socket:
				# receive things
                username_header = client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print("connection closed by the server")
                    sys.exit()


                username_length = int(decrypt(username_header.decode("utf-8").strip()))
                username = client_socket.recv(username_length).decode("utf-8")

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode("utf-8").strip())
                message = client_socket.recv(decrypt(message_length.decode("utf-8")))

                print(f"{username} > {message}")

	except (IOError) as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print('Reading error', str(e))
			sys.exit()
		continue

	except Exception as e:
		print('1General error', str(e))
		sys.exit()