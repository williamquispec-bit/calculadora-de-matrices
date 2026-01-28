# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:44:44 2026

@author: willi
"""

# -*- coding: utf-8 -*-
"""
CALCULADORA DE MATRICES
-----------------------------------
Autor: William Quispe
Curso: Lenguajes de Programación

Calculadora de matrices utilizando la librería NumPy para optimización de cálculos.
"""

import numpy as np
import sys

def solicitar_dimensiones(nombre_matriz):
    """
    Solicita al usuario las filas y columnas validando que sean números enteros positivos.
    Retorna: tupla (filas, columnas)
    """
    while True:
        try:
            print(f"\n--- Dimensiones para Matriz {nombre_matriz} ---")
            f = int(input("Ingrese número de Filas: "))
            c = int(input("Ingrese número de Columnas: "))
            if f > 0 and c > 0:
                return f, c
            else:
                print("Error: Las dimensiones deben ser mayores a 0.")
        except ValueError:
            print(" Error: Debe ingresar números enteros válidos.")

def crear_matriz(nombre):
    """
    Crea una matriz solicitando los datos fila por fila.
    Maneja errores de entrada (letras en lugar de números).
    """
    filas, cols = solicitar_dimensiones(nombre)
    print(f"Ingrese los {filas * cols} números fila por fila (separados por espacio):")
    
    matriz_temp = []
    
    for i in range(filas):
        while True:
            try:
                entrada = input(f"Fila {i+1}: ")
                # Convertimos la entrada de texto a lista de flotantes
                datos_fila = list(map(float, entrada.split()))
                
                # Validación de integridad de datos (Sofisticación)
                if len(datos_fila) != cols:
                    print(f" Error: Se esperaban {cols} números, pero ingresó {len(datos_fila)}.")
                    print("Intente esa fila de nuevo.")
                    continue
                
                matriz_temp.append(datos_fila)
                break # Rompe el while interno y pasa a la siguiente fila
            except ValueError:
                print("Error: Ingresó caracteres no numéricos. Intente de nuevo.")

    return np.array(matriz_temp)

def main():
    """Función principal que gestiona el flujo del programa."""
    print("Calculadora de matrices")
    
    while True:
        print("\n" + "="*40)
        print("       MENÚ PRINCIPAL")
        print("="*40)
        print("1. Sumar Matrices (A + B)")
        print("2. Restar Matrices (A - B)")
        print("3. Multiplicar Matrices (A * B)")
        print("4. Salir")
        
        opcion = input(" Seleccione opción: ")

        if opcion == '4':
            print("fin del proceso")
            break
        
        if opcion in ['1', '2', '3']:
            try:
                print("\n[!] Configurando Matriz A:")
                A = crear_matriz("A")
                
                print("\n[!] Configurando Matriz B:")
                B = crear_matriz("B")

                print("\n" + "-"*30)
                print("      RESULTADO OPERACIÓN")
                print("-" * 30)

                if opcion == '1':
                    # NumPy maneja la suma elemento a elemento
                    if A.shape != B.shape:
                        print(" Error Matemático: Para sumar, las dimensiones deben ser idénticas.")
                    else:
                        print(A + B)

                elif opcion == '2':
                    if A.shape != B.shape:
                        print(" Error Matemático: Para restar, las dimensiones deben ser idénticas.")
                    else:
                        print(A - B)

                elif opcion == '3':
                    # Validación estricta de Algebra Lineal
                    # Columnas de A (A.shape[1]) deben ser igual a Filas de B (B.shape[0])
                    if A.shape[1] != B.shape[0]:
                        print(f" Error Matemático: No se puede multiplicar {A.shape} con {B.shape}.")
                        print("Regla: Columnas de A deben ser iguales a Filas de B.")
                    else:
                        # np.dot es la función para producto punto matricial
                        print(np.dot(A, B))
            
            except Exception as e:
                print(f" Error inesperado en el sistema: {e}")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()