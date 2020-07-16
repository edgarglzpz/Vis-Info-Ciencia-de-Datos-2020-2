
import turtle
from turtle import *

# Construye una segunda forma que utilice los colores secundarios.

speed(100)
shape('turtle')
turtle.penup()
turtle.goto(0,60)
turtle.pendown()

#Tallo
turtle.color('green')
turtle.right(90)
turtle.forward(350)
turtle.right(180)

#Petalo
turtle.forward(100)
turtle.color(0,0,0)
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(100,70)
turtle.left(110)
turtle.circle(100,70)
turtle.end_fill()
turtle.right(-80)
#Tallo
turtle.color('green')
turtle.left(30)
turtle.forward(200)


#Petalos
turtle.color(0,0,0)
color = ['yellow', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta', 'yellow', 'cyan', 'magenta']
for i in range(12):
  turtle.fillcolor(color[i])
  turtle.begin_fill()
  turtle.circle(100,70)
  turtle.left(110)
  turtle.circle(100,70)
  turtle.end_fill()
  turtle.right(-80)

