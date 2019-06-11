import sys
import random
from math import *
from termcolor import colored, cprint
import cProfile


class FiatShamir:

    def __init__(self,prime_one=0,prime_two=0,N=0,secret=0,public=0,compromisos=[],testigo=[],random_bit=random.randint(0,1),responses=[]):
        self.prime_one = prime_one
        self.prime_two = prime_two
        self.N = N
        self.secret = secret
        self.public = public
        self.compromisos = compromisos
        self.testigo = testigo
        self.random_bit = random_bit
        self.responses = responses

    def exponent(self, base, potencia ,modulo):

        resultado = 1

        comienzo_base = base % int(modulo)

        while (potencia > 0) and (comienzo_base > 1):

            if potencia % 2 == 1:
                resultado = (resultado * comienzo_base) % int(modulo)
                potencia -= 1

            else:
                comienzo_base = pow(comienzo_base, 2) % int(modulo)
                potencia /= 2

        return resultado

    def is_prime(self, num):
        if num < 2:
            return False

        elif num != 2 and num % 2 == 0:
            return False
        else:
            return all(num % x for x in range(3, int(num ** 0.5) + 1))

    def co_prime(self, a, b):

        while b != 0:
            (a, b) = (b, a % b)
        return a


    comprobacion = True

    def execute_program(self):

        print('*******Fiat-Shamir******\n')

        opcion = input('Quieres introducir los primos o random?(0/1)\n')

        if opcion == '0':

            self.prime_one = int(input('Introduce el primer numero primo\n'))
            self.prime_two = int(input('Introduce el segundo numero primo\n'))

            if self.prime_one == self.prime_two:
                raise ValueError('Los dos primos tienen el mismo valor\n')

            elif self.is_prime(self.prime_one) is False or self.is_prime(self.prime_two) is False:
                raise ValueError('Uno o ambos valores introducidos no son primos')

        elif opcion == '1':
            minPrime = 100
            maxPrime = 5000
            cached_primes = [i for i in range(minPrime, maxPrime) if self.is_prime(i)]
            #print(cached_primes)

            self.prime_one = random.choice(cached_primes)
            print('El primer numero primo: {}\n'.format(self.prime_one))
            self.prime_two = random.choice(cached_primes)
            print('El segundo numero primo: {}\n'.format(self.prime_two))

            if self.prime_one == self.prime_two:
                raise ValueError('Los dos primos tienen el mismo valor\n')

        else:
            raise ValueError('Opcion incorrecta\n')


        self.N = int(self.prime_one) * int(self.prime_two)

        print('La N es: {}\n'.format(self.N))

        opcion = input('Quieres introducir el numero secreto o random(s)?(0/1)\n')

        if opcion == '0':

            self.secret = int(input('Introduce el numero secreto\n'))

            if self.secret <= 0 or self.secret >= self.N:

                raise ValueError('El valor tiene que ser entre 1 y {}\n'.format(self.N-1))

            elif self.co_prime(self.N,self.secret) != 1:
                raise ValueError('Se ha introducido un valor que no es co-primo con {}'.format(self.N))


        elif opcion == '1':
            secret_primes = [i for i in range(1, self.N) if self.co_prime(self.N, i) == 1]
            # print(secret_primes

            self.secret = random.choice(secret_primes)

        else:
            raise ValueError('Opcion incorrecta\n')


        print('La identificacion secreta es: {}\n'.format(self.secret))


        self.public = self.exponent(self.secret,2,self.N)

        print('La identificacion publica es: {}\n'.format(int(self.public)))


        numero_iteraciones  = input('Cuantas veces quiere realizar la comprobacion?\n')

        for x in range(0,int(numero_iteraciones)):

            print('Iteracion {}\n'.format(x+1))

            lista_compromisos = []

            opcion = input('Quieres introducir el numero secreto o random(Compromiso secreto de A(x)?(0/1)\n')

            if opcion == '0':

                self.compromisos = int(input('Introduce el numero secreto\n'))

                if self.compromisos <= 0 or self.compromisos >= self.N:

                    raise ValueError('El valor tiene que ser entre 1 y {}\n'.format(self.N - 1))

            elif opcion == '1':
                #compromiso = [i for i in range(1, self.N)]
                self.compromisos = random.randrange(1,self.N-1)
                #print(self.compromisos)

            else:
                raise ValueError('Opcion incorrecta\n')


            print('El compromiso escogido es: {}\n'.format(self.compromisos))

            self.testigo = self.exponent(int(self.compromisos), 2, self.N)

            print('El testigo enviado es: {}\n'.format(int(self.testigo)))

            opcion = input('Quieres introducir el bit e (Reto de B a A) o random?(0/1)\n')

            if opcion == '0':

                self.random_bit = input('Introduce el bit e(0/1)\n')


                if self.random_bit != '0' and self.random_bit != '1':
                    raise ValueError('El valor tiene que ser 0 o 1')

            elif opcion == '1':
                self.random_bit = random.randint(0, 1)

            else:
                raise ValueError('Opcion incorrecta\n')


            print('El Reto es: {}\n'.format(self.random_bit))

            if(int(self.random_bit) == 0):

                response = int(input('Introduce el valor para comprobar identidad\n'))
                response_t = int(response) % self.N

                #print(response_t)

                if(response_t != self.compromisos % self.N):
                    comprobacion = False
                    print('Respuesta es: {}'.format(response_t))

                else:
                    comprobacion = True
                    print('Respuesta es: {}'.format(response_t))

            elif(int(self.random_bit) == 1):

                response = int(input('Introduce el valor para comprobar identidad\n'))
                response_t = int(response) % self.N

                #print(response_t)

                if (response_t != ((self.compromisos*self.secret) % self.N)):
                    #print('false')
                    comprobacion = False
                    print('Respuesta es: {}'.format(response_t))

                else:
                    #print('true')
                    comprobacion = True
                    print('Respuesta es: {}'.format(response_t))

            else:
                raise ValueError('Se ha producido un error\n')


            y_sq = int(self.testigo*self.exponent(self.public, int(self.random_bit), self.N)) % self.N
            #print(y_sq)

            y_sqq = int(self.exponent(response_t,2, self.N))
            #print(y_sqq)
            if(y_sq != y_sqq and comprobacion == False):
                print('Se ha introducido un valor incorrecto en la verificacion: {} en vez de {}'.format(y_sqq,y_sq))
                sys.exit(0)
            elif(int(y_sq) == int(y_sqq) and comprobacion == True):
                print('Se ha comprobado la {} verificacion '.format(x+1))


        print('\n\n---------La comprobacion se ha realizado con exito----------\n\n')

ejemplo = FiatShamir()
ejemplo.execute_program()
#cProfile.run('ejemplo.execute_program()')
