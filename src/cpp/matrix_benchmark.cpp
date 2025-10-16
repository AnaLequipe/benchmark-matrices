#include <iostream>
#include <chrono>

//------  FUNCION PARA GENERAR NUMEROS ALEATORIOS --------//
unsigned int generador_aleatorio(int semilla) {      
    unsigned int a = 1664525;
    unsigned int c = 1013904223;
    unsigned long long m = 4294967296; // 2^32
    return (a * semilla + c) % m;         
}

//------  FUNCION PARA MULTIPLICAR DOS MATRICES NAIVE C = A X B  --------//
void naive_matriz_multiplicacion(int N, int** A, int** B, int** C) {
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) {
            C[i][j] = 0;
            for (int k = 0; k < N; k++)
                C[i][j] += A[i][k] * B[k][j];
        }
}

int main(int arg, char const *argv[])
{    
    //------  PRIMERO: INGRESAR VALORES ENTRADA  --------//
    unsigned int semilla;
    unsigned int max;
    unsigned int N;
    std::cout << "Ingresa la semilla: ";
    std::cin >> semilla;
    std::cout << "Ingrese el maximo valor de numeros: ";
    std::cin >> max;
    std::cout << "Ingresa Dimension de la Matriz: ";
    std::cin >> N;

    //------ ARRAYS DINÁMICOS PARA N GRANDES --------//
    int** A_matriz = new int*[N];
    int** B_matriz = new int*[N];
    int** C = new int*[N];
    for(int i = 0; i < N; i++){
        A_matriz[i] = new int[N];
        B_matriz[i] = new int[N];
        C[i] = new int[N];
    }

    //------  SEGUNDO: INGRESAR LOS NUMEROS ALEATORIOS A LAS DOS MATRICES  --------//
    //------           DONDE SE UTILIZA LA FUNCION DE generador_aleatorio()--------//
    for (int i = 0; i < N; i++) {
        int* fila = new int[N];
        int* filaB = new int[N];
        for (int j = 0; j < N; j++) {
            semilla = generador_aleatorio(semilla);
            int numero = (semilla % max) + 1 ;
            int valor = numero;
            fila[j] = valor;
            int semilla2 = generador_aleatorio(semilla+1);
            int numero2 = (semilla2 % max) + 1 ;
            int valor2 = numero2;
            filaB[j] = valor2;  
        }
        for (int j = 0; j < N; j++) {
            A_matriz[i][j] = fila[j];
            B_matriz[i][j] = filaB[j];
        } 
        delete[] fila;
        delete[] filaB;
    }

    //------  TERCERO: SE REALIZA LA MULTIPLICACION DE LAS DOS MATRICES CON EL      --------//
    //------           ALGORITMO DE NAIVE  C = A X B                                --------//
    auto inicio = std::chrono::high_resolution_clock::now();  // se inicia el conteo de la ejecucion
    naive_matriz_multiplicacion(N, A_matriz, B_matriz, C);
    auto fin = std::chrono::high_resolution_clock::now();    // se finaliza el conteo de la ejecucion

//------  CUARTO: SE MUESTRA LAS MATRICES A, B Y C = A X B   --------//
  
    std::cout << "\nMatriz A:\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cout << A_matriz[i][j] << "\t";
        }
        std::cout << "\n";
    }

    std::cout << "\nMatriz B:\n";
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cout << B_matriz[i][j] << "\t";
        }
        std::cout << "\n";
    }
    
    std::cout << "\nC = A x B:" ;
    std::cout << "\nMatriz C:\n" ;
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            std::cout << C[i][j] << "\t";
        }
        std::cout << "\n";
    }
    
//------  QUINTO: SE CALCULA EL TIEMPO DE EJECUCION EN SEGUNDOS   --------//
    std::chrono::duration<double> duracion = fin - inicio;
    double segundos = duracion.count();  
    std::cout << "Tiempo de ejecucion: " << segundos << " segundos\n";

//------ LIBERAR MEMORIA DINAMICA DE LOS VECTORES--------//
    for(int i = 0; i < N; i++){
        delete[] A_matriz[i];
        delete[] B_matriz[i];
        delete[] C[i];
    }
    delete[] A_matriz;
    delete[] B_matriz;
    delete[] C;

    return 0;
}
