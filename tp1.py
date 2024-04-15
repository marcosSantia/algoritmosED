""" ejercicio 5 de la guia de recursividad """

def romanoADecimal(romano):
    numerosRomanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return numerosRomanos[romano]

    if numerosRomanos[romano[0]] < numerosRomanos[romano[1]]:
        return numerosRomanos[romano[1]] - numerosRomanos[romano[0]] + romanoADecimal(romano[2:])
    else:
        return numerosRomanos[romano[0]] + romanoADecimal(romano[1:])


romano = "XX"
numeroDecimal = romanoADecimal(romano)
print(numeroDecimal)

""" ejercicio 25 de la guia de recursividad """

def calcularTrianguloPascal(fila):
    # Creo una matriz 
    matriz = [[0] * (i + 1) for i in range(fila)]

    # Lleno la matriz
    for i in range(fila):
        for j in range(i + 1):
            if j == 0 or j == i:
                matriz[i][j] = 1
            else:
                matriz[i][j] = matriz[i - 1][j - 1] + matriz[i - 1][j]

    # Mostrar el triángulo
    for i in range(fila):
        for j in range(i + 1):
            print(matriz[i][j], end=" ")
        print()

fila = 10
calcularTrianguloPascal(fila)


