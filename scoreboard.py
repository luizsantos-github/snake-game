from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
