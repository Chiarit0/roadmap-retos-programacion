#LECCIÓN 7: PILAS Y COLAS
#Son dos estructuras básicas. Tienen un mecanismo muy concreto de como trabajar con los datos.

#Pila/Stack (LIFO) Last in First out
#Ejemplo, en una pila de libros en los cuales los apilas hacia arriba, el último libro que colocas (que está encima) es el primero que elegirás cuando quieras uno.
'''
stack = []
stack.append("1")    #Push: cada vez que le agregamos un elemento a una pila.
stack.append("2")    #Push
stack.append("3")    #Push

#pop: desapilar o sacar un elemento de la pila
stack_item = stack[len(stack)-1]
print(stack_item)
del stack[len(stack)-1]


print(stack.pop())   #Ya existe una función en python para eliminar el último. "pop"
print(stack)


#Cola/Queue   FIFO    First in First out
#Ejemplo en una cola para el cine, la primera persona en la cola para comprar una entrada será la primera atendida y por ende la primera en salir.

#enqueue
queue = []
queue.append(1)
queue.append(2)
queue.append(3)

#dequeue
print(queue.pop(0))   #Se elimina pero el primero elemento.
print(queue) '''


''' * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.'''


#Pilas y cadenas de texto 
def navegador_web():
    navegador:list = []

    while True:

        accion = input("Escriba acción: ")
        
        if accion == "adelante":
            pass
        elif accion == "atras":
            if len(navegador)>0:
                navegador.pop()
        else:
            navegador.append(accion)
    
        if len(navegador)>0:
            print(f"Estás en: {navegador[len(navegador)-1]}")
        else:
            print("Estas en el home")

#navegador_web()


archivo:list= []

def imprimir_archivo():
    while True:
        doc=input("ingrese nombre de documento o 'imprimir: '")
    
        if doc=="imprimir":
            print(f"Imprimiendo el archivo {archivo.pop(0)}")
        else:
            archivo.append(doc)

        print(f"Cola de impresión: {archivo}")

imprimir_archivo()