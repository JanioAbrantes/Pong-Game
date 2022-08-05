from turtle import Turtle


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.score = -1
        self.penup()
        self.goto(position)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align='center', font=('Verdana', 80, 'normal'))

    def rede(self):
        self.clear()
        self.write('l\n'*100, align='center', font=('Verdana', 15, 'normal'))

    def game_over(self):
        self.clear()
        self.write('FIM DE JOGO', align='center', font=('Verdana', 60, 'normal'))
