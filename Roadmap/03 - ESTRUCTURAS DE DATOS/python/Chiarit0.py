# LECCIÓN 3: ESTRUCTURA DE DATOS
#Una estructura en un lenguaje nos sirve para organizar datos.

#LISTAS
#Es una estructura ordenada donde empezamos a guardar varios elementos de manera ordenada.
#Se crea con corchetes [ ].

'''
my_list:list=["Tami","Yalle","Titu","Niquito"]
print(my_list)

my_list.append("Ochin")           #Inserción: Agrego un nuevo elemento, se añade al final.
print(my_list)
 
my_list.remove("Tami")            #Borrado: Elimino cierto elemento de la lista.
print(my_list)

my_list[1]                        #Accedo a la posición de la lista [1], como se cuenta desde 0 hacia adelante en este caso "Titu" sería la posición 1.
print(my_list[1])

my_list[1]="Roco"                 #Actualización: Accedo a la posición 1 y la cambio por otro valor.

print(my_list)

my_list.sort()                    #Ordenación: Por defecto en Python, ordena alfabeticamente o en caso de números, de menor a mayor.
print(my_list)

print(type(my_list))              #Para serciorarnos que es una lista.


#TUPLAS
#Es una estructura donde se pueden guardar datos pero son inmutables, es decir, como se creen al inicio es como será (no es posible cambiarlas).
#Se crea con entre parentesis ( ).

my_tuple:tuple=("Tami","Ingeniera","27")
print(my_tuple)
print(my_tuple[2])                #Acceso
my_tuple=sorted(my_tuple)         #Sorted (ordenar) vuelve la tupla a lista, considerar que no se pueden combinar string y n° enteros, por lo que el "27" ahora es string.

print(type(my_tuple))             #Para serciorarnos que es una tupla, sin embargo, nos damos cuenta que el sorted lo transforma en lista.

my_tuple=tuple(sorted(my_tuple))  #Vuelve a tupla. Se puede hacer la ordenación pero pasandola a una lista entre medio.
print(type(my_tuple))

print(my_tuple)                   #('27', 'Ingeniera', 'Tami') Ordena primero n° y luego alfabéticamente.


#SETS
#Estructura no ordenada, utilizada para guardar muchos datos guardados de forma óptima donde no se permite el duplicado de datos.
#Manera de serializar los datos para acceder de manera sencilla a ellos de manera interna, sirve principalmente para evitar duplicados. 
#Se crea con llaves { }.

my_set:set={"Tami","Rilakkuma","Kpop","anime"}
print(my_set)
#print(my_set[0])                  No hay forma de acceder un valor, porque no está ordenado.
my_set.add("tami.vmq@gmail.com")   #Inserción.
my_set.add("tami.vmq@gmail.com")   #Inserción duplicada: Al ver que es el mismo dato no lo inserta.
print(my_set)
print(type(my_set))

my_set.remove("anime")
print(my_set)

#my_set.update                     #No es cambiar un dato por otro. Ampliar los datos que ya se tiene en ese set por si se quiere concadenar más datos.
                                   #La mejor forma de actualizar es remover un dato y agregar uno nuevo.
my_set=sorted(my_set)
print(my_set)
print(type(my_set))                #Se vuelve una lista al sortearlos.

my_set=set(sorted(my_set))         #No se puede ordenar ya que lo vuelve un set.
print(my_set)
print(type(my_set)) 


#DICCIONARIOS
#La manera de guardar los datos es clave y valor. Una clave es un punto de acceso para llegar a un dato.
#La estructura de una diccionario no es ordenada. Sin embargo, en Python a nivel de diseño guarda los datos de manera ordenada.
#También se coloca entre llaves { }.

my_dict:dict={"name":"Tami",
             "ocio":"anime",
             "mascotas":"perro"}
print(my_dict)                      #No hay una estructura como tal en la cual podamos acceder a cada uno de los elementos.
print(type(my_dict))

print(my_dict["name"])              #Acceso: como no se puede acceder por posición, se accede por clave.

my_dict["email"]="tamara.vmq@gmail.com"  #Inserción: Agrego una nueva clave con su respectivo dato.
print(my_dict)

my_dict["ocio"]="kpop"              #Actualización: Se busca la clave y se cambia al nuevo valor.
print(my_dict)

del my_dict["mascotas"]             #Eliminación: se utiliza una función de Python delete para sacar la clave y por ende también el dato del diccionario.
print(my_dict)

#my_dict=sorted(my_dict)            #Ordena y entrega en la impresión solo las claves y lo transforma en lista.

#my_dict=sorted(my_dict.items())    #Se le agrega "items" para hacer que devuelva tanto las claves como los datos.
                                    #Devuelve una lista con tuplas ordenadas alfabeticamente por clave.

my_dict=dict(sorted(my_dict.items()))#Se transforma en diccionario nuevamente.
print(my_dict)                      

print(type(my_dict))  '''


''' * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.'''

agenda:dict= {}

def insercion_contacto():
    telefono=input("Ingrese número de teléfono: ")
    if telefono.isdigit and len(telefono)>0 and len(telefono)<=11:
                agenda[nombre]=telefono
                print("El contacto se ha guardado correctamente")
    else:
        telefono=input("Ingrese un número de teléfono hasta 11 dígitos: ")
        print("El contacto se ha guardado correctamente")

while True:   # Condición que siempre es verdadero, la condición no va a cambiar nunca y se va a ejecutar infinito a no ser que se rompa.

    print("")     #Para un salto de linea en la ejecución.
    print("1. Presione 1 para insertar un contacto." )
    print("2. Presione 2 para buscar un contacto." )
    print("3. Presione 3 para actualizar un contacto." )
    print("4. Presione 4 para eliminar un contacto." )
    print("5. Presione 5 para salir." )

    acción=input("\nIngrese n° para acción deseada: ")     #\n para salto de linea.

    if acción == "1":
        nombre=input("Ingrese nombre: ")
        insercion_contacto()
        
    elif acción == "2":
        opcion=input("Ingrese 1 si desea buscar por nombre de contacto o 2 si desea buscar por teléfono de contacto: ")
        if opcion=="1":
            nombre=input("Ingrese nombre de contacto a buscar: ")
            if nombre in agenda:
                print(f"El número de contacto de {nombre} es: {agenda[nombre]}")
            else:
                print("No se ha encontrado contacto")
        elif opcion=="2":
            buscar_telefono=input("Ingrese número de telefono del contacto a buscar: ")
            for nombre, telefono in agenda.items():
                if buscar_telefono==telefono:
                    print(f"El nombre de contacto al cual pertenece el número {buscar_telefono} es: {nombre}")
        
                else:
                    print("No se ha encontrado contacto")
    
    elif acción == "3":
        opcion=input("Ingrese 1 para actualizar nombre o 2 para número telefónico: ")
        nombre=input("Ingrese nombre de contacto a actualizar: ")
        if opcion=="1":
            if nombre in agenda:
                nuevonombre=input("Ingrese nuevo nombre de contacto: ")
                agenda[nuevonombre]=agenda[nombre]
                del agenda[nombre]
                print(f"El contacto {nuevonombre} se ha guardado correctamente con el número de contacto {agenda[nuevonombre]}")
            else:
                print("Ese nombre no se encuentra en la agenda")
        elif opcion=="2":
            insercion_contacto()
        else:
            opcion=input("Ingrese una opción válida: ")
            
    elif acción == "4":
        opcion=input("Ingrese 1 para eliminar contacto por nombre de contacto o 2 para eliminar contacto por número telefónico: ")
        if opcion=="1":
            nombre=input("Ingrese nombre de contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"El contacto {nombre} ha sido eliminado")
            else:
                ("No se encuentra en la agenda")
        elif opcion=="2":
            telefono_eliminar=input("Ingrese teléfono a eliminar: ")
            for nombre, telefono in agenda.items():
                if telefono_eliminar==telefono:
                    del agenda[nombre]
                    print(f"El contacto con el número {telefono_eliminar} ha sido eliminado")
                break
            else:
                print("No se ha encontrado contacto")
                
    elif acción == "5":
        print("Ha salido de la agenda")
        break                                            #BREAK: salir del bucle que se está ejecutando.
        
    else:
        x=input("Por favor ingrese una opción válida: ")


#MATCH OPTION: es como hacer diferentes if y elif donde se ve el valor que va adquiriendo 1 sola variable, en este caso la variable "acción" puede ir tomando
#valores desde el 1 al 5.

#Se utiliza if cuando hay condiciones complejas. Cuando no quiero revisar condiciones más complejas, sino que solo quiero ver los dieferentes valores que va
#adquiriendo "acción", utilizo match option.


















