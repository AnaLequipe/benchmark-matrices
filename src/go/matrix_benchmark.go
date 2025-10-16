package main

import (
	"fmt"
	"time"
)

// ------  FUNCION PARA GENERAR NUMEROS ALEATORIOS --------//
func generador_aleatorio(semilla int64) int64 {
	var a int64 = 1664525
	var con int64 = 1013904223
	var m int64 = 1 << 32 // 2^32
	return (a*semilla + con) % m
}

// ------  FUNCION PARA MULTIPLICAR DOS MATRICES NAIVE C = A X B  --------//
func naive_matriz_multiplicacion(A [][]int, B [][]int) [][]int {
	N := len(A)
	C := make([][]int, N)
	for i := 0; i < N; i++ {
		C[i] = make([]int, N)
	}
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			for k := 0; k < N; k++ {
				C[i][j] += A[i][k] * B[k][j]
			}
		}
	}
	return C
}

func main() {
	//------  PRIMERO: INGRESAR VALORES ENTRADA  --------//
	var semilla int64
	var max int
	var N int

	fmt.Print("Semilla inicial: ")
	fmt.Scan(&semilla)

	fmt.Print("Maximo valor de numeros: ")
	fmt.Scan(&max)

	fmt.Print("Dimension de la matriz: ")
	fmt.Scan(&N)

	//------  SEGUNDO: INGRESAR LOS NUMEROS ALEATORIOS A LAS DOS MATRICES  --------//
	//------           DONDE SE UTILIZA LA FUNCION DE generador_aleatorio()--------//
	A_matriz := make([][]int, N)
	B_matriz := make([][]int, N)

	for i := 0; i < N; i++ {
		fila := make([]int, N)
		fila2 := make([]int, N)

		for j := 0; j < N; j++ {
			semilla = generador_aleatorio(semilla)
			numero := int((semilla % int64(max)) + 1)
			valor := numero
			fila[j] = valor

			semilla2 := generador_aleatorio(semilla + 1)
			numero2 := int((semilla2 % int64(max)) + 1)
			valor2 := numero2
			fila2[j] = valor2
		}
		A_matriz[i] = fila
		B_matriz[i] = fila2
	}

	//------  TERCERO: SE REALIZA LA MULTIPLICACION DE LAS DOS MATRICES CON EL      --------//
	//------           ALGORITMO DE NAIVE  C = A X B                                --------//

	start := time.Now() // se inicia el conteo de la ejecucion
	//naive_matriz_multiplicacion(A_matriz, B_matriz)
	C := naive_matriz_multiplicacion(A_matriz, B_matriz)
	elapsed := time.Since(start) // se finaliza el conteo de la ejecucion
	//------  CUARTO: SE MUESTRA LAS MATRICES A Y B CON LOS NUMEROS ALEATORIOS  --------//

	fmt.Println("Matriz A:")
	for i := 0; i < N; i++ {
		fmt.Print("[")
		for j := 0; j < N; j++ {
			fmt.Printf("%d ", A_matriz[i][j])
		}
		fmt.Println("]")
	}

	fmt.Println("\nMatriz B:")
	for i := 0; i < N; i++ {
		fmt.Print("[")
		for j := 0; j < N; j++ {
			fmt.Printf("%d ", B_matriz[i][j])
		}
		fmt.Println("]")
	}
	fmt.Println("\nC = A x B:")
	fmt.Println("\nMatriz C:")
	for i := 0; i < N; i++ {
		fmt.Print("[")
		for j := 0; j < len(C[i]); j++ {
			fmt.Printf("%d ", C[i][j])
		}
		fmt.Println("]")
	}

	//------  QUINTO: SE CALCULA EL TIEMPO DE EJECUCION EN SEGUNDOS   --------//
	fmt.Printf("Tiempo de ejecucion: %.6f segundos\n", elapsed.Seconds())

}
