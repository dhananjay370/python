import random
import string
import turtle

s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("White")
s.setup(width=600, height=600)


# Creating a head
head = turtle.Turtle()
head.speed(0)
head.color("Blue")
head.fillcolor("Green")
head.shape("circle")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Creating a food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.fillcolor("blue")
food.penup()
food.ht()
food.goto(150, 190)
food.st()


# Creating a Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.penup()
sb.ht()
sb.goto(-280, 270)
sb.write("Score : 0 | Highest Score : 0")

# Creating a function to move all direction
def moveUp():
    if head.direction == "Down":
        head.direction = "Up"

def moveDown():
    if head.direction == "Up":
        head.direction = "Down"

def moveRight():
    if head.direction == "Left":
        head.direction == "Right"

def moveLeft():
    if head.direction  == "Right":
        head.direction = "Left"

def moveStop():
    head.direction = "stop"


turtle.done()
