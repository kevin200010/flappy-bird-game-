import turtle

wn = turtle.Screen()
wn.title("kevin")
wn.bgcolor("black")
wn.setup(width=1000, height=600)

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.color('white')
ball.penup()
ball.goto(-500, 0)
#ball.pendown()
ball.dx = 2
ball.dy = 12
ball.power = 0

land = turtle.Turtle()
land.shape("square")
land.sety(-11)
land.shapesize(stretch_wid=0.01, stretch_len=150)
land.color("white")


def jump_ball():
    ball.power = 25
    while (ball.power > 0):
        ball.power = ball.power - 1
        ball.setx(ball.xcor() + 2)
        ball.sety(ball.ycor() + (ball.power / 2))
        if(int(ball.xcor()) > 480):
            ball.setx(-500)
    if(int(ball.ycor()) > 0 ):
        ball.power = 0
        while (int(ball.ycor()) > 0):
            ball.power = ball.power + 1
            ball.setx(ball.xcor() + 2)
            ball.sety(ball.ycor() - (ball.power / 2))
        ball.power = 0




wn.listen()
wn.onkeypress(jump_ball, "Up")

while True:
    wn.update()
