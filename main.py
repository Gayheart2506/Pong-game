from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision on wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # the ball should bounce
        ball.bounce_y()
    # detect collision with right_paddle and left paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle miss
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_ball()

    # detect left paddle miss
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_ball()

screen.exitonclick()
