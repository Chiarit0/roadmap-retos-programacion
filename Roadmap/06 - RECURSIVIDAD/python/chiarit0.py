'''LECCIÓN N°6: RECURSIVIDAD
Recurisividad es una función que se llama asi misma'''

# def countdown(number):
#     if number>=0:                    #Caso base en donde se coloca hasta que condición de borde llega la recursión.
#         print(number)                
#         countdown(number-1)          #Vuelve a llamar a la función pero esta vez con un número menor, vuelve a la función y se ejecuta hasta llegar al caso base.
    
# countdown(10)


# def countdown(number):
#     for i in range(number,-1,-1):      #Con un bucle for, para ir en rango inverso se voltea con un "-1"
#         print(i)

# countdown(3)



''' * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).'''

def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
   
print(factorial(5))


def sucesion(factor):
    if factor==0:
        return 0
    elif factor==1:
        return 1
    else:
        return sucesion(factor-1)+sucesion(factor-2)
    
print(sucesion(8))

