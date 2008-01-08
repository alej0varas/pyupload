#!/usr/bin/python
#si usas este script, tienes que cambiar el nombre del archivo 
#a subir y crear el archivo a subir.
from ftplib import FTP

#con estos datos conectas 
ftp = FTP('dominio', 'usuario', 'password')

#no es necesario, es para debug. envia el comando 'list'
ftp.retrlines('LIST')

#envia y guarda el archivo, con el nombre que le das a STOR
#f es el objeto f = open('test.txt', 'r')
f = open('test.txt', 'r')
ftp.storbinary("STOR test.txt.texto", f)

#sales simpiamente
ftp.quit()

