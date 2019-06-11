from random import *
import binascii
import sys
from collections import deque
import sys
from termcolor import colored, cprint


class GENACINCO:

    def __init__(self, lfsruno=deque([]), lfsrdos=deque([]), lfsrtres=deque([]), pos_func_mayoria=[], funcion_mayoria=0, salida=[], secuencia_salida=[]):

        #Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.

        self.lfsruno = lfsruno
        self.lfsrdos = lfsrdos
        self.lfsrtres = lfsrtres
        self.pos_func_mayoria = pos_func_mayoria
        self.funcion_mayoria = funcion_mayoria
        self.salida = salida
        self.secuencia_salida = secuencia_salida

    def input_datos(self):

        print("\n")
        cprint('Iteracion 1: ', 'cyan')
        print("\n")
        cprint('-----------Registros iniciales-----------'.center(200), 'yellow')
        print("\n")
        print("\n")


        print(('----' * 30).center(180))
        cprint('Pos:    '.center(70),'cyan', end = '  ')
        for x in range(19, 0, -1):
            if x < 10:
                cprint(x,'yellow', end = '  ')
            else:
                cprint(x, 'yellow', end=' ')
        print("\n")
        cprint('LFSR1: '.center(70), 'cyan', end= '')
        print('[', end=' ')
        for x in range(len(self.lfsruno), 0, -1):
            if x == 9:
                print(colored('{}'.format(self.lfsruno[x-1]), 'red', attrs=['bold','blink']), end = '  ')
            elif x == 19 or x == 18 or x == 17 or x == 14:
                print(colored('{}'.format(self.lfsruno[x-1]), 'blue', attrs=['bold','blink']), end = '  ')
            else:
                print(colored('{}'.format(self.lfsruno[x-1]), 'grey', attrs=['blink']), end = '  ')
        print(']', end = '  ')
        print("\n")
        print(('----'*30).center(180))
        cprint('Pos:    '.center(70), 'cyan', end='  ')
        for x in range(22, 0, -1):
            if x < 10:
                cprint(x, 'yellow', end='  ')
            else:
                cprint(x, 'yellow', end=' ')
        print("\n")
        cprint('LFSR2: '.center(70), 'cyan', end='')
        print('[', end=' ')
        for x in range(len(self.lfsrdos), 0, -1):
            if x == 11:
                print(colored('{}'.format(self.lfsrdos[x-1]), 'red', attrs=['bold','blink']), end = '  ')
            elif x == 21 or x == 22:
                print(colored('{}'.format(self.lfsrdos[x-1]), 'blue', attrs=['bold','blink']), end = '  ')
            else:
                print(colored('{}'.format(self.lfsrdos[x-1]), 'grey', attrs=['blink']), end = '  ')
        print(']', end='  ')
        print("\n")
        print(('----' * 30).center(180))
        cprint('Pos:    '.center(70), 'cyan', end='  ')
        for x in range(23, 0, -1):
            if x < 10:
                cprint(x, 'yellow', end='  ')
            else:
                cprint(x, 'yellow', end=' ')
        print("\n")

        cprint('LFSR3: '.center(70), 'cyan', end='')
        print('[', end=' ')
        for x in range(len(self.lfsrtres), 0, -1):
            if x == 11:
                print(colored('{}'.format(self.lfsrtres[x-1]), 'red', attrs=['bold','blink']), end = '  ')
            elif x == 8 or x == 21 or x == 22 or x == 23:
                print(colored('{}'.format(self.lfsrtres[x-1]), 'blue', attrs=['bold','blink']), end = '  ')
            else:
                print(colored('{}'.format(self.lfsrtres[x-1]), 'grey', attrs=['blink']), end = '  ')
        print(']', end='  ')
        print("\n")
        print(('----' * 30).center(180))

        # cprint(str(self.lfsruno).center(150), 'white')
        # print(str(self.lfsrdos).center(165))
        # print(str(self.lfsrtres).center(170))

        #print('Las posiciones para la funcion mayoria a utilizar son: 9 11 11')
        self.pos_func_mayoria.append(8)
        self.pos_func_mayoria.append(10)
        self.pos_func_mayoria.append(10)


    def funcion_mayoriaa(self):

        a = (int(self.lfsruno[self.pos_func_mayoria[0]]) * int(self.lfsrdos[self.pos_func_mayoria[1]]))
        b = (int(self.lfsruno[self.pos_func_mayoria[0]]) * int(self.lfsrtres[self.pos_func_mayoria[2]]))
        c = (int(self.lfsrdos[self.pos_func_mayoria[1]]) * int(self.lfsrtres[self.pos_func_mayoria[2]]))

        self.funcion_mayoria = a ^ b ^ c
        self.salida.append(self.funcion_mayoria)

        cprint("F({} {} {} ) = {}".format(self.lfsruno[self.pos_func_mayoria[0]], self.lfsrdos[self.pos_func_mayoria[1]],
              self.lfsrtres[self.pos_func_mayoria[2]], self.funcion_mayoria).center(200),'red')
        # print('F(', self.lfsruno[self.pos_func_mayoria[0]], self.lfsrdos[self.pos_func_mayoria[1]],
        #       self.lfsrtres[self.pos_func_mayoria[2]], ') = ', self.funcion_mayoria)

    def programa_principal(self,size_clave):

        # print(self.lfsruno)
        # print(self.lfsrdos)
        # print(self.lfsrtres)

        for x in range(1, size_clave):
            a_t = int(self.lfsruno[13]) ^ int(self.lfsruno[16]) ^ int(self.lfsruno[17]) ^ int(self.lfsruno[18])
            b_t = int(self.lfsrdos[20]) ^ int(self.lfsrdos[21])
            c_t = int(self.lfsrtres[7]) ^ int(self.lfsrtres[20]) ^ int(self.lfsrtres[21]) ^ int(self.lfsrtres[22])

            a_tt = self.lfsruno[len(self.lfsruno)-1]
            b_tt = self.lfsrdos[len(self.lfsrdos)-1]
            c_tt = self.lfsrtres[len(self.lfsrtres)-1]
            varr = int(self.lfsruno[len(self.lfsruno)-1]) ^ int(self.lfsrdos[len(self.lfsrdos)-1]) ^ int(self.lfsrtres[len(self.lfsrtres)-1])
            self.secuencia_salida.append(str(varr))
            self.funcion_mayoriaa()

            flag_d = False

            if(self.funcion_mayoria == int(self.lfsruno[self.pos_func_mayoria[0]])):
                self.lfsruno.rotate(1)
                self.lfsruno.popleft()
                self.lfsruno.appendleft(str(a_t))

            else:
                cprint('Registro uno queda paralizado'.center(200),'red')
                cprint('Z = {} ^ {} ^ {} = {}'.format(a_tt, b_tt, c_tt, varr).center(200), 'red')
                flag_d = True

            if (self.funcion_mayoria == int(self.lfsrdos[self.pos_func_mayoria[1]])):
                self.lfsrdos.rotate(1)
                self.lfsrdos.popleft()
                self.lfsrdos.appendleft(str(b_t))

            else:
                cprint('Registro dos queda paralizado'.center(200),'red')
                cprint('Z = {} ^ {} ^ {} = {}'.format(a_tt, b_tt, c_tt, varr).center(200), 'red')
                flag_d = True

            if (self.funcion_mayoria == int(self.lfsrtres[self.pos_func_mayoria[2]])):
                self.lfsrtres.rotate(1)
                self.lfsrtres.popleft()
                self.lfsrtres.appendleft(str(c_t))

            else:
                cprint('Registro tres queda paralizado'.center(200),'red')
                cprint('Z = {} ^ {} ^ {} = {}'.format(a_tt, b_tt, c_tt, varr).center(200), 'red')
                flag_d = True


            if(flag_d == False):
                cprint('Ningun registro queda paralizado'.center(200),'red')
                cprint('Z = {} ^ {} ^ {} = {}'.format(a_tt, b_tt, c_tt, varr).center(200), 'red')


            print("\n")
            cprint('Iteracion {}:'.format(x+1), 'cyan')
            print("\n")

            print(('----' * 30).center(180))
            cprint('Pos:    '.center(70), 'cyan', end='  ')
            for x in range(19, 0, -1):
                if x < 10:
                    cprint(x, 'yellow', end='  ')
                else:
                    cprint(x, 'yellow', end=' ')
            print("\n")
            cprint('LFSR1: '.center(70), 'cyan', end='')
            print('[', end=' ')
            for x in range(len(self.lfsruno), 0, -1):
                if x == 9:
                    print(colored('{}'.format(self.lfsruno[x - 1]), 'red', attrs=['bold', 'blink']), end='  ')
                elif x == 19 or x == 18 or x == 17 or x == 14:
                    print(colored('{}'.format(self.lfsruno[x - 1]), 'blue', attrs=['bold', 'blink']), end='  ')
                else:
                    print(colored('{}'.format(self.lfsruno[x - 1]), 'grey', attrs=['blink']), end='  ')
            print(']', end='  ')
            print("\n")
            print(('----' * 30).center(180))
            cprint('Pos:    '.center(70), 'cyan', end='  ')
            for x in range(22, 0, -1):
                if x < 10:
                    cprint(x, 'yellow', end='  ')
                else:
                    cprint(x, 'yellow', end=' ')
            print("\n")
            cprint('LFSR2: '.center(70), 'cyan', end='')
            print('[', end=' ')
            for x in range(len(self.lfsrdos), 0, -1):
                if x == 11:
                    print(colored('{}'.format(self.lfsrdos[x - 1]), 'red', attrs=['bold', 'blink']), end='  ')
                elif x == 21 or x == 22:
                    print(colored('{}'.format(self.lfsrdos[x - 1]), 'blue', attrs=['bold', 'blink']), end='  ')
                else:
                    print(colored('{}'.format(self.lfsrdos[x - 1]), 'grey', attrs=['blink']), end='  ')
            print(']', end='  ')
            print("\n")
            print(('----' * 30).center(180))
            cprint('Pos:    '.center(70), 'cyan', end='  ')
            for x in range(23, 0, -1):
                if x < 10:
                    cprint(x, 'yellow', end='  ')
                else:
                    cprint(x, 'yellow', end=' ')
            print("\n")

            cprint('LFSR3: '.center(70), 'cyan', end='')
            print('[', end=' ')
            for x in range(len(self.lfsrtres), 0, -1):
                if x == 11:
                    print(colored('{}'.format(self.lfsrtres[x - 1]), 'red', attrs=['bold', 'blink']), end='  ')
                elif x == 8 or x == 21 or x == 22 or x == 23:
                    print(colored('{}'.format(self.lfsrtres[x - 1]), 'blue', attrs=['bold', 'blink']), end='  ')
                else:
                    print(colored('{}'.format(self.lfsrtres[x - 1]), 'grey', attrs=['blink']), end='  ')
            print(']', end='  ')
            print("\n")
            print(('----' * 30).center(180))
            print("\n")

        a_t = int(self.lfsruno[13]) ^ int(self.lfsruno[16]) ^ int(self.lfsruno[17]) ^ int(self.lfsruno[18])
        b_t = int(self.lfsrdos[20]) ^ int(self.lfsrdos[21])
        c_t = int(self.lfsrtres[7]) ^ int(self.lfsrtres[20]) ^ int(self.lfsrtres[21]) ^ int(self.lfsrtres[22])

        a_tt = self.lfsruno[len(self.lfsruno) - 1]
        b_tt = self.lfsrdos[len(self.lfsrdos) - 1]
        c_tt = self.lfsrtres[len(self.lfsrtres) - 1]
        varr = int(self.lfsruno[len(self.lfsruno) - 1]) ^ int(self.lfsrdos[len(self.lfsrdos) - 1]) ^ int(self.lfsrtres[len(self.lfsrtres) - 1])
        self.secuencia_salida.append(str(varr))
        self.funcion_mayoriaa()

        flag_d = False

        if (self.funcion_mayoria == int(self.lfsruno[self.pos_func_mayoria[0]])):
            self.lfsruno.rotate(1)
            self.lfsruno.popleft()
            self.lfsruno.appendleft(str(a_t))

        else:
            cprint('Registro uno queda paralizado'.center(200), 'red')
            cprint('Z = {} ^ {} ^ {} = {}'.format(a_tt, b_tt, c_tt, varr).center(200), 'red')
            flag_d = True

        if (self.funcion_mayoria == int(self.lfsrdos[self.pos_func_mayoria[1]])):
            self.lfsrdos.rotate(1)
            self.lfsrdos.popleft()
            self.lfsrdos.appendleft(str(b_t))

        else:
            cprint('Registro dos queda paralizado'.center(200), 'red')
            cprint('Z = {} ^ {} ^ {} = {}'.format(a_tt, b_tt, c_tt, varr).center(200), 'red')
            flag_d = True

        if (self.funcion_mayoria == int(self.lfsrtres[self.pos_func_mayoria[2]])):
            self.lfsrdos.rotate(1)
            self.lfsrdos.popleft()
            self.lfsrdos.appendleft(str(c_t))

        else:
            cprint('Registro tres queda paralizado'.center(200), 'red')
            cprint('Z = {} ^ {} ^ {} = {}'.format(a_tt, b_tt, c_tt, varr).center(200), 'red')
            flag_d = True

        if (flag_d == False):
            cprint('Ningun registro queda paralizado'.center(200), 'red')
            cprint('Z = {} ^ {} ^ {} = {}'.format(a_tt, b_tt, c_tt, varr).center(200), 'red')


    def execute_program(self):
        print("\n-------- A5-----------\n\n")
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

                a = ''
                for x in range(1, 20):
                    a += str(randint(0, 1))
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                self.lfsruno += reversed
                a = ''
                for x in range(1, 23):
                    a += str(randint(0, 1))
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                self.lfsrdos += reversed

                a = ''
                for x in range(1, 24):
                    a += str(randint(0, 1))
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                self.lfsrtres += reversed

                self.input_datos()
                print("\n")
                self.programa_principal(len(clave))

                cprint('\n\n El mensaje a cifrar es : {} \n'.format(clave), 'yellow')
                cprint('\n\n La clave : {} \n'.format(self.secuencia_salida), 'yellow')

                w = 0
                mensaje_resultante = ''
                for x in self.secuencia_salida:
                    var = int(x) ^ int(clave[w])
                    w += 1
                    mensaje_resultante += str(int(var))


                #cprint('\n\n La secuencia binaria es : {} \n'.format(mensaje_resultante), 'yellow')


                mensaje_final = ''.join((chr(int(mensaje_resultante[i:i + 8], 2)) for i in range(0, len(mensaje_resultante), 8)))


                cprint('\n\n El mensaje cifrado es:  {} \n'.format(mensaje_final), 'yellow')
            elif variablee == '1':
                a = ''
                print('Introduce semilla del primer registro(tamano 19)')
                a += str(input())
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                #print(reversed)
                self.lfsruno += reversed
                #print(self.lfsruno)

                if len(self.lfsruno) != 19:
                    raise ValueError('No se ha introducido un registro de tamano 19')

                print('Introduce semilla del segundo registro(tamano 22)')
                a=''
                a += str(input())
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                #print(reversed)
                self.lfsrdos += reversed
                #print(self.lfsrdos)

                if len(self.lfsrdos) != 22:
                    raise ValueError('No se ha introducido un registro de tamano 22')

                print('Introduce semilla del tercer registro(tamano 23)')
                a=''
                a += str(input())
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                #print(reversed)
                self.lfsrtres += reversed
                #print(self.lfsrtres)

                if len(self.lfsrtres) != 23:
                    raise ValueError('No se ha introducido un registro de tamano 23')

                self.input_datos()
                print("\n")
                self.programa_principal(len(clave))
                cprint('\n\n El mensaje a cifrar es : {} \n'.format(clave), 'yellow')
                cprint('\n\n La clave : {} \n'.format(self.secuencia_salida), 'yellow')

                w = 0
                mensaje_resultante = ''
                for x in self.secuencia_salida:
                    var = int(x) ^ int(clave[w])
                    w += 1
                    mensaje_resultante += str(int(var))

                #cprint('\n\n La secuencia binaria es : {} \n'.format(mensaje_resultante), 'yellow')

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

                a = ''
                for x in range(1, 20):
                    a += str(randint(0, 1))
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                self.lfsruno += reversed
                a = ''
                for x in range(1, 23):
                    a += str(randint(0, 1))
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                self.lfsrdos += reversed

                a = ''
                for x in range(1, 24):
                    a += str(randint(0, 1))
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                self.lfsrtres += reversed

                self.input_datos()
                print("\n")
                self.programa_principal(len(clave))
                cprint('\n\n El mensaje a descifrar es : {} \n'.format(clave), 'yellow')
                cprint('\n\n La clave es : {} \n'.format(self.secuencia_salida), 'yellow')

                w = 0
                mensaje_resultante = ''
                for x in self.secuencia_salida:
                    var = int(x) ^ int(clave[w])
                    w += 1
                    mensaje_resultante += str(int(var))

                #cprint('\n\n La secuencia binaria es : {} \n'.format(mensaje_resultante), 'yellow')

                mensaje_final = ''.join((chr(int(mensaje_resultante[i:i + 8], 2)) for i in range(0, len(mensaje_resultante), 8)))

                cprint('\n\n El mensaje original es:  {} \n'.format(mensaje_final), 'yellow')
            elif variablee == '1':
                a = ''
                print('Introduce semilla del primer registro(tamano 19)')
                a += str(input())
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                # print(reversed)
                self.lfsruno += reversed
                # print(self.lfsruno)

                if len(self.lfsruno) != 19:
                    raise ValueError('No se ha introducido un registro de tamano 19')

                print('Introduce semilla del segundo registro(tamano 22)')
                a = ''
                a += str(input())
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                # print(reversed)
                self.lfsrdos += reversed
                # print(self.lfsrdos)

                if len(self.lfsrdos) != 22:
                    raise ValueError('No se ha introducido un registro de tamano 22')

                print('Introduce semilla del tercer registro(tamano 23)')
                a = ''
                a += str(input())
                b = a[0]
                reversed = a[:0:-1]
                reversed += str(b)
                # print(reversed)
                self.lfsrtres += reversed
                # print(self.lfsrtres)

                if len(self.lfsrtres) != 23:
                    raise ValueError('No se ha introducido un registro de tamano 23')

                self.input_datos()
                print("\n")
                self.programa_principal(len(clave))
                cprint('\n\n El mensaje a descifrar es : {} \n'.format(clave), 'yellow')
                cprint('\n\n La clave es : {} \n'.format(self.secuencia_salida), 'yellow')

                w = 0
                mensaje_resultante = ''
                for x in self.secuencia_salida:
                    var = int(x) ^ int(clave[w])
                    w += 1
                    mensaje_resultante += str(int(var))

                #cprint('\n\n La secuencia binaria es : {} \n'.format(mensaje_resultante), 'yellow')
                mensaje_final = ''.join((chr(int(mensaje_resultante[i:i + 8], 2)) for i in range(0, len(mensaje_resultante), 8)))

                cprint('\n\n El mensaje original es:  {} \n'.format(mensaje_final), 'yellow')

        else:
            print("Se ha introducido un valor incorrecto\n")
            return


ejemplo = GENACINCO()
# ejemplo.input_datos()
# ejemplo.ksa()
# ejemplo.secuencia_cifrante()
ejemplo.execute_program()

