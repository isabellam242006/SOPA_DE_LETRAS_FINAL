import numpy as np #Para trabajar con matrices, numpy genera una compresion de listas y la resume en funciones
import random
import pandas as pd #Pandas permite generar la matriz de una forma mas organizada omitiendo las comas y los corchetes
                    #ademas de permitir el uso de coordenadas para las palabras
                    
#Esta función nos permite imprimir las funciones del juego
def Instrucciones():
    print()
    print("¡BIENVENIDO/A A LA SOPA DE LETRAS MORATERA!")
    print()
    print("Antes de empezar, te presentaremos las reglas del juego.")
    print()
    print("1. Este juego tendrá 3 niveles de dificultad (Fácil, Medio y Difícil).")
    print("   Nivel Fácil: Matriz 15x15 - 7 palabras ingresadas por categoria o por el usuario.")
    print("   Nivel Medio: Matriz 20x20 - 10 palabras ingresadas por categoria o por el usuario.")
    print("   Nivel Difícil: Matriz 30x30 - 15 palabras ingresadas por categoria o por el usuario.")
    print()
    print("2. Deberas ingresar 2 coordenadas para identificar la posición de la palabra.")
    print("   Las coordenadas serán la primera y ultima letra de la palabra.")
    print("   Fila 1/Columna 1 será la primera letra de la palabra, y Fila 2/Columna 2 será la ultima letra de la palabra.")
    print()
    print("3. Asegúrate de que todas las palabras que ingreses esten en mayúsculas y con buena ortografía.")
    print()
    print("4. No olvides que todas las palabras usadas en la sopa de letras están en singular.")
    print()
    print("5. Disfruta del juego que hemos preparado especialmente para ti.")
    print()
    print("¡ES HORA DE JUGAR!")
    print()
    
#La siguiente función permite evitar la sobreposición de las palabras entre sí
def PosiciónVacia(matriz, fila, col, longitudPalabra, direccion):
    if direccion == 'horizontal':
        return all(matriz[fila, col + i] == ' ' for i in range(longitudPalabra))    #Cada letra que se va agregando en una posición vacía
    elif direccion == 'vertical':
        return all(matriz[fila + i, col] == ' ' for i in range(longitudPalabra))
    elif direccion == 'diagonal':
        return all(matriz[fila + i, col + i] == ' ' for i in range(longitudPalabra))
    else:
        return False
    
#La siguiente función rellena la matriz con letras aleatorias en los espacios en blanco
#Recorre la matriz
def LetrasAzar(matriz):
    for i in range(matriz.shape[0]):                                                 #Representa las filas
        for j in range(matriz.shape[1]):                                             #Representa las columnas
            if matriz[i, j] == ' ':                                                  #Si se encuentra en blanco
                matriz[i, j] = random.choice('abcdefghijklmnopqrstuvwxyzñ').upper()  #Rellena con letras al azar
    return(matriz)

#La siguiente función ingresa las palabras a la sopa de letras

def RellenarLetras(palabras, filas, columnas):
    palabras = [entrada.upper() for entrada in palabras]   #Genera las palabras en mayúsculas
    matriz = np.full((filas, columnas), ' ', dtype=str)    #Genera una matriz vacía usando numpy

    for k in range(len(palabras)):
        num_intentos = 70                            # Este es el número de veces que se va a validar cada palabra en el caso en el que no se pueda ingresar en una posición específica
        for _ in range(num_intentos):
            direccion = random.choice(['horizontal', 'vertical', 'diagonal'])                         #Escoge una dirección al azar
            fila, col = np.random.randint(0, matriz.shape[0]), np.random.randint(0, matriz.shape[1])  #Ingresa a fila y columna el número de la posición aleatoria


#El siguiente código agrega las palabras según la posición que se haya escogido aleatoriamente según dos parámetros:
#Que la palabra al ingresarse no se vaya a salir del tamaño de la matriz Y con la función PosiciónVacia evualamos que efectivamente se ingrese en un espacio vacío
#El break es importante ya que permite que una vez se ingrese la palabra salga del bucle, con esto evitamos que la palabra se repita más veces dentro de la sopa de letras

            if (direccion == 'horizontal' and col + len(palabras[k]) <= matriz.shape[1]) or \
               (direccion == 'vertical' and fila + len(palabras[k]) <= matriz.shape[0]) or \
               (direccion == 'diagonal' and fila + len(palabras[k]) <= matriz.shape[0] and col + len(palabras[k]) <= matriz.shape[1]):
                if PosiciónVacia(matriz, fila, col, len(palabras[k]), direccion):
                    if direccion == 'horizontal':
                        matriz[fila, col:col+len(palabras[k])] = list(palabras[k])
                    elif direccion == 'vertical':
                        matriz[fila:fila+len(palabras[k]), col] = list(palabras[k])
                    elif direccion == 'diagonal':
                        for i in range(len(palabras[k])):
                            matriz[fila+i, col+i] = palabras[k][i]
                    break
        else:
            # Si no se encontró una posición adecuada después de todos los intentos, puedes manejar esto de la manera que prefieras
            print(f"La palabra {palabras[k]} NO se pudo colocar en la sopa de letras.")

    LetrasAzar(matriz)
    return matriz

def IngresarCoordenadas(matriz, coordenadaA, coordenadaB):
    
    x1, y1 = coordenadaA
    x2, y2 = coordenadaB

    # Verifica si las coordenadas están dentro de los límites de la matriz
    if not (0 <= x1 < len(matriz) and 0 <= y1 < len(matriz[0]) and 0 <= x2 < len(matriz) and 0 <= y2 < len(matriz[0])):
        print()
        print()
        print("Coordenadas fuera de los límites. Por favor, ingresa coordenadas válidas para la matriz.")
        return None

    palabra = ""

    # Para palabras en horizontal
    if x1 == x2:
        if y1 < y2:
            for j in range(y1, y2 + 1):
                palabra += matriz[x1][j]
        else:
            for j in range(y2, y1 + 1):
                palabra += matriz[x1][j]
        return palabra

    # Para palabras en vertical
    if y1 == y2:
        if x1 < x2:
            for i in range(x1, x2 + 1):
                palabra += matriz[i][y1]
        else:
            for i in range(x2, x1 + 1):
                palabra += matriz[i][y1]
        return palabra

    # Para palabras en diagonal
    if abs(x2 - x1) == abs(y2 - y1):
        if x2 > x1 and y2 > y1:
            for i in range(x2 - x1 + 1):
                palabra += matriz[x1 + i][y1 + i]
        elif x2 > x1 and y2 < y1:
            for i in range(x2 - x1 + 1):
                palabra += matriz[x1 + i][y1 - i]
        elif x2 < x1 and y2 > y1:
            for i in range(x1 - x2 + 1):
                palabra += matriz[x1 - i][y1 + i]
        else:
            for i in range(x1 - x2 + 1):
                palabra += matriz[x1 - i][y1 - i]
        return palabra

    return None

#Aqui creamos una funcion que nos permite jugar de nuevo una vez ya hayamos ganado el juego
def JugarDeNuevo():
    while True:
        print()
        respuesta = input("¿Te gustaría jugar de nuevo? (S/N): ")
        respuesta = respuesta.lower()
        if respuesta == "S" or respuesta == "s":
            return True
        elif respuesta == "N" or respuesta == "n":
            print()
            print()
            print("FIN DEL JUEGO, GRACIAS POR JUGAR.")
            return False
        else:
            print("Responde con 'S/s' ó 'N/n'")

#El siguiente código define la dificultad del juego. Entre más fácil será más pequeña la matriz y tendrá menos palabras. La dificultad está definida por el usuario

# Escoger nivel de dificultad
def JugarSopadeLetras():
    while True:
        dificultad = input("Ingresa la dificultad. Escriba '1' para dificultad Fácil, '2' para dificultad Medio y '3' para dificultad Difícil: ")

        if dificultad.isdigit() and dificultad in ['1', '2', '3']:
            dificultad = int(dificultad)
            break
        else:
            print("Por favor, ingresa un número válido (1, 2 ó 3).")
            print()

    if dificultad == 1:
        filas = 15
        columnas = 15
        cantidad = 7
    elif dificultad == 2:
        filas = 20
        columnas = 20
        cantidad = 10
    elif dificultad == 3:
        filas = 30
        columnas = 30
        cantidad = 15
    else:
        print("Por favor, selecciona una dificultad valida.")

    # Se crea una lista de palabras ingresadas que se utilizará más adelante
    #Se le da la opción al usuario de si quiere ingresar las palabras él mismo o prefiere que las genere el programa

    Palabras_ingresadas = []
    print()
    Tipo_palabras = input("¿Deseas ingresar tu mismo las palabras? S/N: ")
    Palabras = {}
    #Si la respuesta no está dentro de las opciones dadas se imprime un mensaje de respuesta no válida

    while Tipo_palabras not in ["S","s", "N", "n"]:
        print("Respuesta no válida. Por favor, ingresa 'S/s' o 'N/n'.")
        print()
        Tipo_palabras = input("¿Deseas ingresar tu mismo las palabras? S/N: ")

    #En este caso, cuando la opción sea palabras ingresadas:
    #El usuario ingresará las palabras que quiera (Teniendo en cuenta la dificultad será el número de palabras que se permitirá ingresar)
    #Las palabras ingresadas se meterán a la lista antes hecha "Palabras_ingresadas" y se pondrán en mayúscula

    if Tipo_palabras == "s" or Tipo_palabras == 'S':
        
        while len(Palabras_ingresadas) < cantidad:
            print()
            palabras = input("Ingresa una palabra: ")
            if palabras.isalpha():
                if len(palabras) < filas:
                    Palabras_ingresadas.append(palabras.upper())
                else:
                    print("Tu palabra excede el límite de letras establecido.")
                    print(f"Por favor, ingresa una palabra que tenga menos de {filas} letras")
            else:
                print("Por favor, NO ingreses números ni caracteres especiales.")

    #Si el usuario quiere que las palabras las genere el programa:
    #Se va a crear un diccionario con categorías definidas

    elif Tipo_palabras == "N" or Tipo_palabras == "n":
       Palabras = {

    "COLORES": ["AMARILLO", "ROJO", "VERDE", "AZUL", "NARANJA", "NEGRO", "ROSADO", "MORADO", "BLANCO", "DORADO", "PLATEADO", "GRIS", "TURQUESA", "MARRON", "CELESTE", "LIMA", "MAGENTA",
                "CIAN", "BEIGE", "AGUAMARINA", "VIOLETA"],

    "ANIMALES": ["DELFIN", "BALLENA", "TIBURON", "TORTUGA", "ELEFANTE", "JIRAFA", "LEON", "TIGRE", "OSO", "LOBO", "ZORRO", "CONEJO", "ARDILLA", "NUTRIA", "CASTOR", "CIERVO", "JABALI",
                 "PUMA", "LEOPARDO", "PANTERA", "COCODRILO", "LAGARTO", "IGUANA", "CAMALEON", "SERPIENTE", "VIBORA", "ARAÑA", "ESCORPION", "ABEJA", "AVISPA", "MOSQUITO", "MARIPOSA",
                 "POLILLA", "ESCARABAJO", "CUCARACHA", "MOSCA", "HORMIGA", "CIGARRA", "SURICATA"],

    "EMOCIONES": ["AMOR", "FELICIDAD", "TRISTEZA", "MIEDO", "ENOJO", "SORPRESA", "ASOMBRO", "VERGUENZA", "CONFUSION", "ORGULLO", "CULPA", "CELOS", "GRATITUD", "ESPERANZA", "DOLOR",
                  "EMPATIA", "COMPASION", "DESPRECIO", "ANSIEDAD", "ESTUPOR", "NOSTALGIA", "CULPA", "HOSTILIDAD", "EUFORIA", "INSEGURIDAD", "ADMIRACION", "IMPACIENCIA", "DESDEN",
                  "AVERSION", "ESTIMA", "CAUTELA", "ALIVIO", "ENTUSIASMO", "RESIGNACIÓN", "AGOBIO", "CURIOSIDAD"],

    "MEDIOS DE TRANSPORTE": ["COCHE", "AUTOBUS", "TREN", "METRO", "BICICLETA", "MOTO", "AVION", "BARCO", "TRANVIA", "CAMION", "HELICOPTERO", "TAXI", "PATINETA", "TRINEO", "AMBULANCIA",
                             "BARCA", "SUBMARINO", "TRACTOR", "CANOA"],

    "TECNOLOGÍAS": ["TABLETA", "LAPTOP", "SMARTWATCH", "TELEVISOR", "CONSOLA", "CELULAR", "TELEFONO", "DRON", "IMPRESORA", "CAMARA", "COMPUTADOR", "AUDIFONOS", "RADIO", "REALIDADVIRTUAL", "MICROFONO", "ESCANER"],
    
    "OBJETOS COTIDIANOS": ["LLAVE", "CARTERA", "GAFAS", "RELOJ", "BOLIGRAFO", "PAPEL", "CUADERNO", "BOTELLA", "MOCHILA", "SOMBRILLA", "ROPA", "CEPILLO", "JABON", "TOALLA", "PLATO", "TAZA",
                           "LAMPARA", "ESPEJO", "MAQUILLAJE", "CARGADOR", "ALMOHADA", "SILLA", "PAÑUELO", "LINTERNA", "LAPIZ", "ENCHUFE", "CONTROL", "CORTINA", "BOLSA", "TARJETA", "CINTA",
                           "SARTEN", "ESCOBA"],

    "COMIDAS": ["PIZZA", "PASTA", "SUSHI", "ENSALADA", "TACO", "POLLO", "SOPA", "FILETE", "CURRY", "PAELLA", "LASAÑA", "PASTEL", "PESCADO", "SANDWICH", "BURRITO", "RISOTTO",
                "CEVICHE", "EMPANADA", "CHURRASCO"],

    "PAÍSES": ["EEUU", "CHINA", "RUSIA", "INDIA", "BRASIL", "MEXICO", "CANADA", "FRANCIA", "ALEMANIA", "ITALIA", "JAPON", "AUSTRALIA", "ESPAÑA", "COREA", "SUDAFRICA", "NIGERIA", "ARGENTINA",
               "TURQUIA", "INDONESIA", "EGIPTO", "ISRAEL", "COLOMBIA", "PERU"],

    "ANIMES": ["NARUTO", "ONEPIECE", "DRAGONBALL", "ATTACKONTITAN", "DEATHNOTE", "MYHEROACADEMIA", "ONEPUNCHMAN", "TOKYOGHOUL", "DEMONSLAYER", "EVANGELION", "BLEACH", "BLACKCLOVER",
               "JUJUTSUKAISEN", "CODEGEASS", "HAIKYUU", "CHAINSAWMAN", "DRSTONE", "BEASTARS", "MONSTER", "LOVEISWAR", "POKEMON", "FIREFORCE", "BAKI"],

    "VIDEOJUEGOS": ["MARIOKART", "CHESS", "ZELDA", "MINECRAFT", "TETRIS", "GTAV", "FORTNITE", "OVERWATCH", "CALLOFDUTY", "LEAGUEOFLEGENDS", "RESIDENTEVIL", "HALO", "GODOFWAR", "ASSASSINSCREED", "DARKSOULS",
                    "GENSHINIMPACT", "COUNTERSTRIKE", "ROCKETLEAGUE", "APEXLEGENDS"],

    "MARCAS": ["COCACOLA", "APPLE", "GOOGLE", "MICROSOFT", "AMAZON", "SAMSUNG", "NIKE", "ADIDAS", "MCDONALDS", "TOYOTA", "BMW", "SONY", "FACEBOOK", "TWITTER", "INSTAGRAM", "WALMART",
               "PEPSI", "DISNEY", "VISA", "FORD", "GUCCI", "ROLEX"],

    "PELICULAS": ["TITANIC", "STARWARS", "JURASSICPARK", "HARRYPOTTER", "FORRESTGUMP", "AVATAR", "MATRIX", "GLADIADOR", "INTERESTELAR", "INDIANAJONES", "REGRESOALFUTURO", "SPIDERMAN",
                  "INCEPTION", "LALALAND", "TOYSTORY", "FROZEN", "AVENGERS"],

    "ALIMENTOS": ["MANZANA", "BANANO", "NARANJA", "UVA", "KIWI", "FRESA", "MANGO", "SANDIA", "PIÑA", "MELON", "PERA", "DURAZNO", "CEREZA", "PAPAYA", "CIRUELA", "HIGO", "MANDARINA", "GUAYABA",
                  "LECHUGA", "TOMATE", "ZANAHORIA", "BROCOLI", "COLIFLOR", "ESPINACA", "PEPINO", "PIMENTON", "CALABACIN", "CALABAZA", "CEBOLLA", "AJO", "PATATA", "BERENJENA", "CHAMPIÑON"],

    "ACCIONES": ["TRABAJO", "ESTUDIAR", "JUGAR", "CORRER", "CAMINAR", "BAILAR", "CANTAR", "DORMIR", "COMER", "BEBER", "REIR", "LLORAR", "SONAR", "PENSAR", "HABLAR", "ESCUCHAR", "VER",
                 "SENTIR", "TOCAR", "OLER", "GUSTAR", "DISFRUTAR", "VIAJAR", "CONDUCIR", "NADAR", "SURFEAR", "ESQUIAR", "MONTAR", "SALTAR", "CAER", "LEVANTAR", "EMPUJAR", "JALAR", "ABRIR",
                 "CERRAR", "EMPACAR", "ENVIAR", "RECIBIR", "REGALAR", "COMPRAR", "VENDER", "CAMBIAR", "BUSCAR", "ENCONTRAR", "PERDER", "GANAR", "COMPETIR", "AYUDAR", "APRENDER", "ENSENAR",
                 "CONOCER", "CREER", "DUDAR", "ESPERAR", "QUERER", "AMAR", "ODIAR", "OLVIDAR", "RECORDAR", "DESEAR", "NECESITAR", "PODER", "DEBER", "SER", "ESTAR", "IR", "VENIR", "QUEDAR",
                 "PARTIR", "LLEGAR", "SALIR", "VOLVER", "ANDAR", "PASEAR", "VISITAR", "CONOCER", "INVITAR", "ACEPTAR", "RECHAZAR", "PROBAR", "EXPERIMENTAR", "REALIZAR", "CREAR", "DIBUJAR",
                 "PINTAR", "ESCRIBIR", "LEER", "RESOLVER", "CELEBRAR", "ORGANIZAR", "PREPARAR", "COCINAR", "HORNEAR", "PICAR", "CORTAR", "MEZCLAR", "BATIR", "HERVIR", "FREIR", "ASAR",
                 "ALQUILAR", "COMPARTIR", "CUIDAR", "PROTEGER", "RESPETAR", "TRATAR", "ESFORZARSE", "DESCANSAR", "RELAJARSE", "MEDITAR", "RESPIRAR", "EXHALAR", "INHALAR", "SOPLAR", "SILBAR",
                 "SONREIR", "ABRAZAR", "BESAR", "ESTRECHAR", "ACARICIAR", "MIRAR", "OBSERVAR", "VIGILAR", "ANALIZAR", "PENSAR", "REFLEXIONAR", "IMAGINAR", "COMPRENDER", "ENTENDER", "ASIMILAR",
                 "DUDAR", "CUESTIONAR", "INVESTIGAR", "EXPLORAR", "DESCUBRIR", "ADMIRAR", "APRECIAR", "VALORAR", "DISFRUTAR", "APROVECHAR", "APLAUDIR", "ELOGIAR", "FELICITAR", "CRITICAR",
                 "REPROCHAR", "EXIGIR", "PEDIR", "SOLICITAR", "CONSEGUIR", "OBTENER", "GANAR", "SACRIFICAR", "RENUNCIAR", "DESECHAR", "RECHAZAR", "EVITAR", "PREVENIR", "SUPERAR", "VENCER",
                 "ESCAPAR", "HUIR", "ESCONDER", "OCULTAR", "MOSTRAR", "REVELAR", "EXPONER", "DEMOSTRAR", "EXPLICAR", "COMUNICAR", "TRANSMITIR", "INTERCAMBIAR", "DIALOGAR", "NEGOCIAR",
                 "RESOLVER", "CONFRONTAR", "ENFRENTAR", "ASUMIR", "ACEPTAR", "PERDONAR", "CONVENCER", "PERSUADIR"],

    "LUGARES": ["PARQUE", "PLAYA", "BOSQUE", "MONTAÑA", "LAGO", "RIO", "DESIERTO", "CAMPO", "GRANJA", "JARDIN", "PLAZA", "MERCADO", "BIBLIOTECA", "MUSEO", "TEATRO", "CINE", "CAFE",
                "RESTAURANTE", "BAR", "GIMNASIO", "PISCINA", "SPA", "HOSPITAL", "CLINICA", "FARMACIA", "ESCUELA", "UNIVERSIDAD", "OFICINA", "CASA", "APARTAMENTO", "IGLESIA", "AUDITORIO",
                "ESTACION", "AEROPUERTO"],

    "DEPORTES": ["FUTBOL", "BALONCESTO", "BEISBOL", "TENIS", "GOLF", "HOCKEY", "CRIQUET", "RUGBY", "ATLETISMO", "NATACION", "CICLISMO", "BOXEO", "SNOWBOARD", "SURF", "SKATEBOARDING",
                 "VOLEIBOL", "ESCALADA", "PESCA", "KARATE", "TAEKWONDO", "BOLOS", "BILLAR", "AJEDREZ", "PARKOUR"]

    }

    while True:
        categorias = list(Palabras.keys())
        if not categorias:
            break
        print()
        categoria_elegida = input(f"Ingresa una categoría: {categorias} ")   #Muestra todas las categorías y da la opción de escoger una

    #Creamos un if para asegurarnos de que la categoría ingresada exista en el diccionario

        if categoria_elegida in Palabras:
            valor = Palabras[categoria_elegida]
            palabras_validas = [palabra for palabra in valor if len(palabra) <= min(filas, columnas)]
            if not palabras_validas:
                continue

            valor = Palabras[categoria_elegida]
            Palabras_ingresadas = random.sample(valor, cantidad)

            categoria_seleccionada = categoria_elegida
            break  # Sale del bucle si la categoría es válida
        else:
            print()
            print("La categoría ingresada NO está en el diccionario. Por favor, asegurate de escribirlo correctamente.")

    # Imprime la matriz usando la función de rellenar letras, ya teniendo las palabras ingresadas
    resultado_sopa = RellenarLetras(Palabras_ingresadas, filas, columnas) # Función que da el resultado

    #Según el rango (Es decir el tamaño de la matriz), se añaden los números en las filas y columnas, simulando las coordenadas
    col_names = [str(i) for i in range(resultado_sopa.shape[1])]

    #Usando la biblioteca de pandas, se usa la función dataframe para mostrar la sopa de letras mucho más bonita
    matrizfinal = pd.DataFrame(resultado_sopa, columns=col_names)
    print()
    print()
    print(Palabras_ingresadas)
    print()
    print(matrizfinal)   #Imprime la matriz resultante

    cantidad_palabras = len(Palabras_ingresadas)

    while cantidad_palabras != 0:
        print()
        fila1 = input("Ingresa la coordenada de la Fila 1: ")
        col1 = input("Ingresa la coordenada de la Columna 1: ")
        fila2 = input("Ingresa la coordenada de la Fila 2: ")
        col2 = input("Ingresa la coordenada de la Columna 2: ")

        if not fila1.isdigit() or not col1.isdigit() or not fila2.isdigit() or not col2.isdigit():
            print()
            print()
            print("Sus coordenadas no son válidas. Por favor, ingresa coordenadas válidas.")
            print()
            print(matrizfinal)
            print()
            print("Te faltan las siguientes palabras:")
            print(f"{Palabras_ingresadas}")
            continue

        coordenada1 = (int(fila1), int(col1))
        coordenada2 = (int(fila2), int(col2))

        intento_palabra = IngresarCoordenadas(resultado_sopa, coordenada1, coordenada2)

        if intento_palabra is None:

            continue

        palabra_encontrada = False

        if intento_palabra in Palabras_ingresadas:
            palabra_encontrada = True
            Palabras_ingresadas.remove(intento_palabra)

            cantidad_palabras -= 1
            if cantidad_palabras == 0:
                print()
                print()
                print("¡FELICIDADES, HAS GANADO EL JUEGO!")
            else:
                print()
                print(f"Bien hecho, encontraste la palabra {intento_palabra}, te faltan {cantidad_palabras} por encontrar.")
                print()
                print(matrizfinal)
                print()
                print("Te faltan las siguientes palabras:")
                print(f"{Palabras_ingresadas}")
        else:
            print()
            print(f"La palabra {intento_palabra} NO hace parte de las palabras por buscar, por favor intenta con otras coordenadas")
            print()
            print(matrizfinal)
            print()
            print("Te faltan las siguientes palabras:")
            print(f"{Palabras_ingresadas}")
            
    if JugarDeNuevo():
        JugarSopadeLetras()
            
if __name__ == "__main__":
    Instrucciones()
    JugarSopadeLetras()