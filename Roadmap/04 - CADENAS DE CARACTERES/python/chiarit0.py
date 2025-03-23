'''LECCIÓN N°4: CADENAS DE CARACTERES'''

'''


#Operaciones

s1="Hola"
s2="Tami"

#Concatenación
print(s1+s2)
print(s1+" "+s2+"!")

#Repetición
print(s1*3)

#Indexación
#Acceder a un carácter en concreto de una cadena de texto.

print(s1[0]+s2[1])

#Longitud
print(len(s2))   #Tami tiene 4 letras.

#Slicing (porción)
print(s2[1:])    #Tomar una porción de lo que quiero, toma hasta "todos" los datos finales.
print(s2[:2])    #Mismo caso en el que toma "todo"hasta el digito 2.

#Búsqueda
print("a" in s1)

#Reemplazo
print(s2.replace("a","e")) #Reemplaza el primer carácter por el segundo.

#División
print(s2.split("m"))       #Corta la cadena en la letra indicada.

#Mayúscula y minúsculas
print(s1.upper())
print(s1.lower())
print("tami yalle".title())    #La primera letra en mayúscula de cada palabra.
print("tami yalle".capitalize())    #La primera letra en mayúscula.

#Eliminación de espacios al principio y al final
print(" Tami rillakuma ".strip())   

#Búsqueda al principio y al final
print(s2.startswith("ho"))   

#Búsqueda de posición
print("Tamara tamara tamistic".find("tamara"))   #La posición es la primera coincidencia que encuentra.
print("tamara".upper().find("A"))

#Búsqueda de ocurrencias
print("tamiti".count("i"))

#Formateo
print("Saludo: {}, nombre: {}".format(s1,s2))

#Interpolación
print(f"Saludo: {s1}, nombre: {s2}")   #Anteponer el f da como resultado poder colocar variables entre las llaves.

#Transformación a lista de carácteres
print(list(s1))              #Crea una lista con todos los carácteres de mi cadena de texto.

#Transformación de lista a cadena
lista1=[s1," ",s2,"!"]
print("".join(lista1))
print("-".join(lista1))     #Lo que va entre comillas es el carácter de unión, unirá todos los elementos de la lista anteponiendo ese carácter.

#Transformaciones numéricas
s4=1234
int(s4)
print(s4)

s5=123.456
float(s5)
print(s5)

#comprobaciones varias

s4="1234"

print(s1.isalnum())       #alfanumerico (o letras o números)
print(s1.isalpha())       #alfabetico
print(s4.isalpha())       #alfabetico
print(s4.isnumeric())       #numerico
print(s4.isdigit())       #numerico 


'''
'''
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos: Misma palabra si se lee de derecha a izquierda o izquierda a derecha.
 * - Anagramas: cambio de posición de uno o más carácteres de una palabra que origina otra de distinto significado, por ejemplo amor y roma.
 * - Isogramas: no se repite ninguna letra.
 

 '''

def verificacion_palabras(palabra1,palabra2):
    
#PALINDROMO
    print(f"La palabra {palabra1} corresponde a un palíndromo: {palabra1==(palabra1[::-1])}.")
    print(f"La palabra {palabra2} corresponde a un palíndromo: {palabra2==(palabra2[::-1])}.")

    #ANAGRAMA
    print(f"Las palabras {palabra1} y {palabra2} son un anagráma: {sorted(list(palabra1))==sorted(list(palabra2))}.")

    #ISOGRAMA
    def verisograma(word):
        diccionario=dict()

        for word in palabra2:
            diccionario[word]=diccionario.get(word,0)+1
            
        isograma=True
        vectorvalorletra=list(diccionario.values())
        valorletra1=vectorvalorletra[0]

        for contador_letra in vectorvalorletra:
            if contador_letra!=valorletra1:
                isograma=False
                break                                       
        return isograma
    
    print(f"La palabra {palabra1} es un isograma: {verisograma(palabra1)}")
    print(f"La palabra {palabra2} es un isograma: {verisograma(palabra2)}")

verificacion_palabras("RECONOCER","HOLAHOLA")




