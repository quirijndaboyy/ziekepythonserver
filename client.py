import socket

#server and client information
client_version = '0.1.2_c'
HOST = input('input ip address: ')
PORT = 9090

#establishing connection
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))


#connecting and version checking
server_version = socket.recv(1024).decode('utf-8')
socket.send(client_version.encode('utf-8'))
print('		##connected to server##')
print(f'client version: {client_version}')
print(f'server version: {server_version}\n ')

#message sending
message = 'undefined'
while message != 'disconnect':
	message = input('message: ')
	socket.send(message.encode('utf-8'))
	
	if message == 'disconnect':
		print('\ndisconnected from server')
	else:
		print('  retun: '+socket.recv(1024).decode('utf-8'))
		#print()
print('session ended')
		
