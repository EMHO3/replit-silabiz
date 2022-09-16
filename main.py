#DEFINIENDO COLORES
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#LIBRERIAS NECESARIAS PARA RANDOM Y TIMESLEEP
import random #importamos la librería random
import time

iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.
jugador_turnos = []

#Mensaje de bienvenida
print("Estas por empezar una divertida Trivia")
time.sleep(1)
print("Pondremos a prueba tus conocimientos en tema en Star Wars!")
time.sleep(1)

#Preguntamos el nombre al usuario
nombre=input("Por favor ingresa tu nombre: ")
time.sleep(1)

#Instrucciones
print(BLUE+"Hola", nombre,"debes escribir la letra de la alternativa correcta y dar enter:"+RESET)
print(BLUE+"Por cada pregunta correcta ganarás un numero aleatorio entre 5 y 10, mientras que si respondes de forma incorrecta se te restarán un numero aleatorio entre 1 y 5")
time.sleep(1)

#va a aparecer el número de veces que juguemos la trivia
while iniciar_trivia==True:
  #inicializamos en cero las variables que contaran la cantidad de preguntas correctas e incorrectas
  correcta=0
  incorrecta=0
  
  #Para implementar puntajes, crearemos una nueva variable   llamada "puntaje", la que inicpherializamos en 0.
  puntaje=random.randint(0,10) #Número aleatorio de 0 a 10.
  
  time.sleep(1)
  intentos+=1
  print("\nIntento número: ",intentos)
  input("Presione enter para continuar")
  print(GREEN+"Comenzarás con:",puntaje,"puntos"+RESET)
  
  #Creamos un ciclo para mostrar una carga inicial de 5 segundos
  for z in range(5,0,-1):
    print(z)
    time.sleep(1)
    
  #Pregunta 1
  print(RED+"\n1) ¿En qué año se estreno Star Wars Episodio I "+RESET)
  lista_a=[MAGENTA+"a) 1960","b) 1970","c) 1980","d) 1990"+RESET]
  
  for element in lista_a:
    print(element)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1=input(YELLOW+"\nTu respuesta:"+RESET).lower()
  
  #vamos a aplicar un ciclo de validación
  while respuesta_1 not in ("a","b","c","d"):
    respuesta_1=input("Debes responder a,b,c,d. Ingresa nuevamente tu respuesta: ").lower()
  
  #Utilizamos la condicional para validar la respuesta
  if respuesta_1=="c":
    cantidad_random = random.randint(5,10)
    puntaje+=cantidad_random
    correcta+=1
    print("Muy bien",nombre,"! ganaste",cantidad_random,"puntos y tu nu nuevo puntaje es:", puntaje)
  else:
    cantidad_random =random.randint(1,5)
    puntaje-=cantidad_random
    incorrecta+=1
    print("Incorrecto",nombre," :/ perdiste ", cantidad_random," puntos y tu nueuvo puntaje es:", puntaje)
  time.sleep(1)
  #Pregunta 2
  print(RED+"\n2) ¿Cual es el veradero nombre de Darth Vader?"+RESET)
  listab=[MAGENTA+"a)El cacas","b)Anakin Skywalker","c)Obi Wan","d)Sirius Black"+RESET]
  for element in listab:
    print(element)
  respuesta_2=input(YELLOW+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_2 not in ("a","b","c","d"):
    respuesta_2=input("Debes responder a,b,c,d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_2=="b":
    cantidad_random = random.randint(5,10)
    puntaje+=cantidad_random
    correcta+=1
    print("Muy bien",nombre,"! ganaste",cantidad_random,"puntos y tu nu nuevo puntaje es:", puntaje)
  else:
    cantidad_random =random.randint(1,5)
    puntaje-=cantidad_random
    incorrecta+=1
    print("Incorrecto",nombre," :/ perdiste ", cantidad_random," puntos y tu nueuvo puntaje es:", puntaje)
  time.sleep(1)
  
  #Pregunta 3
  print(RED+"\n3) ¿De los personajes listados quien es el más poderoso?"+RESET)
  listac=[MAGENTA+"a)C3PO","b)Darth Maul","c)Jar Jar","d)Yoda"+RESET]
  for element in listac:
    print(element)
  respuesta_3=input(YELLOW+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_3 not in ("a","b","c","d"):
    respuesta_3=input("Debes responder a,b,c,d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_3=="d":
    cantidad_random = random.randint(5,10)
    puntaje+=cantidad_random
    correcta+=1
    print("Muy bien",nombre,"! ganaste",cantidad_random,"puntos y tu nu nuevo puntaje es:", puntaje)
  else:
    cantidad_random =random.randint(1,5)
    puntaje-=cantidad_random
    incorrecta+=1
    print("Incorrecto",nombre," :/ perdiste ", cantidad_random," puntos y tu nuevo puntaje es:", puntaje)
  time.sleep(1)

  #Pregunta 4
  print(RED+"\n4) ¿Quien es la verdader madre de la Princesa Leia?"+RESET)
  listad=[MAGENTA+"a)Padme Amidala","b)Obina wan","c)Khalessy","d)Java the Hut"+RESET]
  for element in listad:
    print(element)
  
  respuesta_4=input(YELLOW+"\nTu respuesta:"+RESET).lower()
  
  while respuesta_4 not in ("a","b","c","d"):
    respuesta_4=input("Debes responder a,b,c,d. Ingresa nuevamente tu respuesta: ").lower()
  
  if respuesta_4=="a":
    cantidad_random = random.randint(5,10)
    puntaje+=cantidad_random
    correcta+=1
    print("Muy bien",nombre,"! ganaste",cantidad_random,"puntos y tu nu nuevo puntaje es:", puntaje)
  else:
    cantidad_random =random.randint(1,5)
    puntaje-=cantidad_random
    incorrecta+=1
    print("Incorrecto",nombre," :/ perdiste ", cantidad_random," puntos y tu nuevo puntaje es:", puntaje)
  time.sleep(1)
  
  #Ruleta de puntaje final
  print(BLUE+"\nJugaremos la ruleta de puntaje final")
  vueltas_ruleta=int(input("\n¿Cuántas veces quieres girar la ruleta? \n"+RESET))
  resultado_ruleta = random.randint(1,10)
  time.sleep(1)
  print("Girando...")
  time.sleep(3)
  print("Intento N° 1, resultado: ",resultado_ruleta)
  girar_ruleta = input("Introduci Si, en caso desees seguir girando la ruleta o cualquier teclar para dejar de girar: ").lower() 
  x=1
  while girar_ruleta == 'si' :
    x+=1
    print('valorde x: ', x)
    resultado_ruleta = random.randint(1,10)
    time.sleep(1)
    print("Girando...")
    time.sleep(3)
    print("Intento #",x+1," resultado: ",resultado_ruleta)
    girar_ruleta = input("Introduci Si, en caso desees seguir girando la ruleta o cualquier teclar para dejar de girar: ").lower()
    if x == vueltas_ruleta :
      girar_ruleta = 'no'
  time.sleep(1) 
    
  #Agregamos un mensaje al final de nuestra trivia donde mostraremos el puntaje total obtenido.
  print("\nCantidad de respuestas correctas: ",correcta)
  time.sleep(1)
  print("Cantidad de respuestas incorrectas: ",incorrecta)
  time.sleep(1)
  
  print(GREEN+"\nGracias",nombre,"por jugar mi trivia, alcanzaste", puntaje+resultado_ruleta,"puntos."+RESET)
  
  jugador_turnos.append(puntaje)

  #si deseamos seguir jugando aquí se decide
  print(MAGENTA+"\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()

  if repetir_trivia != "si":  # != significa "contrario"
   print(YELLOW+"\nSecuencia de puntaje por cada turno: ",jugador_turnos)
   print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
