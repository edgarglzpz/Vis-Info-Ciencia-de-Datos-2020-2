from turtle import *
import turtle
from random import randint
speed(1000)
penup()
turtle.penup()
goto(0,160)
turtle.pendown()
turtle.write("Crecimiento de los estados en México", None, "center", "16pt bold")
penup()
goto(0,-150)
turtle.write("De 1940 a 2010", None, "center", "16pt bold") 
penup()
# Etiquetas
# Jalisco
goto(-40,-80)
pendown()
turtle.color(46, 59, 71)
forward(20)
penup()
goto(-15, -80)
turtle.write("Jalisco", "16pt bold")
# Veracruz
goto(-40,-90)
pendown()
turtle.color(70, 166, 160)
forward(20)
penup()
goto(-15, -90)
turtle.write("Veracruz", "16pt bold")
# Estado de México
goto(-40,-100)
pendown()
turtle.color(165, 185, 153)
forward(20)
penup()
goto(-15, -100)
turtle.write("Estado de México", "16pt bold")
# Ciudad de México
goto(-40,-110)
pendown()
turtle.color(230, 204, 22)
forward(20)
penup()
goto(-15, -110)
turtle.write("Ciudad de México", "16pt bold")
# Puebla
goto(-40,-120)
pendown()
turtle.color(251, 125, 6)
forward(20)
penup()
goto(-15, -120)
turtle.write("Puebla", "16pt bold")

goto(100, 138)
turtle.color(0,0,0)
pendown()
turtle.write("Población en millones")
penup()

goto(-140, 140)
turtle.color(0,0,0)
Poblacion=['0','1.5','3','4.5','6','7.5','9','10.5','12','13.5','15','16']
for step in range(12):
  write(Poblacion[step], align='center')
  right(90)
  for num in range(10):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(200)
  left(90)
  forward(20)


ada = Turtle()
ada.color(46, 59, 71)
ada.shape('turtle')

ada.penup()
ada.goto(-160, 120)
ada.pendown()

for turn in range(10):
  ada.right(36)

bob = Turtle()
bob.color(70, 166, 160)
bob.shape('turtle')

bob.penup()
bob.goto(-160, 80)
bob.pendown()

for turn in range(72):
  bob.left(5)

ivy = Turtle()
ivy.shape('turtle')
ivy.color(165, 185, 153)

ivy.penup()
ivy.goto(-160, 40)
ivy.pendown()

for turn in range(60):
  ivy.right(6)

jim = Turtle()
jim.shape('turtle')
jim.color(230, 204, 22)

jim.penup()
jim.goto(-160, 0)
jim.pendown()

for turn in range(30):
  jim.left(12)

effy = Turtle()
effy.shape('turtle')
effy.color(251, 125, 6)

effy.penup()
effy.goto(-160, -40)
effy.pendown()

for turn in range(30):
  effy.left(12)
 
 
Jalisco=[1.950939955, 3.098130284, 5.530641644, 8.510929428, 12.26686913, 15.51736222, 17.92194359, 19.07737287, 20.57956085, 22.67009831]
Veracruz=[2.653042076, 4.123035649,6.524756611, 10.32299469, 15.81419829, 18.74990007, 20.52790939, 21.12741061, 21.83024967, 23.69171368]
Mexico=[1, 1.861226595, 3.62576512, 10.38503302, 23.41629398, 31.27965054, 37.88816214, 42.73835545, 45.91940949, 50]
CDMX=[3.135685769, 7.651257022, 14.00922991, 21.00583464, 27.84047196, 25.76122943, 26.64576537, 27.05171247, 27.4557212, 27.91032663]
Puebla=[1.51894535, 2.675715768, 3.891150697, 5.75753573, 8.689395693, 11.40805939, 13.14827573, 14.72803344, 15.79831763, 17.18380175]

for i in range(10):
  ada.forward(Jalisco[i])
  bob.forward(Veracruz[i])
  ivy.forward(Mexico[i])
  jim.forward(CDMX[i])
  effy.forward(Puebla[i])

#Poblacion final al 2010
#Jalisco
penup()  
goto(110, 120)
pendown()
write('7,350,682')

#Veracruz
penup()  
goto(110, 80)
pendown()
write('7,643,194')

#Estado de México
penup()  
goto(110, 40)
pendown()
write('15,175,862')

#Ciudad de México
penup()  
goto(110, 0)
pendown()
write('8,851,080')

#Puebla
penup()  
goto(110, -40)
pendown()
write('5,779,829')

penup()
goto(100, -80)
pendown()
write('Población')
penup()
goto(100, -90)
pendown()
write('hasta el 2010')
penup()
goto(100,-120)