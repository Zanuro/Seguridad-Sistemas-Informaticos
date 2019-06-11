from random import *
import binascii
import sys
from collections import deque
import sys
from termcolor import colored, cprint
import cProfile

class AESSNOW:

    def __init__(self, valor_uno=deque([]), valor_dos=deque([]), byte_sum = '', primer_byte='', segundo_byte='',
                 multiplicacion=''):

        #Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.

        self.valor_uno = valor_uno
        self.valor_dos = valor_dos
        self.byte_sum = byte_sum
        self.primer_byte = primer_byte
        self.segundo_byte = segundo_byte
        self.multiplicacion = multiplicacion

    def programa_principal(self):

        cont1 = self.valor_uno.count("1")
        cont2 = self.valor_dos.count("1")
        print("\n")

        one_position = []

        val_interm = []

        if cont1 >= cont2:

            cprint("Primer byte : {}\n".format(self.valor_uno), 'red')
            cprint("Segundo byte: {}\n".format(self.valor_dos), 'red')
            cprint("Byte Algoritmo: {}\n".format(self.byte_sum), 'red')

            primer = ''.join(self.valor_dos)[0]
            reversed = ''.join(self.valor_dos)[:0:-1]
            reversed += str(primer)

            get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

            one_position = get_indexes('1',reversed)
            #print(one_position)

            number_of_elements = len(one_position)

            # print(one_position)
            #
            # otro = []
            # i = 0
            # for x in range(0, number_of_elements):
            #     otro1 = "0"*8
            #     otro1 = otro1.split(' ')
            #     print(otro1)
            #     otro.append(otro1)
            #
            # for x in otro:
            #     for y in x:
            #         print(y)
            # print(otro)

            #valor_mayor = one_position[len(one_position)-1]

            for x in range(0,len(self.valor_dos)):

                cprint("{}. : {}\n".format(x,self.valor_uno), 'red')

                if x in one_position:

                    if self.valor_uno[0] == '0':

                        val_interm.append(''.join(self.valor_uno))
                        self.valor_uno.rotate(-1)
                        self.valor_uno.pop()
                        self.valor_uno.append('0')

                    elif self.valor_uno[0] == '1':

                        val_interm.append(''.join(self.valor_uno))
                        self.valor_uno.rotate(-1)
                        self.valor_uno.pop()
                        self.valor_uno.append('0')

                        varr = ''.join(self.valor_uno)

                        self.valor_uno.clear()

                        w = 0
                        for y in varr:
                            var = int(y) ^ int(self.byte_sum[w])
                            w += 1
                            self.valor_uno += str(int(var))
                else:

                    if self.valor_uno[0] == '0':

                        self.valor_uno.rotate(-1)
                        self.valor_uno.pop()
                        self.valor_uno.append('0')

                    elif self.valor_uno[0] == '1':

                        self.valor_uno.rotate(-1)
                        self.valor_uno.pop()
                        self.valor_uno.append('0')

                        varr = ''.join(self.valor_uno)

                        self.valor_uno.clear()

                        w = 0
                        for y in varr:
                            var = int(y) ^ int(self.byte_sum[w])
                            w += 1
                            self.valor_uno += str(int(var))

            cprint('Los valores que se suman: {}'.format(val_interm),'red')

            ##  List of lists in each list
            ##  ['01000101', '11010011', '01111000']

            ## [[0,1,0], [1,1,1], [0,0,1] .. ..   ]


            lista_de_elementos = []

            for x in range(8):
                lista_de_elementos.append([int(fila[x]) for fila in val_interm])

            otra_lista = []
            for x in lista_de_elementos:

                numero_unos = x.count(1)
                numero_cero = x.count(0)

                if (numero_unos % 2) == 0:
                    self.multiplicacion += str(0)
                else:
                    self.multiplicacion += str(1)

            cprint("La multiplicacion es: {}".format(self.multiplicacion), 'red')

        else:

            cprint("Primer byte : {}\n".format(self.valor_uno), 'red')
            cprint("Segundo byte: {}\n".format(self.valor_dos), 'red')
            cprint("Byte Algoritmo: {}\n".format(self.byte_sum), 'red')

            primer = ''.join(self.valor_uno)[0]
            reversed = ''.join(self.valor_uno)[:0:-1]
            reversed += str(primer)

            get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

            one_position = get_indexes('1', reversed)
            # print(one_position)

            for x in range(0, len(self.valor_uno)):

                cprint("{}. : {}\n".format(x, self.valor_dos), 'red')

                if x in one_position:

                    if self.valor_dos[0] == '0':

                        val_interm.append(''.join(self.valor_dos))
                        self.valor_dos.rotate(-1)
                        self.valor_dos.pop()
                        self.valor_dos.append('0')

                    elif self.valor_dos[0] == '1':

                        val_interm.append(''.join(self.valor_dos))
                        self.valor_dos.rotate(-1)
                        self.valor_dos.pop()
                        self.valor_dos.append('0')

                        varr = ''.join(self.valor_dos)

                        self.valor_dos.clear()

                        w = 0
                        for y in varr:
                            var = int(y) ^ int(self.byte_sum[w])
                            w += 1
                            self.valor_dos += str(int(var))

                else:
                    if self.valor_dos[0] == '0':

                        self.valor_dos.rotate(-1)
                        self.valor_dos.pop()
                        self.valor_dos.append('0')

                    elif self.valor_dos[0] == '1':

                        self.valor_dos.rotate(-1)
                        self.valor_dos.pop()
                        self.valor_dos.append('0')

                        varr = ''.join(self.valor_dos)

                        self.valor_dos.clear()

                        w = 0
                        for y in varr:
                            var = int(y) ^ int(self.byte_sum[w])
                            w += 1
                            self.valor_dos += str(int(var))


            cprint('Los valores que se suman: {}'.format(val_interm),'red')

            ##  List of lists in each list
            ##  ['01000101', '11010011', '01111000']

            ## [[0,1,0], [1,1,1], [0,0,1] .. ..   ]

            lista_de_elementos = []

            for x in range(8):
                lista_de_elementos.append([int(fila[x]) for fila in val_interm])

            otra_lista = []
            for x in lista_de_elementos:

                numero_unos = x.count(1)
                numero_cero = x.count(0)

                if (numero_unos % 2) == 0:
                    self.multiplicacion += str(0)
                else:
                    self.multiplicacion += str(1)

            cprint("La multiplicacion es: {}".format(self.multiplicacion), 'red')

        print("\n")

    def execute_program(self):
        print("\n-------- SNOW3G/AES-----------\n\n")
        variable = input("En que quieres hacer la multiplicacion? 0-SNOW, 1-AES\n")

        if variable == '0':

            self.primer_byte = input('Introduce el primer byte en hexadecimal a utilizar\n')
            self.segundo_byte = input('Introduce el segundo byte en hexadecimal a utilizar\n')

            self.valor_uno+=bin(int(self.primer_byte, 16))[2:].zfill(8)
            self.valor_dos+=bin(int(self.segundo_byte, 16))[2:].zfill(8)

            if (len(self.valor_uno) or len(self.valor_dos)) != 8:
                raise ValueError('Introduce un valor hexadecimal entre 0 y FF')

            self.byte_sum += "10101001"

            cprint("\nEntradas:",'red')
            cprint("Primer byte: {}".format(self.primer_byte), 'red')
            cprint("Segundo byte: {}".format(self.segundo_byte), 'red')
            cprint("Algoritmo utilizado: SNOW", 'red')

            self.programa_principal()

        elif variable == '1':

            self.primer_byte = input('Introduce el primer byte en hexadecimal a utilizar\n')
            self.segundo_byte = input('Introduce el segundo byte en hexadecimal a utilizar\n')

            self.valor_uno += bin(int(self.primer_byte, 16))[2:].zfill(8)
            self.valor_dos += bin(int(self.segundo_byte, 16))[2:].zfill(8)

            if (len(self.valor_uno) or len(self.valor_dos)) != 8:
                raise ValueError('Introduce un valor hexadecimal entre 0 y FF')

            self.byte_sum += "00011011"


            cprint("Entradas:",'red')
            cprint("Primer byte: {}".format(self.primer_byte), 'red')
            cprint("Segundo byte: {}".format(self.segundo_byte), 'red')
            cprint("Algoritmo utilizado: AES", 'red')

            self.programa_principal()


        else:
            raise ValueError('Se ha introducido un valor incorrecto')




ejemplo = AESSNOW()
# ejemplo.input_datos()
# ejemplo.ksa()
# ejemplo.secuencia_cifrante()
cProfile.run('ejemplo.execute_program()')


