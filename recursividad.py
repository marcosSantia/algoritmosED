""" ejercicio 2 """
def sumatoria(numero):
    if numero == 0:
        return 0
    else:
        return numero + sumatoria(numero-1)
print(sumatoria(10))

""" ejercicio 3 """

def producto(num1,num2):
    if num2 == 1:
        return num1
    else:
        return num1 + producto(num1,num2-1)
print(producto(2,10))




""" ejercicio 4 """
""" 2^3= 2*2*2 = B * (B*exp-1)"""
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

print(potencia(3, 9))


""" ejercicio 8 """
def decimal_a_binario(n):
    if n == 0:
        return 0
    else:
        return decimal_a_binario(n // 2) + str(n % 2) if n > 1 else str(n % 2)

# Prueba del algoritmo
numero_decimal = 6
print(f"El numero {numero_decimal} en binario es {decimal_a_binario(numero_decimal)}")



""" ejercicio 10 """
def contar_digitos(n):
    if n == 0:
        return 0
    else:
        return 1 + contar_digitos(n // 10)

# Prueba del algoritmo
numero = 12
print(f"El numero {numero} tiene {contar_digitos(numero)} digitos.")

""" ejercicio 11 """
def invert_number(numero):
    if numero < 10:
        return numero
    else:
        return(numero%10) * 10 **len(str(numero//10)) + invert_number(numero//10)
    
print(invert_number(1234567))


""" ejercicio 14 """
def sumar_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero//10)
print(sumar_digitos(719))


""" ejercicio 17 """
def mostrar_vector_reversa(vector, indice):
    if indice < 0:
        return
    else:
        print(vector[indice])
        mostrar_vector_reversa(vector, indice-1)

vector = [1, 2, 3, 4, 5]
mostrar_vector_reversa(vector, len(vector)-1)

""" ejercicio 20 """
def mostrar_matriz(matriz, fila, columna):
    if fila == len(matriz):
        return
    elif columna == len(matriz[fila]):
        mostrar_matriz(matriz, fila+1, 0)
    else:
        print(matriz[fila][columna])
        mostrar_matriz(matriz, fila, columna+1)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mostrar_matriz(matriz, 0, 0)


""" ejercicio 20 """
def busqueda_secuencial_recursiva(lista, valor, indice=0):
    if indice == len(lista):
        return False
    elif lista[indice] == valor:
        return True
    else:
        return busqueda_secuencial_recursiva(lista, valor, indice+1)

lista = [1, 2, 3, 4, 5]
valor = 3
if busqueda_secuencial_recursiva(lista, valor):
    print(f"El valor {valor} está en la lista.")
else:
    print(f"El valor {valor} no está en la lista.")
    
""" fibonacci recursivo"""
def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)
    
""" fibonacci iterativo"""
def fibonacci_iter(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        a, b = 0, 1
        for i in range(2, numero+1):
            a, b = b, a+b
        return b
        
print(fibonacci(7))
print(fibonacci_iter(7))

""" busqueda binaria recursiva"""
numeros = [1, 2, 3, 4, 5, 7, 10, 23, 45]
def bb_recursiva(lista,buscado,primero,ultimo):
    if primero > ultimo:
        return None
    medio = (primero + ultimo) // 2
    if lista[medio] == buscado:
        return medio
    elif lista[medio] < buscado:
        return bb_recursiva(lista, buscado, medio+1, ultimo)
    else:
        return bb_recursiva(lista, buscado, primero, medio-1)
pos = bb_recursiva(numeros, 3, 0, len(numeros)-1)
print(f"posicion {pos}")
if pos is not None:
    print(pos, numeros[pos])
    
    
def raiz_cuadrada (numero, valor=1):
    if numero == 0 or numero == 1:
        return numero
    else:
        resultado = valor * valor
        if resultado == numero:
            return valor
        elif resultado>numero:
            return valor -1
        else:
            return raiz_cuadrada (numero, valor+1)
print(raiz_cuadrada(5))

