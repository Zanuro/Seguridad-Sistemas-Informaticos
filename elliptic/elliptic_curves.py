import sys
import random
import math
import cProfile
import re



class EllipticCurves:

    def __init__(self,prime_number=0,d_b = 0,a_a =0, punto_base = (), public_key = (), original_message = "",a = 0,b = 0,valores_x = [],valores_y = [],valid_points=[], mensaje_original = (),
                 lista_valores = []):
        self.prime_one = prime_number
        self.d_b = d_b
        self.a_a = a_a
        self.punto_base = punto_base
        self.public_key = public_key
        self.a = a
        self.b = b
        self.original_message = original_message
        self.valores_x = valores_x
        self.valores_y = valores_y
        self.valid_points = valid_points
        self.mensaje_original = mensaje_original
        self.lista_valores = lista_valores

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

    def valid_point(self):

        for x in range(0,self.prime_number):
            self.valores_x.append((x,((pow(x,3) + self.a*x + self.b) % self.prime_number)))
            self.valores_y.append((x,(pow(x,2) % self.prime_number)))

        #print(self.valores_x)
        #print(self.valores_y)

        for x in self.valores_x:
            for y in self.valores_y:
                posicion_1,valor_1 = x
                posicion_2,valor_2 = y

                if(valor_1 == valor_2):
                    self.valid_points.append([posicion_1,posicion_2])

        #print(valid_points)

    def sumar_puntos(self,punto1,punto2):

        lambdda = 0

        if(punto1 == punto2):
            lambdda = int(((3*pow(punto1[0],2)) + self.a) / (2*punto1[1])) % self.prime_number

        elif (punto1 != punto2):
            lambdda = int((punto2[1] - punto1[1]) / (punto2[0]-punto1[0])) % self.prime_number

        first_coordinate = int(pow(lambdda,2) - punto1[0] - punto2[0]) % self.prime_number
        second_coordinate = int(lambdda*punto1[0] - lambdda*first_coordinate - punto1[1]) % self.prime_number

        suma = (first_coordinate,second_coordinate)

        #print(suma)

        return suma

    def perfect_power(self,number):

        return ((number & (number - 1)) == 0) and number != 0

    def get_sum(self,lista):

        if (len(lista) > 1):
            lista =[self.sumar_puntos(lista[i], lista[i + 1]) for i in range(0, len(lista), 2)]
            #print(lista)
            self.get_sum(lista)

        elif len(lista) == 1:
            return lista

    def execute_program(self):

        print('*******EllipticCurves******\n')

        option = int(input('Quieres cifrar o descifrar(0/1)?\n'))

        if option == 0:

            #self.original_message = input('Introduce el mensaje que quieres cifrar(texto)!\n')

            self.mensaje_original = int(input('Introduce el mensaje que quieres cifrar(primera coordenada)!\n')),

            self.mensaje_original += int(input('Introduce el mensaje que quieres cifrar(primera coordenada)!\n')),

            opcion = input('Quieres introducir el primo o random?(0/1)\n')

            if opcion == '0':

                self.prime_number = int(input('Introduce el numero primo\n'))

            elif self.is_prime(self.prime_number) is False:
                raise ValueError('El valor introducido no es primo')

            elif opcion == '1':
                minPrime = 100
                maxPrime = 10000
                cached_primes = [i for i in range(minPrime, maxPrime) if self.is_prime(i)]
                #print(cached_primes)

                self.prime_number = random.choice(cached_primes)

            else:
                raise ValueError('Opcion incorrecta\n')


            print('La curva eliptica a utilizar es: y^2 = x^3 + ax + b\n')

            self.a = int(input('Introduce el valor de a de la ecuacion \n'))
            self.b = int(input('Introduce el valor de b de la ecuacion \n'))

            self.punto_base = int(input('Introduce la primera coordenada del punto base\n')) ,

            self.punto_base += int(input('Introduce la segunda coordenada del punto base\n')) ,

            print('El punto base es: {}\n'.format(self.punto_base))

            posibles = [i for i in range(0,self.prime_number) if self.perfect_power(i)]

            self.d_b = random.choice(posibles)
            self.a_a = random.choice(posibles)

            print('La clave privada es {}\n'.format(self.d_b))


            self.valid_point()

            print('Los puntos de la curva son: {}\n'.format(self.valid_points))


            print('El mensaje original es: {}\n'.format(self.mensaje_original))

            lista_puntos = []

            lista = []

            if self.d_b > 1:
                for _ in range(0,self.d_b):
                    lista_puntos.append(self.punto_base)

                lista = self.get_sum(lista_puntos)

                print('La clave publica de B es: {}\n'.format(lista))

            else:
                print('Clave publica de B es: {}\n'.format(self.punto_base))

            if self.a_a > 1:
                for _ in range(0, self.a_a):
                    lista_puntos.append(lista)

                otra_lista = self.get_sum(lista_puntos)

            else:
                otra_lista = lista

            primera_coordenada = self.sumar_puntos(otra_lista, self.mensaje_original)

            if self.a_a > 1:
                for _ in range(0, self.a_a):
                    lista_puntos.append(self.punto_base)

                otra_listaa = self.get_sum(lista_puntos)

            else:
                otra_listaa = self.punto_base

            segunda_coordenada = otra_listaa


            print('Primer punto del mensaje cifrado es: {} + {}*({}*{}) = {}'.format(self.mensaje_original,self.a_a,self.d_b,self.punto_base,primera_coordenada))
            print('Segundo punto del mensaje cifrado es: {}*{} = {}'.format(self.a_a,self.punto_base,segunda_coordenada))


ejemplo = EllipticCurves()
#ejemplo.execute_program()
cProfile.run('ejemplo.execute_program()')
