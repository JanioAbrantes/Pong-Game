from turtle import Turtle

class Players(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.direcao = ''

    def go_up(self):
        self.direcao = 'up'
        up = self.ycor() + 20
        if up <= 240:
            self.goto(self.xcor(), up)

    def go_down(self):
        self.direcao = 'down'
        down = self.ycor() - 20
        if down >= -240:
            self.goto(self.xcor(), down)

    def keep_going(self):
        if self.direcao == 'up':
            self.go_up()

        if self.direcao == 'down':
            self.go_down()
