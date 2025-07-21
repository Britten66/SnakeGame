#Author Christopher Britten

#imports here
import turtle
import time

# Step 2: Create Screen 
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600,height=600)
win.tracer(0)

#Snake Head Here

head = turtle.Turtle()
head.speed(0)
head.shape(" # Will Pick A Shape Later ") 
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Move Section // Come Back To This ??? 