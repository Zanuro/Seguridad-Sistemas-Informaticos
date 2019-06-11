from random import *
import binascii
import sys
import string


class RC:

    def __init__(self, semilla=[], texto_original=[],secuencia=[], clave_rep=[], texto_cifrado=[],sec_mensaje=[],sec_cifrante=[]):

        #Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.

        self.semilla = semilla
        self.texto_original = texto_original
        self.secuencia = secuencia
        self.clave_rep = clave_rep
        self.texto_cifrado = texto_cifrado
        self.sec_mensaje = sec_mensaje
        self.sec_cifrante = sec_cifrante

    def ksa(self):

        for x in range(0, 256):
            self.secuencia.append(x)
        #print(self.secuencia)
        #print(len(self.semilla))

        for x in range(0, 256):
            self.clave_rep.append(self.semilla[x % len(self.semilla)])

        # print(self.clave_rep)

        f = 0

        for x in range(0, 256):

            f = (f + int(self.secuencia[x]) + int(self.clave_rep[x])) % 256
            self.secuencia[x], self.secuencia[f] = self.secuencia[f], self.secuencia[x]

        print(self.secuencia)

    def spritz_prg(self):

        i = 0
        j = 0
        k = 0
        z = 0

        print('Generacion de secuencia cifrante y texto cifrado:')

        w = 5

        for x in range(0, len(self.texto_original)):

            i = (i+w) % 256
            j = (k + self.secuencia[(j+self.secuencia[i])%256]) % 256
            k = (i + k + self.secuencia[j]) % 256

            self.secuencia[i], self.secuencia[j] = self.secuencia[j], self.secuencia[i]

            z = (self.secuencia[(j+self.secuencia[(i+self.secuencia[(z+k) % 256])%256])%256]) % 256

            sec_cifr_bin = '{0:08b}'.format(self.secuencia[z], 'b')
            text_orig_bin = '{0:08b}'.format(self.texto_original[x], 'b')

            otro = ''
            y = 0
            for v in sec_cifr_bin:
                var = int(v) ^ int(text_orig_bin[y])
                y += 1
                otro += str(var)

            self.texto_cifrado.append(int(otro, 2))

            print('Byte ', x + 1, ' de secuencia cifrante es: S[', z, '] = ', self.secuencia[z], '--->', sec_cifr_bin)
            print('Byte ', x + 1, ' de texto original es:     M[', x + 1, '] = ', self.texto_original[x], '--->',text_orig_bin)
            print('Byte ', x + 1, ' de texto cifrado es:      C[', x + 1, '] = ', int(otro, 2), '--->', otro)
            print('\n')

            #return z

    def secuencia_cifrante(self, metodo):

        if metodo == 0:

            i = 0
            j = 0

            print('Generacion de secuencia cifrante y texto cifrado:')
            for x in range(0, len(self.texto_original)):

                i = (i+1) % 256
                j = (j+self.secuencia[i]) % 256
                self.secuencia[i], self.secuencia[j] = self.secuencia[j], self.secuencia[i]

                t = (self.secuencia[i]+self.secuencia[j]) % 256

                # print(str(self.secuencia[t]))
                sec_cifr_bin = '{0:08b}'.format(self.secuencia[t], 'b')
                text_orig_bin = '{0:08b}'.format(self.texto_original[x], 'b')

                otro = ''

                if (len(text_orig_bin) > len(sec_cifr_bin)):
                    variable = int(sec_cifr_bin, 2)
                    variable1 = len(text_orig_bin)
                    sec_cifr_bin = "{0:0{var}b}".format(variable, var=variable1)

                    y = 0
                    for z in sec_cifr_bin:
                        var = int(z) ^ int(text_orig_bin[y])
                        y += 1
                        otro += str(var)

                    self.texto_cifrado.append(int(otro, 2))

                    #print(otro)
                    #print(otroo)

                elif(len(text_orig_bin) < len(sec_cifr_bin)):

                    variable = int(text_orig_bin, 2)
                    variable1 = len(sec_cifr_bin)
                    text_orig_bin = "{0:0{var}b}".format(variable, var=variable1)

                    y = 0
                    for z in sec_cifr_bin:
                        var = int(z) ^ int(text_orig_bin[y])
                        y += 1
                        otro += str(var)

                    self.texto_cifrado.append(int(otro, 2))

                    # print(otro)
                    # print(otroo)
                else:

                    y = 0
                    for z in sec_cifr_bin:
                        var = int(z) ^ int(text_orig_bin[y])
                        y += 1
                        otro += str(var)

                    self.texto_cifrado.append(int(otro, 2))

                    # print(otro)
                    # print(otroo)

                print('Byte ', x+1, ' de secuencia cifrante es: S[', t, '] = ', self.secuencia[t], '--->', sec_cifr_bin)
                print('Byte ', x+1, ' de texto original es:     M[', x+1, '] = ', self.texto_original[x], '--->', text_orig_bin)
                print('Byte ', x+1, ' de texto cifrado es:      C[', x+1, '] = ', int(otro, 2), '--->', otro)
                print('\n')

            print('El mensaje cifrado es: ', self.texto_cifrado)

            texto_o_bin = []
            for x in self.texto_cifrado:
                variable_bin = '{0:08b}'.format(x, 'b')
                texto_o_bin.append(variable_bin)

            print('El mensaje cifrado en binario es:', texto_o_bin)

        elif metodo == 1:
            i = 0
            j = 0

            print('Generacion de secuencia original y texto original')
            for x in range(0, len(self.texto_cifrado)):

                i = (i + 1) % 256
                j = (j + self.secuencia[i]) % 256
                self.secuencia[i], self.secuencia[j] = self.secuencia[j], self.secuencia[i]

                t = (self.secuencia[i] + self.secuencia[j]) % 256

                # print(str(self.secuencia[t]))
                sec_cifr_bin = '{0:08b}'.format(self.secuencia[t], 'b')
                text_cifr_bin = '{0:08b}'.format(self.texto_cifrado[x], 'b')

                otro = ''

                if (len(text_cifr_bin) > len(sec_cifr_bin)):
                    variable = int(sec_cifr_bin, 2)
                    variable1 = len(text_cifr_bin)
                    sec_cifr_bin = "{0:0{var}b}".format(variable, var=variable1)

                    y = 0
                    for z in sec_cifr_bin:
                        var = int(z) ^ int(text_cifr_bin[y])
                        y += 1
                        otro += str(var)

                    self.texto_original.append(int(otro, 2))

                    # print(otro)
                    # print(otroo)

                elif (len(text_cifr_bin) < len(sec_cifr_bin)):

                    variable = int(text_cifr_bin, 2)
                    variable1 = len(sec_cifr_bin)
                    text_cifr_bin = "{0:0{var}b}".format(variable, var=variable1)

                    y = 0
                    for z in sec_cifr_bin:
                        var = int(z) ^ int(text_cifr_bin[y])
                        y += 1
                        otro += str(var)

                    self.texto_original.append(int(otro, 2))

                    # print(otro)
                    # print(otroo)
                else:

                    y = 0
                    for z in sec_cifr_bin:
                        var = int(z) ^ int(text_cifr_bin[y])
                        y += 1
                        otro += str(var)

                    self.texto_original.append(int(otro, 2))

                    # print(otro)
                    # print(otroo)

                print('Byte ', x + 1, ' de secuencia cifrante es: S[', t, '] = ', self.secuencia[t], '--->',sec_cifr_bin)
                print('Byte ', x + 1, ' de texto cifrado es:     C[', x + 1, '] = ', self.texto_cifrado[x], '--->', text_cifr_bin)
                print('Byte ', x+1, ' de texto original es:     M[', x+1, '] = ', int(otro, 2), '--->', otro)
                print('\n')

            print('El mensaje original es:', self.texto_original)

            texto_o_bin = []
            for x in self.texto_original:
                variable_bin = '{0:08b}'.format(x, 'b')
                texto_o_bin.append(variable_bin)

            print('El mensaje original en binario es:', texto_o_bin)

        else:
            raise ValueError('Se ha producido un error')


    def input_datos(self,metodo):


        if metodo == 0:

            var = input('Introduce la semilla de clave que quieres utilizar: ')
            var = var.split(' ')
            var = list(map(int, var))
            # print(var)
            self.semilla = var

            varr = input('Introduce el mensaje original que quieres utilizar: ')
            varr = varr.split(' ')
            varr = list(map(int, varr))
            # print(varr)
            self.texto_original = varr

        elif metodo == 1:

            var = input('Introduce la semilla de clave que se ha utilizado: ')
            var = var.split(' ')
            var = list(map(int, var))
            # print(var)
            self.semilla = var

            varr = input('Introduce el mensaje cifrado que quieres utilizar: ')
            varr = varr.split(' ')
            varr = list(map(int, varr))
            # print(varr)
            self.texto_cifrado = varr


    def execute_program(self):
        print("\n-------- RC4-----------\n\n")
        variable = input("Quieres cifrar o descrifrar? 0-Cifrado, 1-Descifrado 2 Spritz\n")
        print(variable)
        if variable == '0':
            self.input_datos(0)
            print("\n")
            self.ksa()
            self.secuencia_cifrante(0)
        elif variable == '1':
            self.input_datos(1)
            print("\n")
            self.ksa()
            self.secuencia_cifrante(1)

        elif variable == '2':
            self.input_datos(0)
            print("\n")
            self.ksa()
            self.spritz_prg()
        else:
            print("Se ha introducido un valor incorrecto\n")
            return


ejemplo = RC()
# ejemplo.input_datos()
# ejemplo.ksa()
# ejemplo.secuencia_cifrante()
ejemplo.execute_program()

