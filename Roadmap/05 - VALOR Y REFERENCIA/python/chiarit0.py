'''LECCIÓN N°5 VALOR Y REFERENCIA'''

#TIPOS DE DATOS POR VALOR
#Cada vez que se le aisgna el valor de una variable a otra variable, copia su valor.
# Enteros, float, cadenas de texto, booleanos.



#TIPOS DE DATOS POR REFERENCIA
#Una variable asignada a otra variable, no copia su valor, sino que hereda su posición de memoria.
#No se copia el valor, se queda con la dirección de memoria de la variable original, cuando se modifica la nueva variable, 
"""se modifica igual la variable original """
#Son los tipos de datos que no son primitivos (NO enteros, float, cadenas de texto, booleanos)
#Listas, set, diccionarios.


#FUNCIONES CON DATOS POR VALOR

'''
my_int_a=10

def my_int_fun(my_int):
    my_int=20
    print(my_int)

my_int_fun(my_int_a)  #Sigue imprimiendo alor de my_int
print(my_int_a)       #my_int_a aigue valiendo 10.



#FUNCIONES CON DATOS POR REFERENCIA

def my_list_fun(my_list:list):
    my_list.append(30)
    print(my_list)

my_list_a=[10,20]                    #Que se cambie dentro de la función, fuera también.
my_list_fun(my_list_a)
print(my_list_a) 

'''

''' * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.'''

#VALORES

def programa1 (a:int,b:int):
    c=a  #nuevavariable para guardar el valor de a.
    a=b
    b=c
    return a,b

#veamos si funciono

a=100
b=200
x,y=programa1 (a,b)

print(f"variables originales: {a},{b}")
print(f"variables nuevas: {x},{y}")


# REFERENCIAS
def programa2 (lista_t:list,lista_j:list):
    vartemp=lista_t
    lista_t=lista_j
    lista_j=vartemp
    return lista_t,lista_j


lista_t=[100,200,300]
lista_j=[400,500,600]

lista_f,lista_g=programa2(lista_t,lista_j)

print(lista_t,lista_j)
print(lista_f,lista_g)







