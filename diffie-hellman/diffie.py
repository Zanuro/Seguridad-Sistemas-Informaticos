from random import *
import binascii
import sys
from collections import deque
import sys
from termcolor import colored, cprint
import cProfile


class DiffieHellman:

    def __init__(self, secreto_uno = 0, secreto_dos = 0, numero_primo = 0, numero_base = 0, numero_in_uno=0,
                 numero_in_dos = 0, clave_comun = 0):

        #Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.

        self.secreto_uno = secreto_uno
        self.secreto_dos = secreto_dos
        self.numero_primo = numero_primo
        self.numero_base = numero_base
        self.numero_in_uno = numero_in_uno
        self.numero_in_dos = numero_in_dos
        self.clave_comun = clave_comun

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

        self.secreto_uno = input("Introduce el primer secreto\n")

        self.numero_in_uno = self.exponent(int(self.numero_base), int(self.secreto_uno))

        self.secreto_dos = input("Introduce el segundo secreto\n")

        self.numero_in_dos = self.exponent(int(self.numero_base), int(self.secreto_dos))

        cprint("\nEntradas:",'red')
        cprint("P: {}".format(self.numero_primo), 'red')
        cprint("A: {}".format(self.numero_base), 'red')
        cprint("XA: {}".format(self.secreto_uno), 'red')
        cprint("XB: {}\n".format(self.secreto_dos), 'red')


        print("---------------")
        cprint("YA: {}^{} mod {} = {}\n".format(self.numero_base,self.secreto_uno,self.numero_primo,self.numero_in_uno), 'red')
        cprint("YB: {}^{} mod {} = {}\n".format(self.numero_base,self.secreto_dos,self.numero_primo,self.numero_in_dos), 'red')
        print("---------------\n")

        clave1 = self.exponent(int(self.numero_in_dos),int(self.secreto_uno))
        clave2 = self.exponent(int(self.numero_in_uno),int(self.secreto_dos))

        if clave1 != clave2:
            raise ValueError('Se ha producido un error')

        else:
            self.clave_comun = clave1
            cprint("K: {}^{} mod {} = {}".format(self.numero_in_dos,self.secreto_uno,self.numero_primo,self.clave_comun), 'red')
            cprint("K: {}^{} mod {} = {}\n\n".format(self.numero_in_uno,self.secreto_dos,self.numero_primo,self.clave_comun), 'red')


ejemplo = DiffieHellman()
# ejemplo.input_datos()
# ejemplo.ksa()
# ejemplo.secuencia_cifrante()
cProfile.run('ejemplo.execute_program()')


