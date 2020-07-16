from turtle import *
import turtle

speed(0)

# Título
penup()
turtle.penup()
goto(0,180)
turtle.pendown()
turtle.write("Population Pyramid of México in 2020", None, "center", "14pt bold")
penup()

# Datos
Edades= ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','100+']
Hombres= [5604781,5731706,5692822,5695013,5505161,5384130,4748412,4343789,4029738,3782769,3236044,2742491,2169271,1657202,1125991,774478,456066,248866,107034,30998,4724]
Mujeres= [5353961,5478805,5448048,5514580,5434658,5411644,5041468,4746361,4502226,4233025,3688873,3090563,2500183,1938297,1340716,947528,602438,361118,168098,50439,8238]
TotalPoblacion = sum(Hombres) + sum(Mujeres)
PorcentajeH = []
PorcentajeM = []
for i in range(len(Hombres)):
    PorcentajeH.append(Hombres[i]/TotalPoblacion)
for i in range(len(Mujeres)):
    PorcentajeM.append(Mujeres[i]/TotalPoblacion)


#Eje x
penup()
goto(-140,-160)
pendown()
forward(300)
penup()
goto(-140,-160)

#Intervalos eje x
for i in range(10):
    forward(30)
    right(90)
    pendown()
    forward(15)
    left(180)
    forward(15)
    right(90)
    
#Etiquetas en eje x
Etiquetasx = ['10%', '8%', '6%', '4%', '2%', '0%', '2%', '4%', '6%', '8%', '10%']
penup()
for i in range(len(Etiquetasx)):
  goto(-140+(29*i),-185)
  write(Etiquetasx[i], move= True, align = "left")
  penup()


#Eje y
penup()
goto(-140,-160)
left(90)
pendown()
forward(315)
penup()
goto(-140,-160)
pendown()

#Intervalos eje y
for i in range(21):
  forward(15)
  left(90)
  forward(15)
  right(180)
  forward(15)
  left(90)

#Etiquetas en eje y
penup()
goto(-190,-148)
for i in range(len(Edades)):
  write(Edades[i])
  penup()
  forward(15)
  pendown()
  
# Label Male/Female
penup()
goto(-90,160)
pendown()
write("Male", None, "center", "12pt bold")
penup()
goto(90,160)
write("Female", None, "center", "12pt bold")
penup()

# Gráfica

# Definimos una función para que nos de el ancho de las barras y obtenemos los valores
def anchograficas(x):
    newx = x*100
    intervalo = newx * 15
    return intervalo

valanchoM = []
for i in range(len(PorcentajeM)):
    valanchoM.append(anchograficas(PorcentajeM[i]))
    
valanchoH = []
for i in range(len(PorcentajeH)):
    valanchoH.append(anchograficas(PorcentajeH[i]))

# Línea que parte gráfica de barras

penup()
goto(10,-160)
pendown()
forward(300)

# Vamos al origen

penup()
goto(10,-160)
right(90)
pendown()

# Barras para mujeres

for i in range(len(valanchoM)):
  turtle.fillcolor("#EE7989")
  turtle.begin_fill()
  forward(valanchoM[i])
  left(90)
  forward(15)
  left(90)
  forward(valanchoM[i])
  right(180)
  turtle.end_fill()

# Cantidades para mujeres

PorcentajeM2=[]
for i in range(len(PorcentajeM)):
  PorcentajeM2.append(round(PorcentajeM[i]*100,1))
  
penup()
goto(80, -158)
pendown()
turtle.color("#000000")
for i in range(len(PorcentajeM2)):
  write(str(PorcentajeM2[i])+"%")
  penup()
  left(90)
  forward(15)
  right(90)


# Volvemos al origen

penup()
goto(10,-160)
right(180)
pendown()

# Barras para hombres

for i in range(len(valanchoH)):
  turtle.fillcolor("#4682B4")
  turtle.begin_fill()
  forward(valanchoH[i])
  right(90)
  forward(15)
  right(90)
  forward(valanchoH[i])
  left(180)
  turtle.end_fill()
  
# Cantidades para hombres

PorcentajeH2=[]
for i in range(len(PorcentajeH)):
  PorcentajeH2.append(round(PorcentajeH[i]*100,1))
  
penup()
goto(-85, -158)
pendown()
turtle.color("#000000")
for i in range(len(PorcentajeH2)):
  write(str(PorcentajeH2[i])+"%")
  penup()
  right(90)
  forward(15)
  left(90)

# Cifra a la actualidad

penup()
goto(0,-200)
pendown()
write("Population: 128,932,753", None, "center", "12pt bold")
penup()
goto(10,-160)
right(180)
pendown()
forward(70)
left(180)
forward(140)
penup()
goto(-160,160)