

#  _____  ______          _____       __  __ ______ _ 
# |  __ \|  ____|   /\   |  __ \     |  \/  |  ____| |
# | |__) | |__     /  \  | |  | |    | \  / | |__  | |
# |  _  /|  __|   / /\ \ | |  | |    | |\/| |  __| | |
# | | \ \| |____ / ____ \| |__| |    | |  | | |____|_|
# |_|  \_\______/_/    \_\_____/     |_|  |_|______(_)


# First, fix alternation so you can start seeing the "X" and "O" markers.
# Look for my comments in the draw_current_shape function.

# Second, once you see the "X" markers being drawn, you'll note that they are weird.
# Repair the function called x_shape.
# This function will start ou with Tina being located directly in the center of the cell.
# That is the correct "initial location", and if the x_shape function wants her to start in
# a different location to start drawing the "X" shape, the function itself should do that
# initial movement by using the appropriate "relative motion" actions.
# The Cheat Sheet now has a section on "relative motion" so refer to that if necessary.





import turtle
tina = turtle.Turtle()
tina.pensize(5)
tina.shape("turtle")
tina.fillcolor("black")
tina.color("red")
screen = turtle.Screen()
tina.speed(10)

def draw_gameboard():
  tina.penup()
  tina.goto(-180, 60)
  tina.pendown()
  tina.forward(360)
  tina.penup()
  tina.goto(-180, -60)
  tina.pendown()
  tina.forward(360)
  tina.penup()
  tina.goto(-60, -180)
  tina.left(90)
  tina.pendown()
  tina.forward(360)
  tina.penup()
  tina.goto(60, -180)
  tina.pendown()
  tina.forward(360)


print("i have created a tick tack toe board. click on the screen then press o for upper right, k for middle right, m for bottom right, then the keys to the left of them for the middle colum..... pick someone to be x and someone to be o")


# WHOA!  Be careful!
# This function called "circle_shape" is what we call "lost code".
# You probably used this function (i.e. "launched" it somewhere else in the code) 
# in some previous version.
# But now, this program never launches this function.
# Probably this happened due to the redesign in which we now have a
# function to draw X and a function to draw O.
# This function "circle_shape" is no longer being used.
# You should DELETE any "lost function" to keep yourself from getting confused.
def circle_shape():
  tina.pencolor('black')
  tina.dot(50)
  
  

tina.penup()


def x_shape():
  # REPAIR THE "X"
  tina.color("black")
  tina.pendown()
  tina.left(90)
  tina.forward(25)   
  tina.pendown()
  tina.right(45)
  tina.pendown()
  tina.forward(50)  
  tina.left(135)
  tina.forward(50)
  print("next playey!!!!!")
  
def o_shape():
  tina.color("black")
  tina.dot(50)



# This is the variable (storage box) that stores the DECISION NUMBER
CURRENT_SHAPE_TO_PLAY = 1

# This is the function that uses the DECISION NUMBER:
def draw_current_shape():
  global CURRENT_SHAPE_TO_PLAY
  print ("I am at the top of function draw_current_shape.")
  print ("The current decision number is: " + str(CURRENT_SHAPE_TO_PLAY))
  # Make the decision about which marker to draw,
  # based on whether the decision number is ODD or EVEN.
  if (CURRENT_SHAPE_TO_PLAY % 2) == 0:
    print("About to launch the function that draws an O marker")
    #EVEN CHOICE
    o_shape()
  else:
    #ODD CHOICE
    print("About to launch the function that draws an X marker")
    x_shape()
  # One last thing to do: 
  # Prepare for the *next* iteration by adding 1 to the decision number.
  CURRENT_SHAPE_TO_PLAY = CURRENT_SHAPE_TO_PLAY + 1







  
# KEY RESPONDER FUNCTIONS

# Each goto should go to the center of the cell
def go_upper_right():
  tina.color("black")
  tina.penup()
  tina.goto(130, 130)   # This is center of cell, doesn't worry about which marker
  draw_current_shape()
  print("next player!!!!!!!!")
def go_upper_middle_colum():
  tina.color("black")
  tina.penup()
  tina.goto(00, 130)
  draw_current_shape()
  print("next player!!!!!!!!")
def go_middle_middle_colum():
  tina.color("black")
  tina.penup()
  tina.goto(00, 00)
  draw_current_shape()
  print("next player!!!!!!!!")
def go_bottom_middle_colum():
  tina.color("black")
  tina.penup()
  tina.goto(000, -130)
  draw_current_shape()
  print("next player!!!!!!!!")
def go_upper_left():
  tina.color("black")
  tina.penup()
  tina.goto(-130, 130)
  draw_current_shape()
  print("next player!!!!!!!!")
def go_middle_left():
  tina.color("black")
  tina.penup()
  tina.goto(-130, -000)
  draw_current_shape()
  print("next player!!!!!!!!")
def go_bottom_left():
  tina.color("black")
  tina.penup()
  tina.goto(-130, -130)
  draw_current_shape()
  print("next player!!!!!!!!")
def go_bottom_right():
  tina.color("black")
  tina.penup()
  tina.goto(130, -130)
  draw_current_shape()
  print("next player!!!!!!!!")
def go_middle_right():
  tina.color("black")
  tina.penup()
  tina.goto(130, 00)
  draw_current_shape()
  print("next player!!!!!!!!")
  
screen.listen()
  
screen.onkey(go_upper_right, 'o')
screen.onkey(go_middle_right, 'k')
screen.onkey(go_bottom_right, 'm')  
screen.onkey(go_upper_middle_colum, 'i')  
screen.onkey(go_middle_middle_colum, 'j')  
screen.onkey(go_bottom_middle_colum, 'n')  
screen.onkey(go_upper_left, 'u') 
screen.onkey(go_middle_left, 'h')  
screen.onkey(go_bottom_left, 'b')  

draw_gameboard()
