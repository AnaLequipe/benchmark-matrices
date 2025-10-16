import java.util.Scanner;
public class MatrixBenchmark {
// ------  FUNCION PARA GENERAR NUMEROS ALEATORIOS --------//
   public static long generador_aleatorio(long semilla)
    {
        int a=1664525;
        int c=1013904223;
        long m = (long) Math.pow(2, 32);
        return (a * semilla + c) % m;
    }

// ------  FUNCION PARA MULTIPLICAR DOS MATRICES NAIVE C = A X B  --------//
    public static int[][] naive_matriz_multiplicacion(int A[][], int B[][])
    {
        int N=A.length;
        int[][] C=new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return  C;
    }
    public static void main(String[] args){
        
//------  PRIMERO: INGRESAR VALORES ENTRADA  --------//
        long semilla;
        int max;
        int N;
        try (Scanner read = new Scanner(System.in)) {
            System.out.print("Semilla inicial: ");
            semilla = read.nextLong();
            System.out.print("Maximo valor de numeros: ");
            max = read.nextInt();
            System.out.print("Dimension de la matriz: ");
            N = read.nextInt();
        }
//------  SEGUNDO: INGRESAR LOS NUMEROS ALEATORIOS A LAS DOS MATRICES  --------//
//------           DONDE SE UTILIZA LA FUNCION DE generador_aleatorio()--------//
        int[][] A_matriz=new int[N][N];
        int[][] B_matriz=new int[N][N];

       for (int i = 0; i < N; i++) {
            int[] fila = new int[N];
            int[] fila2 = new int[N];

            for (int j = 0; j < N; j++) {
                semilla = generador_aleatorio(semilla);   
                int numero = (int)((semilla % max) + 1);
                int valor = numero;
                fila[j] = valor;                          

                long semilla2 = generador_aleatorio(semilla + 1);
                int numero2 = (int)((semilla2 % max) + 1);
                int valor2 = numero2;
                fila2[j] = valor2;                        
            }

            A_matriz[i] = fila;  
            B_matriz[i] = fila2; 
        }

//------  TERCERO: SE REALIZA LA MULTIPLICACION DE LAS DOS MATRICES CON EL      --------//
//------           ALGORITMO DE NAIVE  C = A X B                                --------//
        
        long inicio = System.nanoTime(); // se inicia el conteo de la ejecucion
       // naive_matriz_multiplicacion(A_matriz, B_matriz);
        int[][] C = naive_matriz_multiplicacion(A_matriz, B_matriz);
        long fin = System.nanoTime(); // se finaliza el conteo de la ejecucion
        
//------  CUARTO: SE MUESTRA LAS MATRICES A, B Y C = A X B   --------//

        System.out.println("Matriz A:");
        for (int i = 0; i < N; i++) {
            System.out.print("[");
            for (int j = 0; j < N; j++) {
                System.out.print(A_matriz[i][j] + " ");
            }
            System.out.println("]");
        }

        System.out.println("\nMatriz B:");
        for (int i = 0; i < N; i++) {
            System.out.print("[");
            for (int j = 0; j < N; j++) {
                System.out.print(B_matriz[i][j] + " ");
            }
            System.out.println("]");
        }

        System.out.println("\nC = A X B:");
        System.out.println("\nMatriz C:");

        for (int i = 0; i < N; i++) {
            System.out.print("[");
            for (int j = 0; j < C[i].length; j++) {
                System.out.print(C[i][j] + " ");
            }
            System.out.println("]");
        }

//------  QUINTO: SE CALCULA EL TIEMPO DE EJECUCION EN SEGUNDOS   --------//
        double segundos = (fin - inicio) / 1e9;
        System.out.printf("Tiempo de ejecucion: %.6f segundos%n", segundos);
    }   
}
