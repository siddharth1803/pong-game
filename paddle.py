from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)

    def up(self):
        paddle_new_ycor = self.ycor() + 20
        self.goto(self.xcor(), paddle_new_ycor)

    def down(self):
        paddle_new_ycor = self.ycor() - 20
        self.goto(self.xcor(), paddle_new_ycor)
