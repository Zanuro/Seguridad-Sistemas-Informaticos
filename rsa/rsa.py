import sys
import random
import math
from termcolor import colored, cprint
import cProfile
import re



class RSA:

    def __init__(self,prime_one=0,prime_two=0,n=0,fi_n=0,d=0,e=0,mensaje='',base = 0,valores_bloque =[], valores_bloque_cifrados = []):
        self.prime_one = prime_one
        self.prime_two = prime_two
        self.n = n
        self.fi_n = fi_n
        self.d = d
        self.e = e
        self.mensaje = mensaje
        self.base = base
        self.valores_bloque = valores_bloque
        self.valores_bloque_cifrados = valores_bloque_cifrados

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


    def is_prime_extended(self, num):


        small_primes = [2,3,5,7,11]
        random_numbers = []
        res = []

        resp = any(num % x for x in small_primes)

        if resp == 'True':
            return False

        else:
            #for x in small_primes:
            #   if num % x == 0:
            #       return False
            #    else:
            #        return True

            for _ in range(0,(num/2)-1):
                random_numbers.append(random.randrange(2,num-1))

            for i in range(0,len(random_numbers)):
                elem = random_numbers.pop(i)

                res.append(self.exponent(elem,(num-1)/2,num))

            for i in res:
                if all(res[i] == 1):
                    return False
                elif any(res[i] != 1):
                    return False
                else:
                    return True



    def co_prime(self, a, b):

        while b != 0:
            (a, b) = (b, a % b)
        return a

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self,a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('Modulo no existe')
        else:
            return x % m

    def co_prime_extended(self, a, b):
        x = []
        z = []
        otro = dict()
        x.insert(0,a)
        x.insert(1,b)
        #x[0] = a
        #x[1] = b

        z.insert(-1,0)
        z.insert(0,1)
        #z[-1] = 0
        #z[0] = 1

        resto = x[0] % x[1]
        i = 1
        while resto != 0:
            resto = x[i-1] % x[i]
            print(resto)
            x.insert(i+1,resto)
            z.insert(i,(-int(x[i-1]/x[i])*z[i-1] + (z[i-2] % x[0])))
            print((-int(x[i-1]/x[i])*z[i-1] + (z[i-2] % a)))
            i +=1

        if(x[i-1] == 1):
            otro["primo"] = "True"
            otro["inverso"] = z[i-2]
            return otro

        else:
            otro["primo"] = "False"
            return otro

    def codif_numerica(self):

        num_group = []

        self.mensaje = self.mensaje.replace(" ", "")

        j = int(math.log(self.n,self.base))

        mensaje_dividido = ' '.join((self.mensaje[i:j + i]) for i in range(0, len(self.mensaje), j))
        mensaje_dividido = mensaje_dividido.split(' ')

        print('Como n es {} dividimos el texto en bloques de {} caracteres : {}\n'.format(self.n, j,mensaje_dividido))

        for _ in mensaje_dividido:
            num_group.append(len(_))

        sum = 0

        if self.base == 28:
            for y in mensaje_dividido:
                for x in range(1,len(y)+1):

                    if ((ord(y[x-1]) >= 65) and (ord(y[x-1]) <= 90)):

                        value = ord(y[x-1]) - 65
                        sum += value * pow(self.base, len(y) - x)

                    #elif((ord(y[x-1]) >= 97) and (ord(y[x-1]) <= 122)):
                     #   value = ord(y[x - 1]) - 97
                      #  sum += value * pow(self.base, len(y) - x)
                    elif ord(y[x-1]) == 95:
                        value = ord(y[x-1]) - 69
                        sum += value * pow(self.base, len(y) - x)
                    elif ord(y[x-1]) == 46:
                        value = ord(y[x - 1]) - 19
                        sum += value * pow(self.base, len(y) - x)
                    else:
                        raise ValueError('Se ha producido un error')

                self.valores_bloque.append(sum)
                sum = 0

        elif self.base == 26:
            for y in mensaje_dividido:
                for x in range(1,len(y)+1):

                    if ((ord(y[x-1]) >= 65) and (ord(y[x-1]) <= 90)):

                        value = ord(y[x-1]) - 65
                        sum += value * pow(self.base, len(y) - x)

                    #elif((ord(y[x-1]) >= 97) and (ord(y[x-1]) <= 122)):
                     #   value = ord(y[x - 1]) - 97
                      #  sum += value * pow(self.base, len(y) - x)

                self.valores_bloque.append(sum)
                sum = 0

        elif self.base == 2:

            for y in mensaje_dividido:
                for x in range(1,len(y)+1):

                    sum += y[x-1] * pow(self.base, len(y) - x)

                self.valores_bloque.append(sum)
                sum = 0

        elif self.base == 16:

            for y in mensaje_dividido:
                for x in range(1,len(y)+1):

                    if (ord(y[x-1]) >= 48 and ord(y[x-1]) <= 57):
                        value = ord(y[x - 1]) - 48
                        sum += value * pow(self.base, len(y) - x)
                    elif (ord(y[x-1]) >= 65 and ord(y[x-1]) <= 70):
                        value = ord(y[x - 1]) - 55
                        sum += value * pow(self.base, len(y) - x)

                self.valores_bloque.append(sum)
                sum = 0


        elif self.base == 8:

            for y in mensaje_dividido:
                for x in range(1, len(y) + 1):

                    if (ord(y[x - 1]) >= 48 and ord(y[x - 1]) <= 57):
                        value = ord(y[x - 1]) - 48
                        sum += value * pow(self.base, len(y) - x)
                    elif (ord(y[x - 1]) >= 65 and ord(y[x - 1]) <= 70):
                        value = ord(y[x - 1]) - 55
                        sum += value * pow(self.base, len(y) - x)

                self.valores_bloque.append(sum)
                sum = 0


        else:
            print('Base por defecto')

            return mensaje_dividido


        self.valores_bloque= list(map(int,self.valores_bloque))

    def primeFactors(self,n):

        numbers = []
        while n % 2 == 0:
            n = n/2
            raise ValueError('El numero introducido no es primo')

        for i in range(3, int(math.sqrt(n)) + 1, 2):

            while n % i == 0:
                print(i)
                numbers.append(i)
                n = n / i


        if n > 2:
            print(n)
            numbers.append(n)

        return numbers

    def execute_program(self):

        print('*******RSA******\n')

        option = int(input('Quieres cifrar o descifrar(0/1)?\n'))

        if option == 0:

            self.mensaje = input('Introduce el mensaje que quieres cifrar!\n')

            self.base = int(input('Introduce la base que quieres utilizar para cifrar el mensaje\n'))

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
                maxPrime = 10000
                cached_primes = [i for i in range(minPrime, maxPrime) if self.is_prime(i)]
                #print(cached_primes)

                self.prime_one = random.choice(cached_primes)
                self.prime_two = random.choice(cached_primes)

                if self.prime_one == self.prime_two:
                    raise ValueError('Los dos primos tienen el mismo valor\n')

            else:
                raise ValueError('Opcion incorrecta\n')


            self.n = int(self.prime_one) * int(self.prime_two)

            print('La n(pq) es: {}\n'.format(self.n))

            self.fi_n = int(self.prime_one - 1) * int(self.prime_two - 1)
            print('La phi(n) es : {}\n'.format(self.fi_n))

            self.d = int(input('Introduce el valor de d!\n'))

            res, x,y = self.egcd(self.d,self.fi_n)

            if(res == 1):
                print('El valor d introducido es: {}\n'.format(self.d))
                self.e = self.modinv(self.d,self.fi_n)
                print('El valor e(inverso) es: {}\n'.format(self.e))
            else:
                raise ValueError('El valor introducido no es co primo con {}\n'.format(self.fi_n))

            print('El mensaje a cifrar es: {}\n'.format(self.mensaje))
            print('La base que se va a utilizar es: {}\n'.format(self.base))

            self.codif_numerica()

            print('El mensaje original pasado a bloque decimal: {}\n'.format(self.valores_bloque))

            for x in self.valores_bloque:
                self.valores_bloque_cifrados.append(self.exponent(x,self.e,self.n))

            self.valores_bloque_cifrados = list(map(int, self.valores_bloque_cifrados))

            print('El mensaje cifrado es: {}\n'.format(self.valores_bloque_cifrados))

        elif option == 1:

            self.mensaje = input('Introduce el mensaje que quieres descifrar!\n')

            #self.base = int(input('Introduce la base que quieres utilizar para descifrar el mensaje\n'))

            # opcion = input('Quieres introducir los primos o random?(0/1)\n')
            #
            # if opcion == '0':
            #
            #     self.prime_one = int(input('Introduce el primer numero primo\n'))
            #     self.prime_two = int(input('Introduce el segundo numero primo\n'))
            #
            #     if self.prime_one == self.prime_two:
            #         raise ValueError('Los dos primos tienen el mismo valor\n')
            #
            #     elif self.is_prime(self.prime_one) is False or self.is_prime(self.prime_two) is False:
            #         raise ValueError('Uno o ambos valores introducidos no son primos')
            #
            # elif opcion == '1':
            #     minPrime = 100
            #     maxPrime = 10000
            #     cached_primes = [i for i in range(minPrime, maxPrime) if self.is_prime(i)]
            #     #print(cached_primes)
            #
            #     self.prime_one = random.choice(cached_primes)
            #     self.prime_two = random.choice(cached_primes)
            #
            #     if self.prime_one == self.prime_two:
            #         raise ValueError('Los dos primos tienen el mismo valor\n')
            #
            # else:
            #     raise ValueError('Opcion incorrecta\n')
            #
            #
            # self.n = int(self.prime_one) * int(self.prime_two)
            #
            # print('La n(pq) es: {}\n'.format(self.n))
            #
            # self.fi_n = int(self.prime_one - 1) * int(self.prime_two - 1)
            # print('La phi(n) es : {}\n'.format(self.fi_n))

            self.n = int(input('Introduce el valor de la n:\n'))

            numbers = self.primeFactors(self.n)

            numbers = list(map(int,numbers))
            print(numbers)

            self.fi_n = int(numbers[0]-1) * int(numbers[1]-1)
            print('La phi(n) es : {}\n'.format(self.fi_n))

            self.e = int(input('Introduce el valor de e!\n'))

            res, x, y = self.egcd(self.e, self.fi_n)

            if (res == 1):
                print('El valor e introducido es: {}\n'.format(self.e))
                self.d = self.modinv(self.e, self.fi_n)
                print('El valor d(inverso) es: {}\n'.format(self.d))
            else:
                raise ValueError('El valor introducido no es co primo con {}\n'.format(self.fi_n))

            print('El mensaje a descifrar es: {}\n'.format(self.mensaje))

            self.valores_bloque = re.findall('\d+', self.mensaje)

            for x in self.valores_bloque:
                self.valores_bloque_cifrados.append(self.exponent(int(x),self.d,self.n))

            self.valores_bloque_cifrados = list(map(int, self.valores_bloque_cifrados))

            print('El mensaje original es: {}\n'.format(self.valores_bloque_cifrados))

        else:
            raise ValueError("Se ha introducido un valor erroneo")


ejemplo = RSA()
#ejemplo.execute_program()
cProfile.run('ejemplo.execute_program()')
