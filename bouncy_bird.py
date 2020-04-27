import turtle

wn = turtle.Screen()
wn.title("kevin")
wn.bgcolor("black")
wn.setup(width = 1000,height=600)

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.color('white')
ball.penup()
ball.goto(-500,0)
ball.pendown()
ball.dx = 2
ball.dy = 12


land = turtle.Turtle()
land.shape("square")
land.sety(-11)
land.shapesize(stretch_wid=0.01, stretch_len=150)
land.color("white")

def ball_jump():

    ball.dx = 2
    ball.dy = 12
    for i in range(0,25):
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        ball.dy = ball.dy - 0.5
    if(int(ball.ycor())>=0):
        go_back_to_land()

def go_back_to_land():
    if( int(ball.ycor())>0):
        k = int(ball.ycor())
        while (int(ball.ycor()) >0):
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() - ball.dy)
            ball.dy = ball.dy + 0.5


wn.listen()
wn.onkeypress(ball_jump , "Up")




while True:
    wn.update()