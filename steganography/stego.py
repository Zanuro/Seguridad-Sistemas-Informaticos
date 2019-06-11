#!/usr/bin/env python
from stegano import lsb
import Image
import piexif
import imghdr


#secret = lsb.hide("imagen-a-cifrar.png", "Esto es un mensaje de ejemplo")
#secret.save("imagen-a-cifrar-modificada.png")

#print(mensaje)


imagen = input("Introduce el nombre de la imagen que quieres descifrar:")

try:
  im = Image.load(imagen)
  im.verify()
  im.close()
  im = Image.load(imagen)
  im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
  im.close()
except:


format = imghdr.what(imagen)

if format == 'png' or format == 'rgb' or format == 'jpeg':

    mensaje = lsb.reveal(imagen)

    print(mensaje)

