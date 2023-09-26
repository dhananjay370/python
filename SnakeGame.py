import turtle
import random
import time

delay = 0.1
score = 0
highest_Score = 0
bodies = []

# Creating Screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("lightblue")
s.setup(width=600, height=600)

# Creating a head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"  # type: ignore

# Creating a body
# Creating a Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.ht()
food.goto(150, 200)
food.st()

# Creating a Score Board
sb = turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.penup()
sb.ht()
sb.goto(-280, 270)
sb.write("Score : 0 | Highest Score : 0")


# Creating a function for moving all direction
def moveUp():
    if head.direction != "down":  # type: ignore
        head.direction = "up"  # type: ignore


def moveDown():
    if head.direction != "up":  # type: ignore
        head.direction = "down"  # type: ignore


def moveLeft():
    if head.direction != "right":  # type: ignore
        head.direction = "left"  # type: ignore


def moveRight():
    if head.direction != "left":  # type: ignore
        head.direction = "right"  # type: ignore


def moveStop():
    head.direction = "stop"  # type: ignore


def move():
    if head.direction == "up":  # type: ignore
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":  # type: ignore
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "down":  # type: ignore
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":  # type: ignore
        x = head.xcor()
        head.setx(x + 20)


# Event Handeling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# Mainloop
while True:
    s.update()
    if head.xcor() > 290:
        head.setx(-290)

    if head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)

    if head.ycor() < -290:
        head.sety(290)

    # Check colision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # increase body of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)
        score = score + 100  # updating score
        delay = delay - 0.001  # Increasing speed
        if score > highest_Score:
            highest_Score = score  # Updating Highest Score
        sb.clear()
        sb.write(f"Score : {score} | Highest Score : {highest_Score}")
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()

    # Check colision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"  # type: ignore
            for body in bodies:
                body.ht()
            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write(f"Score : {score} | Highest Score : {highest_Score}")
    time.sleep(delay)
turtle.done()
