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

#Moving with def 

def UpHere ():
    if head.direction != "down":
        head.direction = "up" 

def godown ():
    if head.direction != "up":
        head.direction = "down"
    
def LeftHere ():
    if head.direction != "right":
        head.direction = "leaft"

def RightMove ():
        if head.direction != "left":
             head.direction = "right" 

def move():
        if head.direction == "up";
                y = head.ycor() # Cool here ... coor .. nice 
                head.sety(y+20)
        if head.direction == "down":
         y = head.ycor # Again very cool here ... -----= === 
        head.sety(y-20)
        # X now 
        if head.direction == "left":
             x = head.xcor()
             head.setx(x-20)
        if head.direction == "right":
             x = head.xcor()
             head.setx(x+20)

    # Key Bind Here --- Imortant -- 

win.listen()
#That will take an input from the device being targeted .... ( assuming this is how it works )
win.onkeypress(UpHere, "w")
win.onkeypress(godown, "s")
win.onkeypress(LeftHere, "a")
win.onkeypress(RightMove, "d")
# That Was Awesome 


# Going to Have To loop This 

while True:
     win.update()
     move()
     time.sleep(0,1)