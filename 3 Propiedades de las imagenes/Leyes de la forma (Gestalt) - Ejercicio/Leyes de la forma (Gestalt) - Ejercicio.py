from turtle import *
import turtle
from random import randint

# Gestalt Principles for Visualization


# Proximity

speed(0)
penup()
goto(-150,150)

ubicacion1=[(-100,100), (-100,30), (-100,-60), (-100, -130)]
ubicacion2=[(-50,100), (-50,30), (-50,-60), (-50, -130)]
ubicacion3=[(0,100), (0,30), (0,-60), (0, -130)]
ubicacion4=[(50,100), (50,30), (50,-60), (50, -130)]
ubicacion5=[(100,100), (100,30), (100,-60), (100, -130)]

ubicaciones=[ubicacion1,ubicacion2,ubicacion3,ubicacion4,ubicacion5]
size= len(ubicaciones)

# Comienzo

#Título
penup()
turtle.penup()
goto(0,160)
turtle.pendown()
turtle.write("Gestalt Principle: Proximity", None, "center", "16pt bold")
penup()

#Círculos
for k in range(5):
  for i in range(4):
    goto(ubicaciones[k][i])
    for j in range(4):
        pendown()
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.right(90)
        turtle.end_fill()
        penup()
        forward(10)
        

turtle.reset()


# Similarity

speed(0)
penup()
goto(-150,150)

colores=[(223,102,37), (111,52,109), (25,108,121), (43,170,132)]
ubicacion1=[(-100,100), (-100,30), (-100,-60), (-100, -130)]
ubicacion2=[(-50,100), (-50,30), (-50,-60), (-50, -130)]
ubicacion3=[(0,100), (0,30), (0,-60), (0, -130)]
ubicacion4=[(50,100), (50,30), (50,-60), (50, -130)]
ubicacion5=[(100,100), (100,30), (100,-60), (100, -130)]

ubicaciones=[ubicacion1,ubicacion2,ubicacion3,ubicacion4,ubicacion5]

# Comienzo

#Título
penup()
turtle.penup()
goto(0,160)
turtle.pendown()
turtle.write("Gestalt Principle: Similarity", None, "center", "16pt bold")
penup()

#Círculos
for k in range(5):
  for i in range(4):
    goto(ubicaciones[k][i])
    for j in range(4):
        pendown()
        turtle.fillcolor(colores[i])
        turtle.begin_fill()
        turtle.circle(10)
        turtle.right(90)
        turtle.end_fill()
        penup()
        forward(10)
        
turtle.reset()
  
#Enclosure

speed(0)
penup()
goto(-150,150)

colores=[(223,102,37), (111,52,109), (25,108,121), (43,170,132)]

ubicacion1=[(-100,100), (-100,30), (-100,-60), (-100, -130)]
ubicacion2=[(-50,100), (-50,30), (-50,-60), (-50, -130)]
ubicacion3=[(0,100), (0,30), (0,-60), (0, -130)]
ubicacion4=[(50,100), (50,30), (50,-60), (50, -130)]
ubicacion5=[(100,100), (100,30), (100,-60), (100, -130)]

ubicaciones=[ubicacion1,ubicacion2,ubicacion3,ubicacion4,ubicacion5]

# Comienzo

#Título
penup()
turtle.penup()
goto(0,160)
turtle.pendown()
turtle.write("Gestalt Principle: Enclosure", None, "center", "16pt bold")
penup()

#Marcos

#Marco 1
goto(-140,130)
pendown()
turtle.fillcolor((30,50,61))
turtle.begin_fill()
for i in range(2):
  forward(270)
  right(90)
  forward(70)
  right(90)
turtle.end_fill()
turtle.penup()

#Marco 2
goto(-140,-100)
pendown()
turtle.fillcolor((253,233,98))
turtle.begin_fill()
for i in range(2):
  forward(270)
  right(90)
  forward(70)
  right(90)
turtle.end_fill()
turtle.penup()



#Círculos
for k in range(5):
  for i in range(4):
    goto(ubicaciones[k][i])
    for j in range(4):
        pendown()
        turtle.fillcolor(colores[i])
        turtle.begin_fill()
        turtle.circle(10)
        turtle.right(90)
        turtle.end_fill()
        penup()
        forward(10)

turtle.reset()

# Symmetry
speed(0)

#Título
penup()
turtle.penup()
goto(0,160)
turtle.pendown()
turtle.write("Gestalt Principle: Symmetry", None, "center", "16pt bold")
penup()

ubicacion1=[(-50,60), (-50,40), (-50,20), (-50,0), (-50,-20), (-50,-40)]
ubicacion2=[(-70,50), (-70,30), (-70,10), (-70,-10), (-70,-30)]
ubicacion3=[(-90,40), (-90,20),(-90,0),(-90,-20)]
ubicacion4=[(-110,30), (-110,10),(-110,-10)]
ubicacion5=[(-130,20),(-130,0)]
ubicacion6=[(-150,10)]
ubicaciones=[ubicacion1, ubicacion2, ubicacion3, ubicacion4, ubicacion5, ubicacion6]
n=len(ubicaciones)

paletacolores=[(7,39,76), (0,83,123),(0,130,147),(0,175,144),(130,217,124),(249,248,113)]


penup()
goto(-50,60)
for k in range(n):
  for j in range(n-k):
    goto(ubicaciones[k][j])
    pendown()
    turtle.fillcolor(paletacolores[k])
    turtle.begin_fill()
    for i in range(4):
      forward(20)
      right(90)
    turtle.end_fill()
  penup()
  
ubicacion7=[(50,60), (50,40), (50,20), (50,0), (50,-20), (50,-40)]
ubicacion8=[(70,50), (70,30), (70,10), (70,-10), (70,-30)]
ubicacion9=[(90,40), (90,20),(90,0),(90,-20)]
ubicacion10=[(110,30), (110,10),(110,-10)]
ubicacion11=[(130,20),(130,0)]
ubicacion12=[(150,10)]
ubicaciones2=[ubicacion7, ubicacion8, ubicacion9, ubicacion10, ubicacion11, ubicacion12]
  
goto(50,60)
for k in range(n):
  for j in range(n-k):
    goto(ubicaciones2[k][j])
    pendown()
    turtle.fillcolor(paletacolores[k])
    turtle.begin_fill()
    for i in range(4):
      forward(20)
      right(90)
    turtle.end_fill()
  penup()
  
turtle.reset()

#Closure
speed(0)
#Título
penup()
turtle.penup()
goto(0,160)
turtle.pendown()
turtle.write("Gestalt Principle: Closure", None, "center", "16pt bold")
penup()

paletadecolores=[(243,245,242), (184,155,156), (180,64,48), (239,126,49), (49,39,72)]
for j in range(5):
  goto((-20-(j*25)),j*15)
  pendown()
  pencolor(paletadecolores[j])
  for i in range(6):
    pendown()
    left(30)
    forward(15+(j*10))
    penup()
    forward(10+(j*10))
    pendown()
    forward(15+(j*10))
    right(90)
  penup()
  
turtle.reset()

speed(0)
#Closure

#Título
penup()
turtle.penup()
goto(0,160)
turtle.pendown()
turtle.write("Gestalt Principle: Continuity", None, "center", "16pt bold")
penup()

goto(-100, -50)
for i in range(8):
  pendown()
  turtle.fillcolor((222,181,83))
  turtle.begin_fill()
  turtle.circle(5)
  turtle.end_fill()
  right(90)
  penup()
  forward(15)
  left(90)
  forward(10)

goto(-20,-140)
for i in range(17):
  pendown()
  turtle.fillcolor((222,181,83))
  turtle.begin_fill()
  turtle.circle(5)
  turtle.end_fill()
  penup()
  forward(10)
  left(90)
  forward(15)
  right(90)
  turtle.end_fill()

turtle.reset()


#Closure

speed(0)
#Título
penup()
turtle.penup()
goto(0,160)
turtle.pendown()
turtle.write("Gestalt Principle: Connection", None, "center", "16pt bold")
penup()


colores=[(222,181,83), (60,153,64), (186,94,35), (33,42,36)]
direcciones=[(-150,100), (-150,30), (-150, -100), (-150,-170)]
for k in range(4):
  goto(direcciones[k])
  pendown()
  for j in range(4):
    turtle.fillcolor(colores[k])
    turtle.begin_fill()
    for i in range(4):
      left(45)
      forward(40)
      right(135)
    turtle.end_fill()
    penup()
    forward(55)
    pendown()
    forward(20)
  penup()