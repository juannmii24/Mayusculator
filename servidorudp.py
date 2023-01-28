from socket import *
serviPuerto = 12000
socketServidor = socket(AF_INET, SOCK_DGRAM)
socketServidor.bind(('', serviPuerto))
print ('Soy Mayusculator y espero cadenas en minuscula')
while True:
	mensaje, ClienteDir = socketServidor.recvfrom(2048)
	mensajeMay = mensaje.upper()
	socketServidor.sendto(mensajeMay, ClienteDir)
