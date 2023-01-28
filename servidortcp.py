from socket import *
serviPuerto = 12000
socketServidor = socket(AF_INET, SOCK_STREAM)
socketServidor.bind(('', serviPuerto))
socketServidor.listen(1)
print ('Soy Mayusculator y espero cadenas en minuscula')
while True:
	socketConex, clienteDir = socketServidor.accept()
	mensaje = socketConex.recv(1024)
	mensajeMay = mensaje.upper()
	socketConex.send(mensajeMay)
	socketConex.close()
