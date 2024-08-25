#Creador por
#Jeremy Chacón Beckford
#Jonathan Porras Sandí
#Bryan Castro Solís

#______________________________________________________________________________________________________________________________

#PRIMER EJERCICIO




def transposicionCod(texto):
    """
    Función que recibe como parámetro un texto y le realiza su transposición.
    Entradas y restricciones:
    - texto: es un string y no debe contener números.
    Salidas:
    - La transposicion del texto.
    """
    #Restricciones
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
    restriccionNumeros(texto)
    
    #Codigo
    texto = convertextoTransposicion(texto)
    texto = texto.split()
    textoTransposicion = ""
    palabraRev = ""

    for i in texto:
            palabraRev = i[::-1]
            palabraRev += " "
            textoTransposicion += palabraRev

    textoTransposicion = textoTransposicion.strip()
        
    return textoTransposicion


#______________________________________________________________________________________________________________________________


def transposicionDec(texto):
    """
    Función que recibe como parámetro un texto que ha
    sido códificado y lo decodifica usando el método de
    transposición.
    Entradas y restricciones:
    -texto : debe ser un string y debe estar codificado y sin números.
    Salidas:
    -El texto descodificado
    """
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
    restriccionNumeros(texto)
    
    #Codigo
    texto = convertextoTransposicion(texto)
    texto = texto.split()
    textoTransposicion = ""
    palabraRev = ""

    for i in texto:
            palabraRev = i[::-1]
            palabraRev += " "
            textoTransposicion += palabraRev

    textoTransposicion = textoTransposicion.strip()
        
    return textoTransposicion

def convertextoTransposicion(texto):
    """
    Función que recibe como parámetro un texto a codificar
    y le elimina los signos de puntuación, acentos y cáracteres
    que no sean letras.
    Entradas y restricciones:
    -texto: debe ser un string
    Salidas:
    -El texto sin signos de puntuación, acentos y cáracteres.
    """
    
    texto = texto. lower()
    texto = texto. replace("á", "a")
    texto = texto. replace("é", "e")
    texto = texto. replace("í", "i")
    texto = texto. replace("ó", "o")
    texto = texto. replace("ú", "u")
    texto = texto. replace("ü", "u")
    texto = texto. replace(",", " ")
    texto = texto. replace(".", " ")
    texto = texto. replace(";", " ")
    texto = texto. replace("?", " ")
    texto = texto. replace("¿", " ")
    texto = texto. replace("!", " ")
    texto = texto. replace("¡", " ")
    texto = texto. replace("=", " ")
    texto = texto. replace("-", " ")
    texto = texto. replace("/", " ")
    texto = texto. replace("*", " ")
    texto = texto. replace("¨", " ")
    texto = texto. replace("^", " ")
    texto = texto. replace("ç", " ")
    texto = texto. replace("¬", " ")
    texto = texto. replace("&", " ")
    texto = texto. replace("~", " ")
    texto = texto. replace("$", " ")
    texto = texto. replace("·", " ")
    texto = texto. replace("#", " ")
    texto = texto. replace("º", " ")
    texto = texto. replace("@", " ")
    texto = texto. replace("%", " ")
    texto = texto. replace("_", " ")
    texto = texto. replace("  ", " ")
    texto = texto.strip()

    return texto






#______________________________________________________________________________________________________________________________


#SEGUNDO EJERCICIO

def cesarCod(texto,desplazamiento):
    """
    Función que recibe como parámetro un texto y su número de desplazamiento
    y retorna su codificación.
    Entradas y restricciones:
    -texto: debe ser un string y no debe contener números.
    -desplazamiento: debe ser un número entero no negativo.
    Salidas:
    -El texto codificado según su cantidad indicada de desplazamientos.
    """
    
    #Restricciones
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
    if type(desplazamiento) != int or desplazamiento < 0  or desplazamiento > 27 :
        raise Exception("ERROR: debe ingresar un número y debe estar entre 1 y 27")
    restriccionNumeros(texto)
    texto = convertextoCesar(texto)
    texto = texto.split()
    textoNuevo = ""

    #Codigo
    for palabra in texto:
        textoNuevo += " "
        for letra in palabra:
            if ord(letra) + desplazamiento < 122:
                nuevaletra = (ord(letra) + desplazamiento)
                textoNuevo += chr(nuevaletra)
            else:
                nuevaletra = ((ord(letra)-26) + desplazamiento)
                textoNuevo += chr(nuevaletra)
    textoNuevo = textoNuevo.strip()
    return textoNuevo


#______________________________________________________________________________________________________________________________


def cesarDec(texto,desplazamiento):
    """
    Función que recibe como parámetro un texto codificado y su número de
    desplazamientos y retorna el texto codificado.
    Entradas y restricciones:
    -texto: debe ser un string y no debe contener números.
    -desplazamiento: debe ser un número entero no negativo.
    Salidas:
    -El texto codificado según su cantidad indicada de desplazamientos.
    """

    #Restricciones
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
    if type(desplazamiento) != int or desplazamiento < 0  or desplazamiento > 27 :
        raise Exception("ERROR: debe ingresar un número y debe estar entre 1 y 27")
    restriccionNumeros(texto)
    texto = convertextoCesar(texto)
    texto = texto.split()
    textoNuevo = ""
    

    #Codigo
    for palabra in texto:
        textoNuevo += " "
        for letra in palabra:
            if ord(letra) - desplazamiento > 96:
                nuevaletra = (ord(letra) - desplazamiento)
                textoNuevo += chr(nuevaletra)
            else:
                nuevaletra = ((ord(letra)+26) - desplazamiento)
                textoNuevo += chr(nuevaletra)

    textoNuevo = textoNuevo.strip()
    return textoNuevo

def convertextoCesar(texto):

    """
    Función que recibe como parámetro un texto a codificar
    y le elimina los signos de puntuación, acentos y cáracteres
    que no sean letras.
    Entradas y restricciones:
    -texto: debe ser un string
    Salidas:
    -El texto sin signos de puntuación, acentos y cáracteres.
    """
    
    texto = texto. lower()
    texto = texto. replace("á", "a")
    texto = texto. replace("é", "e")
    texto = texto. replace("í", "i")
    texto = texto. replace("ó", "o")
    texto = texto. replace("ú", "u")
    texto = texto. replace("ü", "u")
    texto = texto. replace(",", "")
    texto = texto. replace(".", "")
    texto = texto. replace(";", "")
    texto = texto. replace("?", "")
    texto = texto. replace("¿", "")
    texto = texto. replace("!", "")
    texto = texto. replace("¡", "")
    texto = texto. replace("=", "")
    texto = texto. replace("-", "")
    texto = texto. replace("/", "")
    texto = texto. replace("*", "")
    texto = texto. replace("¨", "")
    texto = texto. replace("^", "")
    texto = texto. replace("ç", "")
    texto = texto. replace("¬", "")
    texto = texto. replace("&", "")
    texto = texto. replace("~", "")
    texto = texto. replace("$", "")
    texto = texto. replace("·", "")
    texto = texto. replace("#", "")
    texto = texto. replace("º", "")
    texto = texto. replace("@", "")                     
    texto = texto. replace("_", "")
    texto = texto. replace("%", " ")
    texto = texto. replace("  ", " ")
    texto = texto.strip()

    return texto




#______________________________________________________________________________________________________________________________

#TERCER EJERCICIO



def binarioCod(texto):
    """
    Función que recibe como parámetro un texto y lo códifica
    a binario.
    Entradas y restricciones:
    -texto: debe ser un string y no debe contener números.
    Salidas:
    -Texto en binario.
    """
    
    #Restricciones
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
 
    texto = convertextoBinarios(texto)
    restriccionNumeros(texto)

    diccionario ={
        "a" :"00000",
        "b" :"00001",
        "c" :"00010",
        "d" :"00011",
        "e" :"00100",
        "f" :"00101",
        "g" :"00110",
        "h" :"00111",
        "i" :"01000",
        "j" :"01001",
        "k" :"01010",
        "l" :"01011",
        "m" :"01100",
        "n" :"01101",
        "ñ" :"01110",
        "o" :"01111",
        "p" :"10000",
        "q" :"10001",
        "r" :"10010",
        "s" :"10011",
        "t" :"10100",
        "u" :"10101",
        "v" :"10110",
        "w" :"10111",
        "x" :"11000",
        "y" :"11001",
        "z" :"11010",
        }

    texto = texto.split("*")

    textoBinario = ""

    for palabra in texto:
        for letra in palabra:
            if letra in diccionario and letra != "*":
                numeroBinario = diccionario[letra]
                textoBinario += numeroBinario
                textoBinario += " "
            else:
                textoBinario += "* "

    
                
    return textoBinario[:-1]
        
def convertextoBinarios(texto):
    """
 
    Función que recibe como parámetro un texto a codificar
    y le elimina los signos de puntuación, acentos y cáracteres
    que no sean letras.
    Entradas y restricciones:
    -texto: debe ser un string
    Salidas:
    -El texto sin signos de puntuación, acentos y cáracteres.
    """
    
    
    texto = texto. lower()
    texto = texto. replace("á", "a")
    texto = texto. replace("é", "e")
    texto = texto. replace("í", "i")
    texto = texto. replace("ó", "o")
    texto = texto. replace("ú", "u")
    texto = texto. replace("ü", "u")
    texto = texto. replace(",", "")
    texto = texto. replace(".", "")
    texto = texto. replace(";", "")
    texto = texto. replace("?", "")
    texto = texto. replace("¿", "")
    texto = texto. replace("!", "")
    texto = texto. replace("¡", "")
    texto = texto. replace("=", "")
    texto = texto. replace("-", "")
    texto = texto. replace("/", "")
    texto = texto. replace("*", "")
    texto = texto. replace("¨", "")
    texto = texto. replace("^", "")
    texto = texto. replace("ç", "")
    texto = texto. replace("¬", "")
    texto = texto. replace("&", "")
    texto = texto. replace("~", "")
    texto = texto. replace("$", "")
    texto = texto. replace("·", "")
    texto = texto. replace("#", "")
    texto = texto. replace("º", "")
    texto = texto. replace("@", "")
    texto = texto. replace("%", "")
    texto = texto. replace("_", "")
    texto = texto. replace("  ", " ")
    texto = texto.strip()

    return texto

#______________________________________________________________________________________________________________________________


def binarioDec(textoBinario):
    """
    Función que recibe como parámetro un texto codificado en binario
    y lo decofidica.
    Entradas y restricciones:
    -texto: debe ser un string codificado en binario
    Salidas:
    -El texto descodificado.
    """
    #Restricciones
    if type(textoBinario)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")

    diccionario ={
        "00000" :"a",
        "00001" :"b",
        "00010" :"c",
        "00011" :"d",
        "00100" :"e",
        "00101" :"f",
        "00110" :"g",
        "00111" :"h",
        "01000" :"i",
        "01001" :"j",
        "01010" :"k",
        "01011" :"l",
        "01100" :"m",
        "01101" :"n",
        "01110" :"ñ",
        "01111" :"o",
        "10000" :"p",
        "10001" :"q",
        "10010" :"r",
        "10011" :"s",
        "10100" :"t",
        "10101" :"u",
        "10110" :"v",
        "10111" :"w",
        "11000" :"x",
        "11001" :"y",
        "11010" :"z",
        }

    textoBinario = textoBinario.split()

    texto = ""

    for binario in textoBinario:
        if binario in diccionario:
                    letra = diccionario[binario]
                    texto += letra
        elif binario == "*":
            texto += " "
        
        



    return texto




#______________________________________________________________________________________________________________________________

# Cuarto Ejercicio



import random
def leetCod(texto):
    """
    Función que recibe como parámetro un string y lo
    codifica con el alfabeto 1337.
    Entradas:
    -texto: debe ser un string y no debe contener números ni letras "ñ".
    Salidas:
    -el texto codificado a el alfabeto 1337.
    """
     #Restricciones
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
    texto = texto.lower()
    restriccionNumeros(texto)
    texto = convertextoLeet(texto)
    
    biblioteca ={
        "a" : ["4","@","/-\\","/\\","^"""],
        "b" : ["8","|3","6","13","|3","]3"],
        "c" : ["(","<","¢","{","©"],
        "d" : ["|)","[)","])","I>","|>","cl"],
        "e" : ["3","&","€","[-"],
        "f" : ["|=","]=","}","ph","(="],
        "g" : ["6","(_+"],
        "h" : ["|-|","#","]-[","[-]",")-(","(-)",":-:","}{","}-{"],
        "i" : ["!","1","|","¡"],
        "j" : ["_|","_/","]","</","_)"],
        "k" : ["|<","|X","|{"],
        "l" : ["1","|_","|","|_","¬"],
        "m" : ["44","/\\/\\","|\\/|","|v|","IYI","IVI","[V]","^^","nn","//\\\\//\\\\","(V)","(\\/)","/|\\","/|/|",".\\\\","/^^\\","/V\\","|^^|"],
        "n" : ["|\\|","/\\/","//\\\\//","[\]","<\>","{\}","//","[]\[]","]\[","~"],
        "o" : ["0","()","[]","¤"],
        "p" : ["|*","|o","|º","|>","¶",'|"'],
        "q" : ["0_","0,","(,)","<|","9"],
        "r" : ["|2","/2","I2","|^","|~","®","|2","[z,l2"],
        "s" : ["5","$","z","§"],
        "t" : ["7","+","-|-"],
        "u" : ["|_|","(_)","μ","[_]" ,"\\_/" ,"\\_\"" ,"/_/"""],
        "v" : ["\/","\\\\//"],
        "w" : ["\\/\\/","vv","'//","\\\\'","\^/","(n)","\\X/","\|/","\_|_/","\\\\//\\\\//","\_:_/","]I[","UU"],
        "x" : ["%", "><", "}{", "×", ")("],
        "y" : ["`/" ,"`(" ,"-/" ,"'/"],
        "z" : ["2" ,"~/_", "7_"], 
               }
    texto = texto.split()
    
    textoLeet = ""
    

    for palabra in texto:
        textoLeet += " "
        for letra in palabra:
            if letra == "ñ":
                raise Exception('ERROR: El texto no debe contener letras "ñ"')
            elementos = len(letra)
            numAleatorio = random.randint(0,len(biblioteca[letra])-1)
            if letra in biblioteca and letra != "*":
                letraLeet = biblioteca[letra][numAleatorio]
                textoLeet += letraLeet
            else:
                textoLeet += " "
    textoLeet = textoLeet.strip()
    return textoLeet

def restriccionNumeros(texto):

    for palabra in texto:
        for letra in palabra:
            if letra.isnumeric():
                raise Exception("ERROR: El texto no debe contener números.")
    return texto


def convertextoLeet(texto):
    """
    Función que recibe como parámetro un texto a codificar
    y le elimina los signos de puntuación, acentos y cáracteres
    que no sean letras.
    Entradas y restricciones:
    -texto: debe ser un string
    Salidas:
    -El texto sin signos de puntuación, acentos y cáracteres.
    """
    
    
    texto = texto. lower()
    texto = texto. replace("á", "a")
    texto = texto. replace("é", "e")
    texto = texto. replace("í", "i")
    texto = texto. replace("ó", "o")
    texto = texto. replace("ú", "u")
    texto = texto. replace("ü", "u")
    texto = texto. replace(",", "")
    texto = texto. replace(".", "")
    texto = texto. replace(";", "")
    texto = texto. replace("?", "")
    texto = texto. replace("¿", "")
    texto = texto. replace("!", "")
    texto = texto. replace("¡", "")
    texto = texto. replace("=", "")
    texto = texto. replace("-", "")
    texto = texto. replace("/", "")
    texto = texto. replace("*", "")
    texto = texto. replace("¨", "")
    texto = texto. replace("^", "")
    texto = texto. replace("ç", "")
    texto = texto. replace("¬", "")
    texto = texto. replace("&", "")
    texto = texto. replace("~", "")
    texto = texto. replace("$", "")
    texto = texto. replace("·", "")
    texto = texto. replace("#", "")
    texto = texto. replace("º", "")
    texto = texto. replace("@", "")
    texto = texto. replace("%", "")
    texto = texto. replace("_", "")
    texto = texto. replace("  ", " ")
    texto = texto.strip()

    return texto




#______________________________________________________________________________________________________________________________

#Quinto Ejercicio



def monoCod(texto, palabraClave):
    """
    Función que recibe como parámetro un texto y una palabra
    clave la cual sirve para codificar el texto mediante un
    nuevo abecedario.
    Entradas y restricciones:
    -texto: debe ser un string y no debe contener números.
    -palabraClave: debe ser un string y no debe contener números.    
    Salidas:
    -El texto codificado.
    """


    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")

    restriccionNumeros(texto)
    
    texto = texto.lower()
    texto = convertextoMono(texto)
    palabraClave = palabraClave.lower()
    palabraClave = convertextoMono(palabraClave)
    texto = texto.split()

    
    
    abecedario = ["a" ,"b" ,"c" ,"d", "e", "f", "g", "h","i", "j", "k", "l","m", "n", "ñ", "o", "p","q", "r", "s", "t", "u", "v","w" "x", "y","z"]

    abecedarioConver = ["a" ,"b" ,"c" ,"d", "e", "f", "g", "h","i", "j", "k", "l","m", "n", "ñ", "o", "p","q", "r", "s", "t", "u", "v","w", "x", "y","z"]
    abecedarioCod = []
    palabraClaveEspacios = palabraClave
    palabraClave = ""
    textoNuevo = ""

    for letra in palabraClaveEspacios:
        palabraClave += " "
        palabraClave += letra

    palabraClave = palabraClave.strip()
    palabraClave = palabraClave.split()

    for letra in palabraClave:
        if letra in abecedarioConver:
            abecedarioCod += [letra]
            abecedarioConver.remove(letra)

    abecedarioCod += abecedarioConver
    

    for palabra in texto:
        textoNuevo += " "
        for letra in palabra:
            posicion = abecedario.index(letra)
            textoNuevo += abecedarioCod[posicion]

    
    textoNuevo = textoNuevo.strip()  
        

    return textoNuevo


#______________________________________________________________________________________________________________________________


def monoDec(texto, palabraClave):
    """
    Función que recibe como parámetro un texto codificado y una
    palabra clave la cual sirve para decodificar el texto mediante
    un nuevo abecedario.
    Entradas y restricciones:
    -texto: debe ser un string y no debe contener números.
    -palabraClave: debe ser un string y no debe contener números.    
    Salidas:
    -El texto decodificado.
    """


    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")

    restriccionNumeros(texto)
    
    texto = texto.lower()
    texto = convertextoMono(texto)
    palabraClave = palabraClave.lower()
    palabraClave = convertextoMono(palabraClave)
    texto = texto.split()

    
    
    abecedario = ["a" ,"b" ,"c" ,"d", "e", "f", "g", "h","i", "j", "k", "l","m", "n", "ñ", "o", "p","q", "r", "s", "t", "u", "v", "x", "y","z"]

    abecedarioConver = ["a" ,"b" ,"c" ,"d", "e", "f", "g", "h","i", "j", "k", "l","m", "n", "ñ", "o", "p","q", "r", "s", "t", "u", "v", "x", "y","z"]
    abecedarioCod = []
    palabraClaveEspacios = palabraClave
    palabraClave = ""
    textoDec = ""

    for letra in palabraClaveEspacios:
        palabraClave += " "
        palabraClave += letra

    palabraClave = palabraClave.strip()
    palabraClave = palabraClave.split()

    for letra in palabraClave:
        if letra in abecedarioConver:
            abecedarioCod += [letra]
            abecedarioConver.remove(letra)

    abecedarioCod += abecedarioConver
    

    for palabra in texto:
        textoDec += " "
        for letra in palabra:
            posicion = abecedarioCod.index(letra)
            textoDec += abecedario[posicion]

    
    textoDec = textoDec.strip() 
        

    return textoDec




def convertextoMono(texto):
    """
    Función que recibe como parámetro un texto a codificar
    y le elimina los signos de puntuación, acentos y cáracteres
    que no sean letras.
    Entradas y restricciones:
    -texto: debe ser un string
    Salidas:
    -El texto sin signos de puntuación, acentos y cáracteres.
    """
    
    
    texto = texto. lower()
    texto = texto. replace("á", "a")
    texto = texto. replace("é", "e")
    texto = texto. replace("í", "i")
    texto = texto. replace("ó", "o")
    texto = texto. replace("ú", "u")
    texto = texto. replace("ü", "u")
    texto = texto. replace(",", " ")
    texto = texto. replace(".", " ")
    texto = texto. replace(";", " ")
    texto = texto. replace("?", " ")
    texto = texto. replace("¿", " ")
    texto = texto. replace("!", " ")
    texto = texto. replace("¡", " ")
    texto = texto. replace("=", " ")
    texto = texto. replace("-", " ")
    texto = texto. replace("/", " ")
    texto = texto. replace("*", " ")
    texto = texto. replace("¨", " ")
    texto = texto. replace("^", " ")
    texto = texto. replace("ç", " ")
    texto = texto. replace("¬", " ")
    texto = texto. replace("&", " ")
    texto = texto. replace("~", " ")
    texto = texto. replace("$", " ")
    texto = texto. replace("·", " ")
    texto = texto. replace("#", " ")
    texto = texto. replace("º", " ")
    texto = texto. replace("@", " ")
    texto = texto. replace("%", " ")
    texto = texto. replace("_", " ")
    texto = texto. replace("  ", " ")
    texto = texto.strip()
    return texto


#______________________________________________________________________________________________________________________________

#Sexto Ejercicio

def vigenereCod(texto,palabra):
    """
    Función que recibe como parámetro un texto y una palabra
    clave la cual sirve para codificar cada palabra que se
    encuentre dentro del texto, sumandole la posicion de cada
    letra del texto a la posicion de cada letra en la palabra
    clave.
    Entradas y restricciones:
    - texto: debe ser un string y no debe contener números.
    - palabraClave: debe ser un string y no debe contener números.
    Salidas:
    - Texto codificado.
    """
    #Restricciones
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")

    if type(palabra)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
    
    restriccionNumeros(texto)
    
    texto = converTextoVigenere(texto)
    palabra = palabra.lower()

    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    textocifr = ""
    recorre = 0

    for letra in texto:
        if letra != " ":
            suma = abecedario.find(letra) + abecedario.find(palabra[recorre % len(palabra)])
            if suma > 26:
                suma -= 27
                modulo = int(suma) % len(abecedario)
                textocifr = textocifr + str(abecedario[modulo]) 
                recorre = recorre + 1
            else:
                modulo = int(suma) % len(abecedario)
                textocifr = textocifr + str(abecedario[modulo]) 
                recorre = recorre + 1
        else:
            textocifr += " "

    return textocifr    


#______________________________________________________________________________________________________________________________

    
def vigenereDec(texto,palabra):
    """
    Función que recibe como parámetro un texto codificado
    y una palabra clave la cual sirve para decodificar cada
    palabra que se encuentre dentro del texto, restandole la
    posicion de cada letra de la palabra clave a cada letra
    del texto codificado.
    Entradas y restricciones:
    - texto: debe ser un string y no debe contener números.
    - palabraClave: debe ser un string y no debe contener números.
    Salidas:
    - Texto decodificado.
    """
    #Restricciones
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")

    if type(palabra)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
    restriccionNumeros(texto)

    texto = converTextoVigenere(texto)
    palabra = palabra.lower()

    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    textoDec = ""
    recorre = 0

    for letra in texto:
        if letra != " ":
            suma = abecedario.find(letra) - abecedario.find(palabra[recorre % len(palabra)])
            if suma > 26:
                suma -= 27
                modulo = int(suma) % len(abecedario)
                textoDec = textoDec + str(abecedario[modulo]) 
                recorre = recorre + 1
            else:
                modulo = int(suma) % len(abecedario)
                textoDec = textoDec + str(abecedario[modulo]) 
                recorre = recorre + 1
        else:
            textoDec += " "

    return textoDec







#______________________________________________________________________________________________________________________________

#Sétimo Ejercicio

    
def playfairCod(texto,palabra):
    """
    Función que recibe como parametro un texto y una palabra clave
    mediante la cual se genera una  matriz  que  ayuda a codificar
    texto de dos en dos letras.
    Entradas y restricciones:
    -texto: Debe ser un string y no debe contener números.
    -palabra: Debe ser un string y no debe contener números.
    Salidas:
    -Texto codificado.
    """
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")

    if type(palabra)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")
    
    texto = convertextoPlayfair(texto)
    texto = texto.lower()
    palabra = palabra.lower()
    palabra = palabraSinRepetidas(palabra)
    texto = textoSinRepetidas(texto)
    texto = textoListaParesCod(texto)
    
    
    abecedario = ["a" ,"b" ,"c" ,"d", "e", "f", "g", "h","i", "j", "k", "l","m", "n", "ñ", "o", "p","q", "r", "s", "t", "u", "v","w", "x", "y","z"]
    abcFilaColum = {"1":[5,2],"2":[5,3],"3":[5,4]}
    matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,"1","2","3"]]
    fila = 0
    colum = 0

    for letra in palabra:
        if colum != 5:
            matriz[fila][colum] = letra
            abcFilaColum[letra] = [fila,colum]
            colum += 1
            abecedario.remove(letra)
        else:
            colum = 0
            fila += 1
            abcFilaColum[letra] = [fila,colum]
            matriz[fila][colum] = letra
            colum += 1
            abecedario.remove(letra)
 
    for letra in abecedario:
        if colum != 5:
            matriz[fila][colum] = letra
            abcFilaColum[letra] = [fila,colum]
            colum += 1
        else:
            colum = 0
            fila += 1
            abcFilaColum[letra] = [fila,colum]
            matriz[fila][colum] = letra
            colum += 1

    textoCod = ""    
    for letra1,letra2 in texto:
        dosLetras = letra1 + letra2
        if dosLetras == "**":
            textoCod += "  "
        #Caso 1
        elif  abcFilaColum[letra1][0] != abcFilaColum[letra2][0] and abcFilaColum[letra1][1] != abcFilaColum[letra2][1]:
            letrasNuevas = caso1playfair(letra1,letra2,matriz,abcFilaColum)
            textoCod += letrasNuevas
        #Caso 2
        elif abcFilaColum[letra1][0] == abcFilaColum[letra2][0]:
            letrasNuevas = caso2playfair(letra1,letra2,matriz,abcFilaColum)
            textoCod += letrasNuevas
        #Caso 3
        elif abcFilaColum[letra1][1] == abcFilaColum[letra2][1]:
            letrasNuevas = caso3playfair(letra1,letra2,matriz,abcFilaColum)
            textoCod += letrasNuevas
            
    textoCod = textoCod.replace("  "," ")
    
    return textoCod

def palabraSinRepetidas(palabra):
    """
    Subrutina que recibe como parametro una palabra y retorna una
    palabra nueva la cual no contiene letras repetidas.
    Entradas y restricciones:
    - palabra: Es un string
    Salidas:
    - Palabra sin letras repetidas.
    """   
    palabraNueva = ""
    
    for letra in palabra:
        if letra not in palabraNueva:
            palabraNueva += letra

    
    return palabraNueva
    
def textoSinRepetidas(texto):
    """
    Subrutina que recibe como parametro una texto y lo modifica para
    que cada letra repetidas se separe por un 1.
    Entradas y restricciones:
    - Texto: Es un string.
    Salidas:
    - Texto con letras repetidas separadas por un 1.
    """   
    texto = texto.replace ("aa","a1a")
    texto = texto.replace ("bb","b1b")
    texto = texto.replace ("cc","c1c")
    texto = texto.replace ("dd","d1d")
    texto = texto.replace ("ee","e1e")
    texto = texto.replace ("ff","f1f")
    texto = texto.replace ("gg","g1g")
    texto = texto.replace ("hh","h1h")
    texto = texto.replace ("ii","i1i")
    texto = texto.replace ("jj","j1j")
    texto = texto.replace ("kk","k1k")
    texto = texto.replace ("ll","l1l")
    texto = texto.replace ("mm","m1m")
    texto = texto.replace ("nn","n1n")
    texto = texto.replace ("ññ","ñ1ñ")
    texto = texto.replace ("oo","o1o")
    texto = texto.replace ("pp","p1p")
    texto = texto.replace ("qq","q1q")
    texto = texto.replace ("rr","r1r")
    texto = texto.replace ("ss","s1s")
    texto = texto.replace ("tt","t1t")
    texto = texto.replace ("uu","u1u")
    texto = texto.replace ("vv","v1v")
    texto = texto.replace ("ww","w1w")
    texto = texto.replace ("xx","x1x")
    texto = texto.replace ("yy","y1y")
    texto = texto.replace ("zz","z1z")
    
    return texto 


def textoListaParesCod(texto):
    """
    Subrutina que recibe el texto y retorna una lista de
    pares de letras.
    Entradas y restricciones:
    - texto: Es un string.
    Salidas:
    - Lista de pares de letras.
    """
    
    textoNuevo = ""

    texto = texto.split()
    
    i = 0
    for palabra in texto:
        if len(palabra) % 2 != 0:
            palabra += "1"
        for letra in palabra:
            if i != 1:
                i += 1
                textoNuevo += letra
            elif i == 1:
                i = 0
                textoNuevo += letra
                textoNuevo += " "
                
        textoNuevo += "** "
    
    textoNuevo = textoNuevo.split()
    
    return textoNuevo[:-1]


def caso1playfair(letra1,letra2,matriz,abcFilaColum):
    """
    Subrutina que recibe como parametro el par de letras de un texto y por
    medio de la matriz y el diccionario abcFilaColum retorna un nuevo par
    de letras codificadas mediante las operaciones del caso 1.
    Entradas y restricciones:
    - letra1: Es una letra en string.
    - letra2: Es una letra en string.
    - matriz: Lista de filas y columnas de un texto.
    - abcFilaColum: Diccionario que contiene letras asociadas con fila
                    y columna de su posicion.
    Salidas:
    - Letras codificadas.
    """
    
    nuevaFila1 = abcFilaColum[letra1][0]
    nuevaFila2 = abcFilaColum[letra2][0]
   
    colum1 = abcFilaColum[letra2][1]
    colum2 = abcFilaColum[letra1][1]

    letraNueva1 = str(matriz[nuevaFila1][colum1])
    letraNueva2 = str(matriz[nuevaFila2][colum2])

    letrasNuevas = letraNueva1 + letraNueva2 
  
    return letrasNuevas

def caso2playfair(letra1,letra2,matriz,abcFilaColum):
    """
    Subrutina que recibe como parametro el par de letras de un texto y por
    medio de la matriz y el diccionario abcFilaColum retorna un nuevo par
    de letras codificadas mediante las operaciones del caso 2.
    Entradas y restricciones:
    - letra1: Es una letra en string.
    - letra2: Es una letra en string.
    - matriz: Lista de filas y columnas de un texto.
    - abcFilaColum: Diccionario que contiene letras asociadas con fila
                    y columna de su posicion.
    Salidas:
    - Letras codificadas.
    """
    fila = abcFilaColum[letra1][0]

    colum1 = abcFilaColum[letra1][1]
    colum2 = abcFilaColum[letra2][1]
 
    if colum1 > 3:
        colum1 -= 4
    else:
        colum1 +=1

    if colum2 > 3:
        colum2 -= 4
    else:
        colum2 +=1
  
    letraNueva1 = str(matriz[fila][colum1])
    letraNueva2 = str(matriz[fila][colum2])

    letrasNuevas = letraNueva1 + letraNueva2

    return letrasNuevas
    
def caso3playfair(letra1,letra2,matriz,abcFilaColum):
    """
    Subrutina que recibe como parametro el par de letras de un texto y por
    medio de la matriz y el diccionario abcFilaColum retorna un nuevo par
    de letras codificadas mediante las operaciones del caso 3.
    Entradas y restricciones:
    - letra1: Es una letra en string.
    - letra2: Es una letra en string.
    - matriz: Lista de filas y columnas de un texto.
    - abcFilaColum: Diccionario que contiene letras asociadas con fila
                    y columna de su posicion.
    Salidas:
    - Letras codificadas.
    """
    colum = abcFilaColum[letra1][1]

    fila1 = abcFilaColum[letra1][0]
    fila2 = abcFilaColum[letra2][0]

    if fila1 > 4:
        fila1 -= 5
    else:
        fila1 +=1

    if fila2 > 4:
        fila2 -= 5
    else:
        fila2 +=1

    letraNueva1 = str(matriz[fila1][colum])
    letraNueva2 = str(matriz[fila2][colum])

    letrasNuevas = letraNueva1 + letraNueva2
    return letrasNuevas

def convertextoPlayfair(texto):
        
    """
    Función que recibe como parámetro un texto a codificar
    y le elimina los signos de puntuación, acentos y cáracteres
    que no sean letras.
    Entradas y restricciones:
    -texto: debe ser un string
    Salidas:
    -El texto sin signos de puntuación, acentos y cáracteres.
    """
    texto = texto.lower()
    texto = texto. replace("á", "a")
    texto = texto. replace("é", "e")
    texto = texto. replace("í", "i")
    texto = texto. replace("ó", "o")
    texto = texto. replace("ú", "u")
    texto = texto. replace("ü", "u")
    texto = texto. replace(",", "")
    texto = texto. replace(".", "")
    texto = texto. replace(";", "")
    texto = texto. replace("?", "")
    texto = texto. replace("¿", "")
    texto = texto. replace("!", "")
    texto = texto. replace("¡", "")
    texto = texto. replace("=", "")
    texto = texto. replace("-", "")
    texto = texto. replace("/", "")
    texto = texto. replace("*", "")
    texto = texto. replace("+", "")
    texto = texto. replace("¨", "")
    texto = texto. replace("^", "")
    texto = texto. replace("ç", "")
    texto = texto. replace("¬", "")
    texto = texto. replace("&", "")
    texto = texto. replace("~", "")
    texto = texto. replace("$", "")
    texto = texto. replace("·", "")
    texto = texto. replace("#", "")
    texto = texto. replace("º", "")
    texto = texto. replace("@", "")
    texto = texto. replace("%", "")
    texto = texto. replace("_", "")
    texto = texto. replace("  ", " ")
    return texto

#______________________________________________________________________________________________________________________________



def playfairDec(texto,palabra):
    """
    Función que recibe como parametro un texto y una palabra clave
    mediante la cual se genera una  matriz  que  ayuda a codificar
    texto de dos en dos letras.
    Entradas y restricciones:
    -texto: Debe ser un string y no debe contener números.
    -palabra: Debe ser un string y no debe contener números.
    Salidas:
    -Texto codificado.
    """
    
    if type(texto)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")

    if type(palabra)!= str:
        raise Exception ("ERROR:El texto ingresado debe ser un string.")

    texto = convertextoPlayfair(texto)
    texto = texto.lower()
    palabra = palabra.lower()
    palabra = palabraSinRepetidas(palabra)
    texto = textoListaParesDec(texto)
    
    abecedario = ["a" ,"b" ,"c" ,"d", "e", "f", "g", "h","i", "j", "k", "l","m", "n", "ñ", "o", "p","q", "r", "s", "t", "u", "v","w", "x", "y","z"]
    abcFilaColum = {"1":[5,2],"2":[5,3],"3":[5,4]}
    matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,2,3]]
    fila = 0
    colum = 0

    for letra in palabra:
        if colum != 5:
            matriz[fila][colum] = letra
            abcFilaColum[letra] = [fila,colum]
            colum += 1
            abecedario.remove(letra)
        else:
            colum = 0
            fila += 1
            abcFilaColum[letra] = [fila,colum]
            matriz[fila][colum] = letra
            colum += 1
            abecedario.remove(letra)
 
    for letra in abecedario:
        if colum != 5:
            matriz[fila][colum] = letra
            abcFilaColum[letra] = [fila,colum]
            colum += 1
        else:
            colum = 0
            fila += 1
            abcFilaColum[letra] = [fila,colum]
            matriz[fila][colum] = letra
            colum += 1

    textoDec = ""    
    for letra1,letra2 in texto:
        dosLetras = letra1 + letra2
        if dosLetras == "**":
            textoDec += " "
        #Caso 1
        elif  abcFilaColum[letra1][0] != abcFilaColum[letra2][0] and abcFilaColum[letra1][1] != abcFilaColum[letra2][1]:
            letrasNuevas = caso1playfairDec(letra1,letra2,matriz,abcFilaColum)
            textoDec += letrasNuevas
        #Caso 2
        elif abcFilaColum[letra1][0] == abcFilaColum[letra2][0]:
            letrasNuevas = caso2playfairDec(letra1,letra2,matriz,abcFilaColum)
            textoDec += letrasNuevas
        #Caso 3
        elif abcFilaColum[letra1][1] == abcFilaColum[letra2][1]:
            letrasNuevas = caso3playfairDec(letra1,letra2,matriz,abcFilaColum)
            textoDec += letrasNuevas

    for letras in textoDec:
        if letras == "1":
            textoDec = textoDec.replace("1","")
    
    return textoDec

def textoListaParesDec(texto):
    """
    Subrutina que recibe el texto y retorna una lista de
    pares de letras.
    Entradas y restricciones:
    - texto: Es un string.
    Salidas:
    - Lista de pares de letras.
    """
    
    textoNuevo = ""

    texto = texto.split()
    
    i = 0
    for palabra in texto:
        if len(palabra) % 2 != 0:
            palabra += "1"
        for letra in palabra:
            if i != 1:
                i += 1
                textoNuevo += letra
            elif i == 1:
                i = 0
                textoNuevo += letra
                textoNuevo += " "
                
        textoNuevo += "** "

    textoNuevo = textoNuevo.split()
  
    return textoNuevo[:-1]

def caso1playfairDec(letra1,letra2,matriz,abcFilaColum):
    """
    Subrutina que recibe como parametro el par de letras codificadas
    de un texto y por medio de la matriz y el diccionario abcFilaColum
    retorna un nuevo par de letras decodificadas mediante las operaciones
    del caso 1.
    Entradas y restricciones:
    - letra1: Es una letra en string.
    - letra2: Es una letra en string.
    - matriz: Lista de filas y columnas de un texto.
    - abcFilaColum: Diccionario que contiene letras asociadas con fila
                    y columna de su posicion.
    Salidas:
    - Letras codificadas.
    """
    
    nuevaFila1 = abcFilaColum[letra1][0]
    nuevaFila2 = abcFilaColum[letra2][0]

    colum1 = abcFilaColum[letra2][1]
    colum2 = abcFilaColum[letra1][1]

    letraNueva1 = str(matriz[nuevaFila1][colum1])
    letraNueva2 = str(matriz[nuevaFila2][colum2])

    letrasNuevas = letraNueva1 + letraNueva2 
    
    return letrasNuevas

def caso2playfairDec(letra1,letra2,matriz,abcFilaColum):
    """
    Subrutina que recibe como parametro el par de letras codificadas
    de un texto y por medio de la matriz y el diccionario abcFilaColum
    retorna un nuevo par de letras decodificadas mediante las operaciones
    del caso 2.
    Entradas y restricciones:
    - letra1: Es una letra en string.
    - letra2: Es una letra en string.
    - matriz: Lista de filas y columnas de un texto.
    - abcFilaColum: Diccionario que contiene letras asociadas con fila
                    y columna de su posicion.
    Salidas:
    - Letras codificadas.
    """

    fila = abcFilaColum[letra1][0]

    colum1 = abcFilaColum[letra1][1]
    colum2 = abcFilaColum[letra2][1]

    if colum1 < 0:
        colum1 += 5
    else:
        colum1 -=1

    if colum2 < 0:
        colum2 += 5
    else:
        colum2 -=1

    letraNueva1 = str(matriz[fila][colum1])
    letraNueva2 = str(matriz[fila][colum2])

    letrasNuevas = letraNueva1 + letraNueva2

    return letrasNuevas
    
def caso3playfairDec(letra1,letra2,matriz,abcFilaColum):
    """
    Subrutina que recibe como parametro el par de letras codificadas
    de un texto y por medio de la matriz y el diccionario abcFilaColum
    retorna un nuevo par de letras decodificadas mediante las operaciones
    del caso 3.
    Entradas y restricciones:
    - letra1: Es una letra en string.
    - letra2: Es una letra en string.
    - matriz: Lista de filas y columnas de un texto.
    - abcFilaColum: Diccionario que contiene letras asociadas con fila
                    y columna de su posicion.
    Salidas:
    - Letras codificadas.
    """

    colum = abcFilaColum[letra1][1]

    fila1 = abcFilaColum[letra1][0]
    fila2 = abcFilaColum[letra2][0]

    if fila1 < 0:
        fila1 += 6
    else:
        fila1 -=1

    if fila2 < 0:
        fila2 += 6
    else:
        fila2 -=1
    
    letraNueva1 = str(matriz[fila1][colum])
    letraNueva2 = str(matriz[fila2][colum])

    letrasNuevas = letraNueva1 + letraNueva2

    return letrasNuevas
















    

    



