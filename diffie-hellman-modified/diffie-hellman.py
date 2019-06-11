from random import *
import binascii
import sys
from collections import deque
import sys
from termcolor import colored, cprint
import cProfile


class DiffieHellman:

    def __init__(self, secreto_uno = 0, secreto_dos = 0, numero_primo = 0, numero_base = 0, numero_in_uno=0,
                 numero_in_dos = 0, clave_comun = 0,array_usuarios = [],array_claves_secretas=[],array_claves_publicas=[],clave_sesion=[]):

        #Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.

        self.secreto_uno = secreto_uno
        self.secreto_dos = secreto_dos
        self.numero_primo = numero_primo
        self.numero_base = numero_base
        self.numero_in_uno = numero_in_uno
        self.numero_in_dos = numero_in_dos
        self.clave_comun = clave_comun
        self.array_usuarios = array_usuarios
        self.array_claves_secretas = array_claves_secretas
        self.array_claves_publicas = array_claves_publicas
        self.clave_sesion = clave_sesion

    def exponent(self, base, secreto):

        resultado = 1

        comienzo_base = base % int(self.numero_primo)

        while(secreto > 0) and (comienzo_base > 1):

            if secreto % 2 == 1:
                resultado = (resultado * comienzo_base) % int(self.numero_primo)
                secreto -= 1

            else:
                comienzo_base = pow(comienzo_base,2) % int(self.numero_primo)
                secreto /= 2

        return resultado

    def is_prime(self, num):
        if num < 2:
            return False
        elif num != 2 and num % 2 == 0:
            return False
        else:
            return all(num % x for x in range(3, int(num ** 0.5) + 1))

    def execute_program(self):
        print("\n-------- Diffie-Hellman-----------\n\n")
        self.numero_primo = input("Introduce el numero primo(p) a utilizar\n")

        if int(self.numero_primo) < 1:
            raise ValueError('Se ha introducido un valor negativo o 0')

        comp = self.is_prime(int(self.numero_primo))

        if comp is False:
            raise ValueError('Se ha introducido un valor no primo')


        self.numero_base = input("Introduce la base(a) a utilizar\n")

        if int(self.numero_base) >= int(self.numero_primo):
            raise ValueError('El valor de la base tiene que ser < que el valor del numero primo del modulo')

        elif int(self.numero_base) < 1:
            raise ValueError('La base introducida no puede ser negativa o 0')

        numero_usuarios = input('Introduce el numero de usuarios\n')

        if int(numero_usuarios) % 2 == 0:
            pass
        else:
            raise ValueError('No se ha introducido un numero par de usuarios')


        numero_pares = int(numero_usuarios)/2

        i = 0
        for x in range(0,int(numero_pares)):

            print('====Pareja {} =====\n'.format(x+1))
            self.secreto_uno = input("Introduce el secreto del primer usuario de la pareja {}\n".format(x+1))
            self.array_claves_secretas.append(self.secreto_uno)


            self.numero_in_uno = self.exponent(int(self.numero_base), int(self.secreto_uno))
            self.array_claves_publicas.append(self.numero_in_uno)

            self.secreto_dos = input("Introduce el secreto del segundo usuario de la pareja {}\n".format(x+1))
            self.array_claves_secretas.append(self.secreto_dos)

            self.numero_in_dos = self.exponent(int(self.numero_base), int(self.secreto_dos))

            self.array_claves_publicas.append(self.numero_in_dos)

            cprint("\nEntradas:",'red')
            cprint("P: {}".format(self.numero_primo), 'red')
            cprint("A: {}".format(self.numero_base), 'red')
            cprint("XA: {}".format(self.array_claves_secretas[x+i]), 'red')
            cprint("XB: {}\n".format(self.array_claves_secretas[x+1+i]), 'red')

            print("---------------")
            cprint("YA: {}^{} mod {} = {}\n".format(self.numero_base,self.array_claves_secretas[x+i],self.numero_primo,self.array_claves_publicas[x+i]), 'red')
            cprint("YB: {}^{} mod {} = {}\n".format(self.numero_base,self.array_claves_secretas[x+1+i],self.numero_primo,self.array_claves_publicas[x+1+i]), 'red')
            print("---------------\n")

            clave1 = self.exponent(int(self.array_claves_publicas[x+1+i]),int(self.array_claves_secretas[x+i]))
            self.clave_sesion.append(clave1)
            clave2 = self.exponent(int(self.array_claves_publicas[x+i]),int(self.array_claves_secretas[x+1+i]))
            self.clave_sesion.append(clave2)

            if self.clave_sesion[x+i] != self.clave_sesion[x+1+i]:
                raise ValueError('Se ha producido un error')

            else:
                self.clave_comun = self.clave_sesion[x]
                cprint("K: {}^{} mod {} = {}".format(self.array_claves_publicas[x+1+i],self.array_claves_secretas[x+i],self.numero_primo,self.clave_comun), 'red')
                cprint("K: {}^{} mod {} = {}\n\n".format(self.array_claves_publicas[x+i],self.array_claves_secretas[x+1+i],self.numero_primo,self.clave_comun), 'red')

            i += 1

        print(self.array_claves_secretas)
        print(self.array_claves_publicas)
        print(self.clave_sesion)

        pareja=input('\nQue pareja quieres utilizar para cifrar/descrifrar?(0-3)\n\n')
        if int(pareja) >= 0 and int(pareja) < 4:

            print('Se ha escogido la pareja {}\n\n'.format(int(pareja)))

            print('------Cifrado----\n\n')
            mensaje_a_cifrar = input('Introduce el mensaje a cifrar\n')
            print(mensaje_a_cifrar)
            print('Clave a utilizar: {}'.format(self.clave_sesion[int(pareja)*2]))

            sec_cifr_bin = '{0:08b}'.format(self.clave_sesion[int(pareja)*2], 'b')

            otro = ''
            y = 0
            for z in mensaje_a_cifrar:
                var = int(z) ^ int(sec_cifr_bin[y])
                y += 1
                otro += str(var)

            print('Mensaje cifrado : {}\n\n'.format(otro))

            print('------Descifrado----\n\n')
            mensaje_a_descifrar = input('Introduce el mensaje a desccifrar\n\n')
            print(mensaje_a_descifrar)
            print('Clave a utilizar: {}'.format(self.clave_sesion[(int(pareja)*2)+1]))

            sec_cifr_bin = '{0:08b}'.format(self.clave_sesion[(int(pareja)*2)+1], 'b')

            otro = ''
            y = 0
            for z in mensaje_a_descifrar:
                var = int(z) ^ int(sec_cifr_bin[y])
                y += 1
                otro += str(var)

            print('Mensaje original : {}\n\n'.format(otro))

ejemplo = DiffieHellman()
# ejemplo.input_datos()
# ejemplo.ksa()
# ejemplo.secuencia_cifrante()
cProfile.run('ejemplo.execute_program()')


