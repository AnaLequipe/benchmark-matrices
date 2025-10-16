
import time
##  ------  FUNCION PARA GENERAR NUMEROS ALEATORIOS --------//
def generador_aleatorio(seed):
    a = 1664525        
    c = 1013904223     
    m = 2**32          
    return (a * seed + c) % m

##  ------  FUNCION PARA MULTIPLICAR DOS MATRICES NAIVE C = A X B  --------//
def naive_matriz_multiplicacion(A,B):
    N = len(A)
    C = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]

    return C

##-----  PRIMERO: INGRESAR VALORES ENTRADA  --------//
semilla = int(input("Semilla inicial: "))
max = int(input("Maximo valor de numeros: "))
N = int(input("Dimension de la Matriz: "))

##------  SEGUNDO: INGRESAR LOS NUMEROS ALEATORIOS A LAS DOS MATRICES  --------//
##------           DONDE SE UTILIZA LA FUNCION DE generador_aleatorio()--------//
A_matriz = []
B_matriz = []

for i in range(N):
    fila = []
    fila2 = []
    for j in range(N):
        semilla = generador_aleatorio(semilla)   
        numero = (semilla % max) + 1 
        valor = numero
        fila.append(valor)
        semilla2 = generador_aleatorio(semilla+1) 
        numero2 = (semilla2 % max) + 1 
        valor2 = numero2
        fila2.append(valor2)
    A_matriz.append(fila)
    B_matriz.append(fila2)

##------  TERCERO: SE REALIZA LA MULTIPLICACION DE LAS DOS MATRICES CON EL      --------//
##------           ALGORITMO DE NAIVE  C = A X B                                --------//

start_time = time.time() ## se inicia el conteo de la ejecucion
C = naive_matriz_multiplicacion(A_matriz, B_matriz)
end_time = time.time()   ## se finaliza el conteo de la ejecucion

##------  CUARTO: SE MUESTRA LAS MATRICES A, B Y C = A X B   --------//
print("\nMatriz A:")
for fila in A_matriz:
    print(fila)

print("\nMatriz B")
for fila in B_matriz:
    print(fila)

print("\nResultado C = A x B:")
for fila in C:
    print(fila)
    
##------  QUINTO: SE CALCULA EL TIEMPO DE EJECUCION EN SEGUNDOS   --------//
elapsed = end_time - start_time
print(f"\nTiempo de ejecucion: {elapsed:.6f} segundos")