#Author Christopher Britten

        #imports here
import turtle
import time
import random

        # Step 2: Create Screen 

def save_score():
      global score, high
      if score > high:
            with open("snake.dat", "w") as file:
                 file.write(str(score))

def high_score():
      try:
            with open("snake.dat", "r") as file:
                  return int(file.read())
      except:
            return 0
      
DELAY = 0.1
segments = []

score = 0
high = high_score()

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=400,height=600)
win.tracer(0)

        #Snake Head Here

head = turtle.Turtle()
head.speed(0)
head.shape("circle") 
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"


#Here Food Is Added

food =turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100) # This Will Start Randomly On Screen 


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score} High Score: {high}", align ="center",font=("courier", 14, "normal"))
  #Move Section // Come Back To This ??? 

 #Moving with def 

def UpHere ():
 if head.direction != "down":
        head.direction = "up" 

def godown ():
        if head.direction != "up":
         head.direction = "down"

def LeftHere ():
        if head.direction != "right":
         head.direction = "left"

def RightMove ():
        if head.direction != "left":
                head.direction = "right" 

def move():
        # This Was Put In Reverse Order
        for i in range(len(segments) -1, 0, -1):
                x = segments[i - 1].xcor()
                y= segments[i - 1].ycor()
                segments[i].goto(x,y)
                # Trying to trigger a game over with this code below 
        if head.xcor() > 190 or head.xcor() < -190 or head.ycor() > 290 or head.ycor() < -290:
                        save_score()
                        print("Game Over")
                        time.sleep(2)
                        win.bye()
# FIrst part 
        if len(segments) > 0:
                segments[0].goto(head.xcor(), head.ycor())


        #moving Head 
        if head.direction == "up":
                y = head.ycor() # Cool here ... coor .. nice 
                head.sety(y+20)
        if head.direction == "down":
                y = head.ycor() # Again very cool here ... -----= === 
                head.sety(y-20)
        # X now 
        if head.direction == "left":
                x = head.xcor()
                head.setx(x-20)
        if head.direction == "right":
                x = head.xcor()
                head.setx(x+20)


        if head.distance(food) < 20:
              
              x = random.randint(-180, 180)
              y = random.randint(-280,280)
              food.goto(x,y)
              grow_snake()
              
              global score
              score += 10
              pen.clear()
              pen.write(f"Score: {score} High Score: {high}", align ="center",font=("courier", 14, "normal"))

             

def grow_snake():
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)
# Key Bind Here --- Imortant -- 
        
 #That will take an input from the device being targeted .... ( assuming this is how it works )

win.listen()
win.onkeypress(UpHere, "w")
win.onkeypress(godown, "s")
win.onkeypress(LeftHere, "a")
win.onkeypress(RightMove, "d")
# That Was Awesome 

grow_snake()
grow_snake()
grow_snake()
# Going to Have To loop This 

while True:
 win.update() 
 move()

 time.sleep(DELAY)