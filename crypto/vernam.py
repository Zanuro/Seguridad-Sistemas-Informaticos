from random import *
import binascii
import sys

class Vernam:


    def __init__(self, clave, mensaje_binario, mensaje_original, mensaje_cifrado, mensaje_final):
        self.clave = clave
        self.mensaje_binario = mensaje_binario
        self.mensaje_original = mensaje_original
        self.mensaje_cifrado = mensaje_cifrado
        self.mensaje_final = mensaje_final


    def transform_message(self, mensaje):
        mensaje_binarioo = ''
        for var in mensaje:
            otro = '{0:08b}'.format(ord(var), 'b')
            mensaje_binarioo += otro
            # otro = ' '.join(otro)
        self.mensaje_binario = mensaje_binarioo

        return self.mensaje_binario


    def asignar_clave(self):
        x = 1
        clavee = ''
        while x <= len(self.mensaje_binario):
            clavee += str(randint(0, 1))
            x += 1
        # clave = '010101010101010'
        self.clave = clavee
        print('La clave es:', self.clave, 'con tamano de:', len(self.clave),'bits')
        return self.clave


    def introducir_clave(self):
        var = input("Introduce la clave con la que quieres encriptar el mensaje!\n")
        print(len(var))
        if len(self.mensaje_binario) == len(var):
            self.clave = var
            print("La clave que ha introducido es:", self.clave)
        else:
            raise ValueError('Los tamanos no coinciden')

    def asignar_clavee(self, clavv):
        x = 1
        clavee = ''
        if len(clavv) == len(self.mensaje_original):
            for var in clavv:
                otro = '{0:08b}'.format(ord(var), 'b')
                clavee += otro
        else:
            raise ValueError('Los tamanos no coinciden')

        self.clave = clavee
        print('La clave es:', self.clave, 'con tamano de:', len(self.clave),'bits')
        return self.clave


    def crypt(self):
        # mensaje_binario = ''
        #clavee = ''
        #clavee += self.clave
        self.transform_message(self.mensaje_original)
        #self.asignar_clave()
        mensaje_resultante = ''
        z = 0
        print('El mensaje que se quiere encriptar es: ', self.mensaje_original)
        # print('La clave que se utiliza es: ', self.clave)

        for x in self.mensaje_binario:
            # var = int(x) ^ int(self.clave[z])
            if x == self.clave[z]:
                var = 0
                z += 1
            else:
                var = 1
                z += 1
            mensaje_resultante += str(int(var))
        #binascii.b2a_uu(mensaje_resultante.encode())
        variable = ''.join((chr(int(mensaje_resultante[i:i + 8], 2)) for i in range(0, len(mensaje_resultante), 8)))
        # udata = variable.decode("utf-8")
        # asciidata = udata.encode("ascii", "ignore")
        self.mensaje_final = variable
        print('Mensaje original:--> ', self.mensaje_binario)
        print('Clave secreta---:--> ', self.clave)
        print('Mensaje incripta:--> ', mensaje_resultante)
        print('El mensaje cifrado resultante es:', self.mensaje_final)

        return self.mensaje_final


    def decrypt(self):
        # mensaje_binario = ''
        #clavee = ''
        #clavee += self.clave
        self.transform_message(self.mensaje_cifrado)
        #self.asignar_clave()
        mensaje_resultantee = ''
        w = 0
        print('El mensaje que se quiere desencriptar es: ', self.mensaje_cifrado)
        # print('La clave que se utiliza es: ', self.clave)

        for x in self.mensaje_binario:
            var = int(x) ^ int(self.clave[w])
            w += 1
            mensaje_resultantee += str(int(var))

        variable = ''.join((chr(int(mensaje_resultantee[i:i + 8], 2)) for i in range(0, len(mensaje_resultantee), 8)))
        self.mensaje_final = variable
        print('Mensaje original:--> ', self.mensaje_binario)
        print('Clave secreta---:--> ', self.clave)
        print('Mensaje incripta:--> ', mensaje_resultantee)
        print('El mensaje original es:', self.mensaje_final)

        return self.mensaje_final

    def execute_program(self):
        print("\n--------Vernam CYPHER-----\n\n")
        variable = input("Quieres encriptar o decriptar? 0-Encryption, 1-Decryption\n")
        print(variable)
        if variable == '0':
            self.mensaje_original = input("Mensaje que quieres encriptar?\n")
            variable1 = input("Como quieres pasar la clave? 0-Random key, 1-Que la pases tu\n")
            if variable1 == '0':
                self.transform_message(self.mensaje_original)
                self.asignar_clave()
                self.crypt()
            elif variable1 == '1':
                self.transform_message(self.mensaje_original)
                self.introducir_clave()
                self.crypt()
            else:
                print("Se ha introducido un valor incorrecto\n")
                return

        elif variable == '1':
            self.mensaje_cifrado = input("Mensaje que quieres decriptar?\n")
            variable1 = input("Como quieres pasar la clave? 0-Random key, 1-Que la pases tu\n")
            if variable1 == '0':
                self.transform_message(self.mensaje_cifrado)
                self.asignar_clave()
                self.decrypt()
            elif variable1 == '1':
                self.transform_message(self.mensaje_cifrado)
                self.introducir_clave()
                self.decrypt()
            else:
                print("Se ha introducido un valor incorrecto\n")
                return
        else:
            print("Se ha introducido un valor incorrecto\n")
            return


ejemplo = Vernam('01010101', '01011101', 'OTRO', '#$h/', '2h&-')
# str = "1110010001100101011011000110110001101111"
# message = ""
# while str != "":
#     i = chr(int(str[:8], 2))
#     message = message + i
#     str = str[8:]
# print(message)

ejemplo.execute_program()