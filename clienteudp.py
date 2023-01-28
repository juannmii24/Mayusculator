from socket import*
serviNombre = '192.168.100.207'
serviPuerto = 12000
socketCliente = socket(AF_INET, SOCK_DGRAM)
socketCliente.connect((serviNombre, serviPuerto))
mensaje = input('Mete una linea en minusculas: ')
socketCliente.send(bytes(mensaje, encoding='utf8'))
mensajeMayu, serviDir = socketCliente.recvfrom(2048)
print(mensajeMayu.decode("utf-8"))
socketCliente.close()
