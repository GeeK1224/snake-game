from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    highest_score: int

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt", "r") as file:
            self.highest_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def get_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}, Highest Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

