# # # 1. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla la frase “Hola, ya se imprimir frases”.

# # print("\nEjercicio 1")
# # print("Hola, ya se imprimir frases")

# # # 2. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla un número entero, 
# # # por ejemplo el 273, o el 597.

# # print("\nEjercicio 2")
# # print(273)
# # print(597)

# # # 3. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla un número decimal, por
# # # ejemplo el 5’3, ó el 7’5.

# # print("\nEjercicio 3")
# # print(5.3)
# # print(7.5)

# # # 4. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla la suma de 1234 y 532.

# # print("\nEjercicio 4")
# # print(1234 + 532)

# # # 5. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla la resta de 1234 y 532.

# # print("\nEjercicio 5")
# # print(1234 - 532)

# # # 6. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla la multiplicación de 1234 y 532.

# # print("\nEjercicio 6")
# # print(1234 * 532)

# # # 7. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla la división de 1234 entre 532.

# # print("\nEjercicio 7")
# # print(1234 / 532)

# # # 8. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla los números del 1 al 3.

# # print("\nEjercicio 8")
# # for i in range(1, 4):
# #     print(i)
    
# # # 9. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla los números del 1 al 9.

# # print("\nEjercicio 9")
# # for i in range(1, 10):
# #     print(i)
    
# # # 10. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla los números del 1 al 10.000.
# # # Conveniente usar bucles.

# # print("\nEjercicio 10")
# # for i in range(1, 10001):
# #     print(i)
    
# # # 11. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla los números del 5 al 10. 

# # print("\nEjercicio 11")
# # for i in range(5, 11):
# #     print(i)
    
# # # 12. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla los números del 5 al 15. 

# # print("\nEjercicio 12")
# # for i in range(5, 16):
# #     print(i)
    
# # # 13. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla los números del 5 al 15.000.
# # # Conveniente usar bucles.

# # print("\nEjercicio 13")
# # for i in range(5, 15001):
# #     print(i)
    
# # # 14. Ejercicio:
# # # Escribir un programa en Python que imprima 200 veces la palabra “hola”. Nota: en el
# # # código fuente que usted escriba debe figurar solamente una vez la palabra “hola”.

# # print("\nEjercicio 14")
# # for i in range(200):
# #     print("hola")
    
# # # 15. Ejercicio:
# # # Escribir un programa en Python que imprima por pantalla los cuadrados de los 30
# # # primeros números naturales.

# # print("\nEjercicio 15")
# # for i in range(1, 31):
# #     print(i**2)
    
# # # 16. Ejercicio:
# # # Escribir un programa en Python que multiplique los 20 primeros número naturales
# # # (1*2*3*4*5...).

# # print("\nEjercicio 16")
# # multi = 1
# # for i in range(1, 21):
# #     multi = i * multi
# #     print(multi)
    
# # # 17. Ejercicio:
# # # Escribir un programa en Python que sume los cuadrados de los cien primeros números
# # # naturales, mostrando el resultado en pantalla.

# # print("\nEjercicio 17")
# # suma = 0
# # for i in range(1, 101):
# #     suma = suma + i**2
# # print(suma)

# # # 18. Ejercicio:
# # # Escribir un programa en Python que lea un número entero desde teclado y realiza la
# # # suma de los 100 número siguientes, mostrando el resultado en pantalla.

# # print("\nEjercicio 18")
# # num = int(input("Ingrese un número entero: "))
# # suma = 0
# # for i in range(num, num + 101):
# #     suma = suma + i
# # print(suma)

# # # 19. Ejercicio:
# # # Escribir un programa en Python que convierta de euros a dólares. Recibirá un número
# # # decimal correspondiente a la cantidad en euros y contestará con la cantidad
# # # correspondiente en dolares.

# # print("\nEjercicio 19")
# # valor_euro_dolar = 1.11
# # valor_dolar_euro = 0.90
# # euros = float(input("Ingrese la cantidad de euros: "))
# # dolares = euros * valor_euro_dolar
# # print(f"{euros} euros equivalen a {dolares} dolares")

# # # 20. Ejercicio:
# # # Escribir un programa en Python que calcule el área de un rectángulo del cual se le
# # # proporcionará por el teclado su altura y anchura (números decimales).

# # print("\nEjercicio 20")
# # altura = float(input("Ingrese la altura del rectángulo: "))
# # anchura = float(input("Ingrese la anchura del rectángulo: "))
# # area = altura * anchura
# # print(f"El área del rectángulo es {area} unidades cuadradas")

# # # 21. Ejercicio:
# # # Escribir un programa en Python que lea dos números del teclado y diga cual es el
# # # mayor y cual el menor.

# # print("\nEjercicio 21")
# # num1 = float(input("Ingrese el primer número: "))
# # num2 = float(input("Ingrese el segundo número: "))
# # if num1 > num2:
# #     print(f"{num1} es mayor que {num2}")
# # elif num1 < num2:
# #     print(f"{num2} es mayor que {num1}")
# # else:
# #     print("Los dos números son iguales")
    
# # # 22. Ejercicio:
# # # Escribir un programa en Python que lea un número entero por el teclado e imprima
# # # todos los número impares menores que él.

# # print("\nEjercicio 22")

# # E22_num = int(input("Ingrese un número entero: "))

# # for i in range (1,E22_num):
# #     if i % 2 == 1:
# #         print(i)
        
# # 23. Ejercicio:
# # Implemente el algoritmo de Euclides para encontrar el gcd de dos número leídos
# # desde teclado.

# # E23_num1 = int(input("Ingrese el primer número: "))
# # E23_num2 = int(input("Ingrese el segundo número: "))

# # if E23_num1 == 0:
# #     print(f"El MCD es {E23_num2}")
# # elif E23_num2 == 0:
# #     print(f"El MCD es {E23_num1}")
# # else:
# #     A = E23_num1
# #     B = E23_num2
    
# #     while True:
# #         C = B
# #         B = A % B
# #         A = C
# #         if B == 0:
# #             B = A
# #             break
# #     print (f"El MCD es {B}")
    
# # 24. Ejercicio:
# # Escriba un programa que lea los coeficientes a, b y c de una ecuación de segundo, y
# # estudie si tiene o no solución. En caso positivo, las soluciones se calcularán e
# # imprimirán en pantalla.
    
# coeficiente_a = float(input("Ingrese el coeficiente a: "))
# coeficiente_b = float(input("Ingrese el coeficiente b: "))
# coeficiente_c = float(input("Ingrese el coeficiente c: "))

# discriminante = coeficiente_b**2 - 4*coeficiente_a*coeficiente_c
# if True:
#     if discriminante < 0:
#         print("La ecuación no tiene solución real")
#     else:
#         if discriminante == 0:
#             print("La ecuación tiene una solución real")
#         else:
#             print("La ecuación tiene dos soluciones reales")
#         valor_raiz = discriminante**0.5
#         divisor = 2 * coeficiente_a
#         solucion_1 = (-coeficiente_b + valor_raiz) / divisor
#         solucion_2 = (-coeficiente_b - valor_raiz) / divisor
        
#         print(f"Las soluciones para la ecuación: {coeficiente_a}^2 + {coeficiente_b} + {coeficiente_c}"
#             f" son: {solucion_1} y {solucion_2}")

# # 25. Ejercicio:
# # Pruebe la recursividad en Python. Escriba programas que calculen recursivamente las
# # funciones f actorial(n) y Ackermann(x, y).

# print("\nEjercicio 25")

# def factorial(n):
#     for i in range (1, n+1):
#         if i == 1:
#             fact = 1
#         else:
#             fact = i * fact
#     print(f"El factorial de {n} es {fact}")

# fact_Num =  int(input("Ingrese un número para calcular su factorial: "))
# factorial(fact_Num)

# def Ackerman(x,y):
#     if x == 0:
#         print(x,y)
#         return y + 1
#     elif x > 0 and y == 0:
#         print(x,y)
#         return Ackerman(x-1, 1)
#     elif x > 0 and y > 0:
#         print(x,y)
#         return Ackerman(x-1,Ackerman(x,y-1))
    
# print(Ackerman(1,1))

# 26. Ejercicio:
# Escriba un programa que lea tres números enteros positivos, y que calcule e imprima
# en pantalla el menor y el mayor de todos ellos.

# E26_num1 = int(input("Ingrese el primer número: "))
# E26_num2 = int(input("Ingrese el segundo número: "))
# E26_num3 = int(input("Ingrese el tercer número: "))

# if E26_num1 > E26_num2 and E26_num1 > E26_num3:
#     mayor = E26_num1
#     if E26_num2 < E26_num3:
#         menor = E26_num2
#     else:
#         menor = E26_num3
# elif E26_num2 > E26_num1 and E26_num2 > E26_num3:
#     mayor = E26_num2
#     if E26_num1 < E26_num3:
#         menor = E26_num1
#     else:
#         menor = E26_num3
# elif E26_num3 > E26_num1 and E26_num3 > E26_num3:
#     mayor = E26_num2
#     if E26_num1 < E26_num3:
#         menor = E26_num1
#     else:
#         menor = E26_num3
    
# print(f"El mayor es {mayor} y el menor es {menor}")

# 27. Ejercicio:
# Escriba un programa que lea temperaturas expresadas en grados Fahrenheit y las
# convierta a grados Celsius mostrándola. El programa finalizará cuando lea un valor
# de temperatura igual a 999. La conversión de grados Farenheit (F) a Celsius (C) está
# dada por C = 5/9(F − 32).

# for i in range (1,1000):
#     C = 5/9*(i-32)
#     print(f"{i} Fahrenheit son {C} Celsius")

# 28. Ejercicio:
# Implemente una sentencia switch que escriba un mensaje en cada caso. Inclúyala en
# bucle de prueba for. Utilice también un break tras cada caso y pruébelo. Elimine el
# break y vea qué ocurre.
 
# print("\nEjercicio 28")
# opcion = int(input("Ingrese un número del 1 al 5: "))   
# match opcion:
#     case 1:
#         print("Elegiste la opción 1")
#     case 2:
#         print("Elegiste la opción 2")
#     case 3:
#         print("Elegiste la opción 3")
#     case 4:
#         print("Elegiste la opción 4")
#     case 5:
#         print("Elegiste la opción 5")
#     case _:
#         print("Opción no válida")
        
# 29. Ejercicio:
# Cuando se lee una entrada estándar, por lo general se alcanza el fin de archivo
# cuando el usuario teclea CRTL-D, CRTL-Z, o algún otro carácter dependiente del
# sistema. Descubra cuál es el adecuado en su sistema. Escriba un programa que lea
# datos controlando el fin de la secuencia con la combinación adecuada.

# print("\nEjercicio 29")
        
# 30. Ejercicio:
# Escriba un programa que use dos bucles for anidados y el operador de módulo (%)
# para detectar e imprimir números primos.
    
# print("\nEjercicio 30")

# cont=1
# primo=[]

# while cont <= 100:
#     num_primo=[]
#     for i in range (2,11):
#         if cont % i != 0:
#             num_primo = True
#         elif (cont == i) and (cont%i-1 !=0):
#             num_primo = True
#             break
#         else:
#             num_primo = False
#             break
#     if num_primo == True:
#         print(f"{cont} es primo")
#         primo.append(cont)
    
#     cont += 1
