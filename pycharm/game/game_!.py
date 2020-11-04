import turtle
import time

wn = turtle.Screen()
wn.title("pong by rsd")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0.5)
paddle_a.shape("square")game_!.pyls

paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0.1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0.1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.6
ball.dy = -0.6

# pen
pen = turtle.Turtle()
pen.speed(0.1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0  Player B : 0", align="center", font=("courier", 24, "normal"))




# function

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boarder checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() - 45):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 45 and ball.ycor() > paddle_a.ycor() - 45):
        ball.setx(-340)
        ball.dx *= -1

    if score_a==5:
        wn.update()
        pen.clear()
        ball.clear()
        paddle_a.clear()
        paddle_b.clear()
        pen.goto(0,0)
        pen.write("Player A Won",align="center", font=("courier", 35, "normal"))
        time.sleep(5)
        pen.clear()

    if score_b==5:
        wn.update()
        pen.clear()
        ball.clear()
        paddle_a.clear()
        paddle_b.clear()
        pen.goto(0,0)
        pen.write("Player B Won",align="center", font=("courier", 35, "normal"))
        time.sleep(5)
        pen.clear()
