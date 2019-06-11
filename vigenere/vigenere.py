from random import *
import binascii
import sys
import string

class Vigenere:


    def __init__(self, clave='OTRO',clave_separada='otro otro',mensaje_original='HOLA', mensaje_cifrado='VHCO', mensaje_dividido='otro',
                 posicion_div=[], posicion_clave=[], mensaje_final='ABBA',posicion_letras=[]):
        self.clave = clave
        self.clave_separada = clave_separada
        self.alphabet = string.ascii_uppercase
        self.mensaje_original = mensaje_original
        self.mensaje_cifrado = mensaje_cifrado
        self.mensaje_dividido = mensaje_dividido
        self.posicion_div = posicion_div
        self.posicion_clave = posicion_clave
        self.mensaje_final = mensaje_final
        self.posicion_letras = posicion_letras

    def input_message(self, metodo):
        if metodo == 0:
            print('Introduce el mensaje que quieres encriptar:')
            var = input()

            espacios = 0
            for x in var:
                if x != ' ':
                    espacios +=1
                else:
                    self.posicion_letras.append(espacios)
                    espacios = 0

            self.posicion_letras.append(espacios)
            #print(self.posicion_letras)
            var = var.replace(" ", "")

            #print(string.ascii_letters)
            otro = string.ascii_letters
            # print(otro)
            for x in var:
                if x not in otro:
                    raise ValueError('Las letras permitidas son las del alfabeto latino internacional.')
                elif x in otro:
                    var = var.replace(x, x.upper())

            self.mensaje_original = var
            return self.mensaje_original
        elif metodo == 1:
            print('Introduce el mensaje que quieres desencriptar:')
            var = input()

            var = var.replace(" ", "")

            otro = string.ascii_letters
            for x in var:
                if x not in otro:
                    raise ValueError('Las letras permitidas son las del alfabeto latino internacional.')
                elif x in otro:
                    var = var.replace(x, x.upper())

            self.mensaje_original = var
            return self.mensaje_original
        else:
            raise ValueError('Se ha producido un error')

    def input_clave(self):
        print('Introduce la clave que quieres utilizar:')
        var = input()

        var = var.replace(" ", "")

        otro = string.ascii_letters
        for x in var:
            if x not in otro:
                raise ValueError('Las letras permitidas son las del alfabeto latino internacional.')
            elif x in otro:
                var = var.replace(x, x.upper())

        self.clave = var
        return self.clave

    def dividir(self):
        #self.mensaje_original = self.mensaje_original.split()
        self.mensaje_dividido = ' '.join((self.mensaje_original[i:len(self.clave)+i]) for i in range(0, len(self.mensaje_original), len(self.clave)))
        print(self.mensaje_dividido)
        print(self.clave_separada)
        # self.clave_separada = ' '.join((self.clave[i:i+len(self.clave)]) for i in range(0, len(self.mensaje_original), len(self.clave)))
        # print(self.clave_separada)

    def repetir_clave(self):
        self.clave_separada = (self.clave * int((len(self.mensaje_original)/len(self.clave))+1))[:len(self.mensaje_original)]
        self.clave_separada = ' '.join((self.clave_separada[i:i+len(self.clave)]) for i in range(0, len(self.mensaje_original), len(self.clave)))

    def get_position(self, metodo):

        self.posicion_div = []
        for x in self.mensaje_dividido:
            if ord(x) >= 65 and ord(x) <= 90:
                y = ord(x)-65
                #print(str(y))
                self.posicion_div.append(str(y))
            elif x == " ":
                self.posicion_div.append(" ")

        # print(self.posicion_div)

        self.posicion_clave = []
        for x in self.clave_separada:
            if ord(x) >= 65 and ord(x) <= 90:
                y = ord(x)-65
                #print(str(y))
                self.posicion_clave.append(str(y))
                
            elif x == " ":
                self.posicion_clave.append(" ")

        # print(self.posicion_clave)

        variable_valores=[]
        w = 0
        if metodo == 0:
            if len(self.posicion_clave) == len(self.posicion_div):
                for x in self.posicion_div:

                    if x == ' ' and self.posicion_clave[w] == ' ':
                        variable_valores.append(' ')
                        w += 1
                    else:
                        y = int(x)+int(self.posicion_clave[w])
                        variable_valores.append(y)
                        w += 1

                # print(variable_valores)
            else:
                raise ValueError('Se ha producido un error ya que los tamanos no coinciden')

            variable_letras=[]
            for x in variable_valores:
                if x == ' ':
                    variable_letras.append(' ')
                else:
                    tmp = x % 26
                    tmp += 65
                    variable_letras.append(chr(tmp))

            # print(variable_letras)
            self.mensaje_final = ''.join(variable_letras)
            print(self.mensaje_final)

        elif metodo == 1:
            if len(self.posicion_clave) == len(self.posicion_div):
                for x in self.posicion_div:
                    if x == ' ' and self.posicion_clave[w] == ' ':
                        variable_valores.append(' ')
                        w += 1
                    else:
                        if int(x) >= int(self.posicion_clave[w]):
                            y = int(x) - int(self.posicion_clave[w])
                            variable_valores.append(y)
                            w += 1
                        else:
                            y = (int(x) + 26) - int(self.posicion_clave[w])
                            variable_valores.append(y)
                            w += 1

                # print(variable_valores)
            else:
                raise ValueError('Se ha producido un error ya que los tamanos no coinciden')

            variable_letras=[]
            for x in variable_valores:
                if x == ' ':
                    variable_letras.append(' ')
                else:
                    tmp = x % 26
                    tmp += 65
                    variable_letras.append(chr(tmp))

            # print(variable_letras)
            self.mensaje_final = ''.join(variable_letras)
            print(self.mensaje_final)

    def execute_program(self):
        print("\n-------- VIGENERE-----\n\n")
        variable = input("Quieres encriptar o desencriptar? 0-Encryption, 1-Decryption\n")
        print(variable)
        if variable == '0':
            self.input_message(0)
            self.input_clave()
            print("\n")
            self.repetir_clave()
            self.dividir()
            self.get_position(0)
            print("Texto cifrado: ", self.mensaje_final.replace(" ", ""))

        elif variable == '1':
            self.input_message(1)
            self.input_clave()
            self.repetir_clave()
            self.dividir()
            self.get_position(1)
            print("\nTexto original: ", self.mensaje_final.replace(" ", ""))

        else:
            print("Se ha introducido un valor incorrecto\n")
            return



ejemplo = Vigenere()
ejemplo.execute_program()

