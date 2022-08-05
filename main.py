from turtle import Turtle, Screen, getcanvas
from players import Players
from time import sleep
from textos import Score
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)  # Tira a animação da tartaruga

player1 = Players((-370, 0))
player2 = Players((370, 0))

player1_score = Score((-100, 180))
player1_score.update_score()
player2_score = Score((100, 180))
player2_score.update_score()

rede = Score((0, -320))
rede.rede()

ball = Ball()

game_over_message = Score((0, -40))

screen.listen()

screen.onkey(player1.go_up, 'w')
screen.onkey(player1.go_down, 's')
screen.onkey(player2.go_up, 'Up')
screen.onkey(player2.go_down, 'Down')

game_over = False

bola_x = 10
bola_y = 10
while not game_over:
    player1.keep_going()
    player2.keep_going()
    ball.move(bola_x, bola_y)
    if ball.ycor() >= 290 or ball.ycor() <= -280:
        bola_y = bola_y * -1

    if ball.xcor() >= 380:
        player1_score.update_score()
        bola_x = -10
        ball.goto(0, 0)

    if ball.xcor() <= -380:
        player2_score.update_score()
        bola_x = 10
        ball.goto(0, 0)

    if ball.distance(player1) < 50 and ball.xcor() < -340 or ball.distance(player2) < 50 and ball.xcor() > 340:
        bola_x = bola_x * -1


    if player1_score.score == 3 or player2_score.score == 3:
        game_over_message.game_over()
        game_over = True
        ball.hideturtle()


    sleep(0.03)
    screen.update()



screen.exitonclick()
