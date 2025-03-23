#LECCIÓN 0
#Elegiré Python como lenguaje de programación.
#https://www.python.org/
#Esto es un comentario. 
'''esto es
un comentario en varias lineas'''
my_variable="mi variable"
my_variable="nuevo valor de mi variable"
MY_CONSTANTE="mi constante"  #En Python no existen las constantes por lo que por convención, al nombrar la varialbes en mayus se entiende que es constante.

my_int=1 #Números enteros.
my_float=0.5 #Números decimales
my_bool=True #Números boleanos con valores en verdadero o falso.
my_bool=False
my_string="Hola" #Cadenas de texto
my_other_string='Hola' #Cadena de texto con comilla simple.

print("¡Hola, Python!")








#LECCIÓN 1
#OPERADORES Y ESTRUCTURAS DE CONTROL
#Operadores Ariméticos
print(f"suma:10+3={10+3}")
print(f"resta:10-3={10-3}")
print(f"multiplicación:10*3={10*3}")
print(f"división:10/3={10/3}")
print(f"módulo:10%3={10%3}")   #Operación que da por resultado el resto que queda luego de dividir el primer número en el segundo.
print(f"exponente:10**3={10**3}")
print(f"división entera:10//3={10//3}")

#Operadores de comparación
print(f"Igualdad: 10==3 es:{10==3}")
print(f"Desigualdad: 10!=3 es:{10!=3}")
print(f"Mayor que: 10>3 es:{10>3}")
print(f"Menor que: 10<3 es:{10<3}")
print(f"Mayor o igual que: 10>=10 es:{10>=10}")
print(f"Menor o igual que: 10<=3 es:{10<=3}")

#Operadores lógicos
print(f"AND &&: 10+3==13 and 4-1==3 es:{10+3==13 and 4-1==3}") #Ambas condiciones deben ser verdaderas.
print(f"OR ||: 10+3==13 or 4-1==0 es:{10+3==13 or 4-1==0}")  #Se debe cumplir alguna de las condiciones.
print(f"NOT !: 10+3==14 es:{not 10+3==14}")  #Se antepone el not para decir que no se cumple dicha condición.

#Operadores de asignación
my_number=11  #Se asigna un valor.
my_number+=1  #Suma y asignación.
my_number-=1  #Resta y asignación.
my_number*=2  #Multiplicación y asignación.
my_number/=2  #División y asignación.
my_number**=1  #Exponente y asignación.
my_number//=1  #División entera y asignación.

#Operadores de identidad
#Nos sirve para comparar no el valor de la variable, sino el valor de la posición. Compara el valor en memoria.

#Operadores de Pertenencia
#Ayuda ver si algo pertenece a algo.
print(f"T está en la palabra Tami:{'T'in'Tami'}")
print(f"T no está en la palabra Tami:{'T'not in'Tami'}")

#Operadores BIT
a=10 #1010
b=3 #0011

print(f"AND: 10 & 3 = {10&3}") #Compara bit a bit, si ambos valores son 1, es 1. En este caso al comparar 1010 y 0011 --> 0010 lo cual es 2.
print(f"OR: 10 | 3 = {10|3}") #Compara bit a bit, si al menos un valor es 1, es 1. En este caso al comparar 1010 y 0011 --> 1011 lo cual es 11.
print(f"XOR: 10 ^ 3 = {10^3}") #Compara bit a bit, si son iguales es 0, si son diferentes es 1. En este caso 1010 y 0011 --> 1001 lo cual es 9.
print(f"NOT: ~10= {~10}") #Intercambia valor de bit.
print(f"Desplazamiento a la derecha: 10 >> 2 = {10>>2}") #Desplaza bit a la derecha 2 veces.
print(f"Desplazamiento a la izquierda: 10 << 2 = {10<<2}") #Desplaza bit a la izquierda 2 veces.

#ESTRUCTURAS DE CONTROL
#Condicionales

#IF
my_string="Tami"
if my_string == "Tami":                #Se puede cumplir esta o la segunda condición, o ninguna y pasa a la última.
    print("my_string es 'Tami'")
elif my_string=="Yalle":
    print("my_string es 'Yalle'")
else:
    print("my_string no es 'Tami'")

#Iterativos

#FOR

for j in range(11):                    #Para crear bucles, para recorrer estructuras o ejecutar una acción varias veces.
    print(j)                           #Rango estructura que mete todos los números desde el 0 hasta el que le indique.

#WHILE

i=0
while i<=10:                           #Condición para que el bucle se ejecute mientras esa condición sea verdadera.
    print(i)
    i+=1

#Manejo de excepciones                 #Control de flujo basado en problemas que pueda haber en el código conocido como "trycatch"

try:                                   
    print(10/0)
except:                                #En caso de que falle, que el programa no rompa y siga ejecutando.
    print("Se ha producido un error")
finally:                               #Esto se ejecuta siempre que se ejecute el manejo de excepciones, se produzca o no error.
    print("Ha finalizado el manejo de excepciones")


#EJERCICIOS

for a in range(10,56):
    if a%2==0 and a!=16 and a%3!=0:
        print(a)








#LECCIÓN 2
#Una función es un bloque de código, la cual se crea para reutilizar esa parte de código
#Forma de organizar, que sea más legible, que sea menos lag y que sea más fácil de mantener.

''' Funciones definidas por el usuario'''

#Simple: la palabra "def" sirve para definir una función.

def greet():                           #Se le asigna el nombre a la función.
    print("Hola, Python!")             #Se asigna lo que hará el código cada vez que llamemos a la función.

greet()                                #Creo una función que desarrolle mi lógica y cada vez que la necesite solo llamo a esa función.


#Con retorno: va a ejecutar una lógica y devuelve algo.

def return_greet():
    return "Hola, Tami"                #Solo lo retorna mas no lo imprime por la terminal.
return_greet()        

b=return_greet()                       #Acá se captura en una variable para posteriormente imprimir esa variable.
print(b)

print(return_greet())                  #También se puede imprimir directamente el resultado de llamar a la función.


#Con un argumento: Le podemos pasar algo a la función para que opere "un parámetro"

def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("jared")

#Con argumentos: Puedo pasar más de un parámetro

def args_greet(greet,name):
    print(f"{greet}, {name}!")

args_greet("hi","yalle")
args_greet("yalle","hi")               #Aquí lo desarrolla según el orden de posición que le doy.

args_greet(name="yalle",greet="hi")    #Esto se arregla: aunque no se entregue en orden he dicho a cual corresponde cada parámetro.


#Con argumentos predeterminado

def default_arg_greet(name="Python"):  #Cuando name no tenga valor, sale por defecto el valor Python.
    print(f"Hola, {name}")

default_arg_greet("Tamiti")
default_arg_greet()                    #Cuando no quieras pasar un parámetro que tenga un valor por defecto


#Con argumentos y return

def return_args_greet(greet,name):
    return f"{greet}, {name}!"

print(return_args_greet("hola","tamiti"))


#Con retorno de varios valores

def multiple_return_greet():
    return "Hola","TAMITI"              #Aquí estoy devolviendo dos cadenas de texto por separado.

great,name=multiple_return_greet()      #Desacoplamos los valores en dos variables, Separo con comas el nombre de las variables.

print(multiple_return_greet())
print(great)                            #Las trabajo de manera independiente.
print(name)



#Con un número variable de argumentos

def variable_arg_greet(*names):          #Le podemos pasar más de un argumento (infinitos), anteponiendo un asterisco al argumento
    for name in names:
        print(f"¡Hola, {name}!")
              
variable_arg_greet("Ana","Bea","Cami")   #Se entregan los argumentos separados por comas.


#Con un número variable de argumentos con palabra clave

def variable_arg_greet(**names):         #Le podemos 
    for name in names:
        print(f"¡Hola, {name}!")



''' Funciones dentro de otras funciones'''

def outer_function():                    
    def inner_function():
        print("Función interna: holaa")
    inner_function()                      # Llama a la función inner.

outer_function()                          # Ahora sí, al llamar a la función externa, llama a la interna y se ejecuta la función interna.



''' Funciones del enguaje (built-in)'''

print("Yalle")                             #Función que se encarga de imprimir por terminal el texto que le pasemos.
print(len("Tami"))                         #Función que retorna un número entero. Regresa cantidad de letras o cantidad de valores.
print(type("Yalle"))                       #Función que retorna el tipo de dato, cadena de terxto, entero, etc.
print("Tami".upper())                      #Función que dentro de la cadena de texto, vuelve ese texto mayúscula.



''' VARIABLES LOCALES Y GLOBALES'''

#Una buena práctica es siempre trabajar con variables locales ya que las globales pueden ser cambiadas por otro usuario.
#Si se necesita dicha variable fuera de la función, no se traspasa directamente la función a manera global, valorar si tiene sentido llevarla hacia afuera.

global_var="rilakkuma"                #Variable global: su ámbito es superior a lo que queremos ejecutar, a medida que vamos creando código es lo que está fuera.
print(global_var)

def gl_hello_rilakkuma():
    print(f"Hola, {global_var}")      #Acceso a la variable global pero dentro de la función. 
                                           
gl_hello_rilakkuma()

def loc_hello_rilakkuma():
    local_var="aniaseyo"              #Acá la variable está definida de manera local
    print(f"{local_var}, {global_var}")      
                                           
loc_hello_rilakkuma()                 #Funciona de manera correcta dado que es una función definida en la función y la función se ejecuta.            

print(global_var)
#print(local_var)                     #Al ser una variable local, no se puede acceder desde fuera de la función.


#EJERCICIOS
''' * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'''

def two_param(text1,text2)->int:
    count=0
    for num in range(1,101):
        if num%3==0 and num%5==0:       #Esta condición se coloca en primer lugar.
            print(text1+text2)
        elif num%3==0:
            print(text1)
        elif num%5==0:
            print(text2)
        else:
            print(num)
            count+=1                     #Para que me vaya contando todas las veces que devuelve un número, pongo un contador dentro de ese bucle.
    return count                         #Retorno el contador al final del bucle pero dentro de la función.
        
print(two_param("texto1","texto2"))
    





