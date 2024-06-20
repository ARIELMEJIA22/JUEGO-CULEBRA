import turtle                           
import time                             
import random                           

posponer = 0.1
puntaje = 0
maxPuntaje = 0

#Configuración
window = turtle.Screen()                
window.title('Snake')                   
window.bgcolor('#353535')               
window.setup(width=600,height=600)      
window.tracer(0)                        

#Cabeza de la serpiente
cabeza = turtle.Turtle()                
cabeza.speed(0)                         
cabeza.shape('square')                  
cabeza.color('#75C46D')                 
cabeza.penup()                          
cabeza.goto(0,0)                       
cabeza.direction = 'stop'              

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('#D12D2D')
comida.penup()
comida.goto(0,100)

#Texto para el puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('Puntaje:0     Máximo puntaje: 0', align='center', font=('Courier', 20, 'normal'))

#Cuerpo de la serpiende
cuerpo = []                             
colores = [(109,160,104),(104,142,160)]

#Funciones

def printText():

    global  maxPuntaje
    if puntaje>maxPuntaje:
        maxPuntaje = puntaje
    texto.clear()
    texto.write(f'Puntaje:{puntaje}     Máximo puntaje: {maxPuntaje}', align='center', font=('Courier', 20, 'normal'))

#Definir cada movimiento
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def izquierda():
    cabeza.direction = 'left'
def derecha():
    cabeza.direction = 'right'

#Ejecuta el movimiento
def movimiento():
    if cabeza.direction == 'up':       
        y =  cabeza.ycor()             
        cabeza.sety(y + 20)             

    elif cabeza.direction == 'down':
        y =  cabeza.ycor()              
        cabeza.sety(y - 20)

    elif cabeza.direction == 'left':
        x =  cabeza.xcor()              
        cabeza.setx(x - 20)

    elif cabeza.direction == 'right':
        x =  cabeza.xcor()             
        cabeza.setx(x + 20)

#Creacion del cuerpo
def crearSegmento():
    global puntaje
    segmento = turtle.Turtle()
    turtle.colormode(255)
    segmento.speed(0)
    segmento.shape('square')
    segmento.color(random.choice(colores))
    segmento.penup()
    cuerpo.append(segmento)
    puntaje += 1
    printText()

#Colisión con la comida
def colisionComida():
    if cabeza.distance(comida)<20:     
        x = random.randint(-280,280)
        y = random.randint(-280, 280)
        comida.goto(x,y)               
        crearSegmento()

#Mover el cuerpo
def movCuerpo():
    totalSeg = len(cuerpo)

    #Cada elemento sigue al anterior
    #Exepto el primero
    for segmento in range(totalSeg-1,0,-1):     
        x = cuerpo[segmento-1].xcor()           
        y = cuerpo[segmento-1].ycor()
        cuerpo[segmento].goto(x,y)              

    if totalSeg >0:                            
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x,y)

#Colisión con el borde
def borde():

    global  puntaje
    if cabeza.xcor()<-280 or cabeza.xcor()>280 or cabeza.ycor()<-280 or cabeza.ycor()>280:
        time.sleep(0.5)
        cabeza.goto(0,0)
        cabeza.direction = 'stop'
        for segmento in cuerpo:         
            segmento.goto(1000,1000)
        cuerpo.clear()                 
        puntaje = 0
        printText()

def mordida():

    global puntaje
    for segmento in cuerpo:
        if cabeza.distance(segmento) < 20:
            time.sleep(0.5)
            cabeza.goto(0, 0)
            cabeza.direction = 'stop'
            for segmento in cuerpo:  
                segmento.goto(1000, 1000)
            cuerpo.clear()  
            puntaje = 0
            printText()

#Conexion con teclado
window.listen()                         
window.onkeypress(arriba,'Up')          
window.onkeypress(abajo,'Down')
window.onkeypress(izquierda,'Left')
window.onkeypress(derecha,'Right')

#Ciclo permanente
while True:
    window.update()                     

    borde()
    colisionComida()                 
    mordida()
    movCuerpo()                         
    movimiento()                       

    time.sleep(posponer)                
