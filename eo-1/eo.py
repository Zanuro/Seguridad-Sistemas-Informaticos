from random import *
import binascii
import sys
from collections import deque
import sys
from termcolor import colored, cprint


class GenBlue:

    def __init__(self, lfsruno=deque([]), lfsrdos=deque([]), lfsrtres=deque([]),lfsrcuatro=deque([]), lfsrcinco = deque([]), semilla = '',bit_m = '',
                 registroa = deque([]), registrob = deque([]),registrot = deque([]), registrott = deque([]), salida = []):

        #Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.

        self.lfsruno = lfsruno
        self.lfsrdos = lfsrdos
        self.lfsrtres = lfsrtres
        self.lfsrcuatro = lfsrcuatro
        self.lfsrcinco = lfsrcinco
        self.semilla = semilla
        self.bit_m = bit_m
        self.registroa = registroa
        self.registrob = registrob
        self.registrot = registrot
        self.registrott = registrott
        self.salida = salida

    def programa_principal(self,size_clave):


        self.semilla += "01"


        for x in range(0, size_clave):

            cprint('Iteracion {}: '.format(x+1), 'cyan')
            print("\n")
            print(('----' * 30).center(180))
            cprint('Pos:    '.center(70), 'cyan', end='  ')
            for z in range(0, 25):
                if z < 10:
                    cprint(z, 'yellow', end='  ')
                else:
                    cprint(z, 'yellow', end=' ')
            print("\n")
            cprint('LFSR1: '.center(70), 'cyan', end='')
            print('[', end=' ')
            for z in range(0, len(self.lfsruno)):

                if z == 7 or z == 11 or z == 19 or z == 24:
                    print(colored('{}'.format(self.lfsruno[z]), 'blue', attrs=['blink']), end='  ')
                else:
                    print(colored('{}'.format(self.lfsruno[z]), 'grey', attrs=['blink']), end='  ')

            print(']', end='  ')
            print("\n")
            print(('----' * 30).center(180))
            cprint('Pos:    '.center(70), 'cyan', end='  ')
            for z in range(0, 31):
                if z < 10:
                    cprint(z, 'yellow', end='  ')
                else:
                    cprint(z, 'yellow', end=' ')
            print("\n")
            cprint('LFSR2: '.center(70), 'cyan', end='')
            print('[', end=' ')
            for z in range(0, len(self.lfsrdos)):

                if z == 11 or z == 15 or z == 23 or z == 30:
                    print(colored('{}'.format(self.lfsrdos[z]), 'blue', attrs=['blink']), end='  ')
                else:
                    print(colored('{}'.format(self.lfsrdos[z]), 'grey', attrs=['blink']), end='  ')

            print(']', end='  ')
            print("\n")
            print(('----' * 30).center(180))
            cprint('Pos:    '.center(70), 'cyan', end='  ')
            for z in range(0, 33):
                if z < 10:
                    cprint(z, 'yellow', end='  ')
                else:
                    cprint(z, 'yellow', end=' ')
            print("\n")

            cprint('LFSR3: '.center(70), 'cyan', end='')
            print('[', end=' ')
            for z in range(0, len(self.lfsrtres)):

                if z == 3 or z == 23 or z == 27 or z == 32:
                    print(colored('{}'.format(self.lfsrtres[z]), 'blue', attrs=['blink']), end='  ')
                else:
                    print(colored('{}'.format(self.lfsrtres[z]), 'grey', attrs=['blink']), end='  ')

            print(']', end='  ')
            print("\n")
            print(('----' * 30).center(180))

            cprint('Pos:    '.center(70), 'cyan', end='  ')
            for z in range(0, 39):
                if z < 10:
                    cprint(z, 'yellow', end='  ')
                else:
                    cprint(z, 'yellow', end=' ')
            print("\n")

            cprint('LFSR4: '.center(70), 'cyan', end='')
            print('[', end=' ')
            for z in range(0, len(self.lfsrcuatro)):

                if z == 3 or z == 27 or z == 35 or z == 38:
                    print(colored('{}'.format(self.lfsrcuatro[z]), 'blue', attrs=['blink']), end='  ')
                else:
                    print(colored('{}'.format(self.lfsrcuatro[z]), 'grey', attrs=['blink']), end='  ')

            print(']', end='  ')
            print("\n")
            print(('----' * 30).center(180))

            cprint('Pos:    '.center(70), 'cyan', end='  ')
            for z in range(0, 39):
                if z < 10:
                    cprint(z, 'yellow', end='  ')
                else:
                    cprint(z, 'yellow', end=' ')
            print("\n")

            cprint('LFSR5: '.center(70), 'cyan', end='')
            print('[', end=' ')
            for z in range(0, len(self.lfsrcinco)):

                if z == 4 or z == 9 or z == 14 or z == 24:
                    print(colored('{}'.format(self.lfsrcinco[z]), 'blue', attrs=['blink']), end='  ')
                else:
                    print(colored('{}'.format(self.lfsrcinco[z]), 'grey', attrs=['blink']), end='  ')

            print(']', end='  ')
            print("\n")
            print(('----' * 30).center(180))
            print("\n")
            print("\n")

            a_t = int(self.lfsruno[7]) ^ int(self.lfsruno[11]) ^ int(self.lfsruno[19]) ^ int(self.lfsruno[24])
            b_t = int(self.lfsrdos[11]) ^ int(self.lfsrdos[15]) ^ int(self.lfsrdos[23]) ^ int(self.lfsrdos[30])
            c_t = int(self.lfsrtres[3]) ^ int(self.lfsrtres[23]) ^ int(self.lfsrtres[27]) ^ int(self.lfsrtres[32])
            d_t = int(self.lfsrcuatro[3]) ^ int(self.lfsrcuatro[27]) ^ int(self.lfsrcuatro[35]) ^ int(self.lfsrcuatro[38])
            e_t = int(self.lfsrcinco[4]) ^ int(self.lfsrcinco[9]) ^ int(self.lfsrcinco[14]) ^ int(self.lfsrcinco[24])

            a_tt = int(self.lfsruno[len(self.lfsruno)-1])
            b_tt = int(self.lfsrdos[len(self.lfsrdos)-1])
            c_tt = int(self.lfsrtres[len(self.lfsrtres)-1])
            d_tt = int(self.lfsrcuatro[len(self.lfsrcuatro)-1])
            e_tt = int(self.lfsrcinco[len(self.lfsrcinco)-1])


            cprint('Ultimos bits de cada registro son: {} {} {} {} {}'.format(a_tt,b_tt,c_tt,d_tt,e_tt), 'red')

            cprint('La semilla de R1 es: {}'.format(self.semilla), 'blue')
            print("\n")

            suma_registros = a_tt+ b_tt+c_tt+d_tt


            if suma_registros > 4 or suma_registros < 0:
                raise ValueError('Se ha producido un error')

             #b = self.semilla[0]

            registro_inv = ''

            registro_inv = self.semilla[:0:-1]
            registro_inv += self.semilla[0]
            self.registroa += registro_inv


            cprint('Registro R1: {}'.format(self.registroa), 'red')

            registro_runo = ''

            registro_runo += str(int(registro_inv,2))


            suma_registross = suma_registros + int(registro_runo)

            if suma_registross > 7 or suma_registross < 0 :
                raise ValueError('Se ha producido un error')

            dividido_dos = "{0:02b}".format(int(suma_registross / 2))

            self.bit_m = str(self.registroa[len(self.registroa)-1])

            cprint('Bit menos significativo de R1: {}'.format(self.bit_m), 'yellow')

            self.salida.append(int(a_tt) ^ int(b_tt) ^ int(c_tt) ^ int(d_tt) ^ int(self.bit_m) ^ int(e_tt))

            for f in self.registroa:

                self.registrot.append(f)

            self.registroa.rotate(1)

            self.registrob = self.registroa

            cprint('Registro R2: {}'.format(self.registrob), 'red')

            # T1(X,Y) = REGA(X,Y)
            # T2(X,Y) = REGB(Y,X ^ Y)

            self.registrott += self.registrob[1]
            self.registrott += str(int(self.registrob[0]) ^ int(self.registrob[1]))

            cprint('Registro T1: {}'.format(self.registrot), 'red')
            cprint('Registro T2: {}'.format(self.registrott), 'red')

            xor1 = ''
            xor2 = ''
            y = 0
            for z in dividido_dos:
                xor1 += str(int(z) ^ int(self.registrott[y]))
                y += 1

            cprint('Salida R1-decimal: {}'.format(registro_runo), 'red')

            cprint('Suma primer registro: {}'.format(suma_registros), 'red')

            cprint('Suma segundo registro: {}'.format(suma_registross), 'red')

            cprint('Registro "/2" : {}'.format(dividido_dos), 'red')

            cprint('XOR 1 entre "/2" y T2: {}'.format(xor1), 'red')

            y = 0
            for z in xor1:
                xor2 += str(int(z) ^ int(self.registrot[y]))
                y += 1

            cprint('XOR 2 entre T1 y XOR1: {}'.format(xor2), 'blue')

            self.semilla = xor2

            cprint('Bit de salida de la {} iteracion es: {}'.format(x+1, self.salida[x]), 'green')

            self.lfsruno.rotate(1)
            self.lfsruno.popleft()
            self.lfsruno.appendleft(a_t)

            self.lfsrdos.rotate(1)
            self.lfsrdos.popleft()
            self.lfsrdos.appendleft(b_t)

            self.lfsrtres.rotate(1)
            self.lfsrtres.popleft()
            self.lfsrtres.appendleft(c_t)

            self.lfsrcuatro.rotate(1)
            self.lfsrcuatro.popleft()
            self.lfsrcuatro.appendleft(d_t)

            self.lfsrcinco.rotate(1)
            self.lfsrcinco.popleft()
            self.lfsrcinco.appendleft(e_t)


            self.registroa.clear()
            self.registrob.clear()
            self.registrot.clear()
            self.registrott.clear()

            print("\n")
            print("\n")

        # a_t = int(self.lfsruno[7]) ^ int(self.lfsruno[11]) ^ int(self.lfsruno[19]) ^ int(self.lfsruno[24])
        # b_t = int(self.lfsrdos[11]) ^ int(self.lfsrdos[15]) ^ int(self.lfsrdos[23]) ^ int(self.lfsrdos[30])
        # c_t = int(self.lfsrtres[3]) ^ int(self.lfsrtres[23]) ^ int(self.lfsrtres[27]) ^ int(self.lfsrtres[32])
        # d_t = int(self.lfsrcuatro[3]) ^ int(self.lfsrcuatro[27]) ^ int(self.lfsrcuatro[35]) ^ int(self.lfsrcuatro[38])
        #
        # a_tt = self.lfsruno[len(self.lfsruno) - 1]
        # b_tt = self.lfsrdos[len(self.lfsrdos) - 1]
        # c_tt = self.lfsrtres[len(self.lfsrtres) - 1]
        # d_tt = self.lfsrcuatro[len(self.lfsrcuatro) - 1]
        #
        # self.salida.append(int(a_tt) ^ int(b_tt) ^ int(c_tt) ^ int(d_tt) ^ int(self.bit_m))
        #
        # cprint('Ultimos bits de cada registro son: {} {} {} {}'.format(a_tt, b_tt, c_tt, d_tt), 'red')
        #
        # cprint('La semilla de R1 es: {}'.format(self.semilla), 'blue')
        #
        # suma_registros = a_tt + b_tt + c_tt + d_tt
        #
        # cprint('Suma primer registro: {}'.format(suma_registros), 'red')



    def execute_program(self):
        print("\n-------- E0-----------\n\n")
        variable = input("Quieres cifrar o descrifrar? 0-Cifrado, 1-Descifrado\n")

        if variable == '0':

            opcion = input('Introduce el mensajes que quieres cifrar: \n')

            clave = []
            for x in opcion:
                varr = '{0:08b}'.format(ord(x), 'b')
                clave += varr

            #print(clave)
            variablee = input("Quieres introducir los registros o aleatorios?(1/0)\n")

            if variablee == '0':

                for x in range(0, 25):
                    self.lfsruno += str(randint(0, 1))

                for x in range(0,31):
                    self.lfsrdos += str(randint(0, 1))

                for x in range(0, 33):
                    self.lfsrtres += str(randint(0, 1))

                for x in range(0, 39):
                    self.lfsrcuatro += str(randint(0, 1))

                for x in range(0,39):
                    self.lfsrcinco += str(1)

                print("\n")
                self.programa_principal(len(clave))

                cprint('\n\n El mensaje a cifrar es : {} \n'.format(clave), 'yellow')
                cprint('\n\n La clave : {} \n'.format(self.salida), 'yellow')

                w = 0
                mensaje_resultante = ''
                for x in self.salida:
                    var = int(x) ^ int(clave[w])
                    w += 1
                    mensaje_resultante += str(int(var))


                mensaje_final = ''.join((chr(int(mensaje_resultante[i:i + 8], 2)) for i in range(0, len(mensaje_resultante), 8)))


                cprint('\n\n El mensaje cifrado es:  {} \n'.format(mensaje_final), 'yellow')

            elif variablee == '1':

                print('Introduce semilla del primer registro(tamano 25)')
                self.lfsruno += str(input())

                if len(self.lfsruno) != 25:
                    raise ValueError('No se ha introducido un registro de tamano 25')

                print('Introduce semilla del segundo registro(tamano 31)')

                self.lfsrdos += str(input())

                if len(self.lfsrdos) != 31:
                    raise ValueError('No se ha introducido un registro de tamano 31')

                print('Introduce semilla del tercer registro(tamano 33)')

                self.lfsrtres += str(input())

                if len(self.lfsrtres) != 33:
                    raise ValueError('No se ha introducido un registro de tamano 33')

                print('Introduce semilla del cuarto registro(tamano 39)')

                self.lfsrcuatro += str(input())

                if len(self.lfsrcuatro) != 39:
                    raise ValueError('No se ha introducido un registro de tamano 39')

                print('Introduce semilla del quinto registro(tamano 39)')

                self.lfsrcinco += str(input())

                if len(self.lfsrcinco) != 39:
                    raise ValueError('No se ha introducido un registro de tamano 39')


                print("\n")
                self.programa_principal(len(clave))

                cprint('\n\n El mensaje a cifrar es : {} \n'.format(clave), 'yellow')
                cprint('\n\n La clave : {} \n'.format(self.salida), 'yellow')

                w = 0
                mensaje_resultante = ''
                for x in self.salida:
                    var = int(x) ^ int(clave[w])
                    w += 1
                    mensaje_resultante += str(int(var))


                mensaje_final = ''.join((chr(int(mensaje_resultante[i:i + 8], 2)) for i in range(0, len(mensaje_resultante), 8)))


                cprint('\n\n El mensaje cifrado es:  {} \n'.format(mensaje_final), 'yellow')

        elif variable == '1':
            opcion = input('Introduce el mensajes que quieres descifrar: \n')

            clave = ''
            for x in opcion:
                varr = '{0:08b}'.format(ord(x), 'b')
                clave += varr

            #print(clave)
            variablee = input("Quieres introducir los registros o aleatorios?(1/0)\n")

            if variablee == '0':

                for x in range(0, 25):
                    self.lfsruno += str(randint(0, 1))

                for x in range(0,31):
                    self.lfsrdos += str(randint(0, 1))

                for x in range(0, 33):
                    self.lfsrtres += str(randint(0, 1))

                for x in range(0, 39):
                    self.lfsrcuatro += str(randint(0, 1))

                for x in range(0,39):
                    self.lfsrcinco += str(1)

                print("\n")
                self.programa_principal(len(clave))

                cprint('\n\n El mensaje a descifrar es : {} \n'.format(clave), 'yellow')
                cprint('\n\n La clave es : {} \n'.format(self.salida), 'yellow')

                w = 0
                mensaje_resultante = ''
                for x in self.salida:
                    var = int(x) ^ int(clave[w])
                    w += 1
                    mensaje_resultante += str(int(var))

                mensaje_final = ''.join((chr(int(mensaje_resultante[i:i + 8], 2)) for i in range(0, len(mensaje_resultante), 8)))

                cprint('\n\n El mensaje original es:  {} \n'.format(mensaje_final), 'yellow')

            elif variablee == '1':

                print('Introduce semilla del primer registro(tamano 25)')
                self.lfsruno += str(input())

                if len(self.lfsruno) != 25:
                    raise ValueError('No se ha introducido un registro de tamano 25')

                print('Introduce semilla del segundo registro(tamano 31)')

                self.lfsrdos += str(input())

                if len(self.lfsrdos) != 31:
                    raise ValueError('No se ha introducido un registro de tamano 31')

                print('Introduce semilla del tercer registro(tamano 33)')

                self.lfsrtres += str(input())

                if len(self.lfsrtres) != 33:
                    raise ValueError('No se ha introducido un registro de tamano 33')

                print('Introduce semilla del cuarto registro(tamano 39)')

                self.lfsrcuatro += str(input())

                if len(self.lfsrcuatro) != 39:
                    raise ValueError('No se ha introducido un registro de tamano 39')

                print('Introduce semilla del quinto registro(tamano 39)')

                self.lfsrcinco += str(input())

                if len(self.lfsrcinco) != 39:
                    raise ValueError('No se ha introducido un registro de tamano 39')

                print("\n")
                self.programa_principal(len(clave))
                cprint('\n\n El mensaje a descifrar es : {} \n'.format(clave), 'yellow')
                cprint('\n\n La clave es : {} \n'.format(self.salida), 'yellow')

                w = 0
                mensaje_resultante = ''
                for x in self.salida:
                    var = int(x) ^ int(clave[w])
                    w += 1
                    mensaje_resultante += str(int(var))

                mensaje_final = ''.join((chr(int(mensaje_resultante[i:i + 8], 2)) for i in range(0, len(mensaje_resultante), 8)))

                cprint('\n\n El mensaje original es:  {} \n'.format(mensaje_final), 'yellow')

        else:
            print("Se ha introducido un valor incorrecto\n")
            return



ejemplo = GenBlue()
# ejemplo.input_datos()
# ejemplo.ksa()
# ejemplo.secuencia_cifrante()
ejemplo.execute_program()

