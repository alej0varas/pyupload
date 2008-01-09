#!/usr/bin/python
#si usas este script, tienes que cambiar el nombre del archivo 
#a subir y crear el archivo a subir.
from ftplib import FTP
import re

#next line will disapear when wx is done
#arch=raw_input('file to upload: ')

def uploader(arch):
	f=open(arch, 'r')

	sitio=open('site.ini')
	lista=sitio.readlines()
	lista0=lista[0]
	lista1=lista[1]
	lista2=lista[2]
	site=re.sub('\n', '', lista0)
	user=re.sub('\n', '', lista1)
	password=re.sub('\n', '', lista2)
	#print site
	#print user
	#print password
	sitio.close()

	#con estos datos conectas 
	ftp = FTP(site, user, password)
	
	#envia y guarda el archivo, con el nombre que le das a STOR
	# f es el objeto f = open('test.txt', 'r')
	este="uploader" + '.' + arch + '.' + "now"
	ftp.mkd(este)
	ftp.cwd(este)
	tempura="STOR" + ' ' + arch
	#print tempura
	ftp.storbinary(tempura, f)
	#no es necesario, es para debug. envia el comando 'list'
	ftp.retrlines('LIST')
	#sales simpiamente
	ftp.quit()
