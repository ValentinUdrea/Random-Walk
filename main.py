import turtle as t
import random
count = 0
tim = t.Turtle()
colors = ["medium aquamarine","CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]


directions = [0,90,180,270]



for i in range(200):
    tim.forward(30)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))

