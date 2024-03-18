from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
score = Scoreboard()
score.update()

screen.listen()
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_r_paddle()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_l_paddle()

    if ball.xcor() > 380:
        ball.ball_reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.ball_reset()
        score.r_point()

screen.exitonclick()
