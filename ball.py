from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.8, 0.8)
        self.color('magenta')
        self.penup()

    def move(self, valor_x, valor_y):
        new_x = self.xcor() + valor_x
        new_y = self.ycor() + valor_y
        self.goto(new_x, new_y)
