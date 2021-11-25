import socket

#server information
server_version = '0.3.23_s'
HOST = '192.168.2.106'
PORT = 9090

#opening server
print(f' \nserver version: {server_version}\nlistening for connections::\n ')

#establishing connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

communication_socket, address = server.accept()
communication_socket.send(server_version.encode('utf-8'))
client_version = communication_socket.recv(1024).decode('utf-8')
print(f'connected to: {address}\nclient version: {client_version}\n ')


end = 0
while end == 0:
	message = communication_socket.recv(1024).decode('utf-8')
	print(f'{address}: {message}')
	communication_socket.send(f'message received'.encode('utf-8'))
	if message == 'disconnect':
		end = 1
	else:
		end = 0
else:		
	communication_socket.send(f'!disconnected from server!'.encode('utf-8'))
	communication_socket.close()
	print('\ndisconnected from: '+str(address))
	print(' ')
