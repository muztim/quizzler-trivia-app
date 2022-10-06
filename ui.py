from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=250, height=400)
        self.window.config(padx=0, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="The question goes here",
            fill="black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score = Label(text=f"Score: {0}", bg=THEME_COLOR, foreground="white", font=("Arial", 12, "normal"))
        self.score.grid(column=1, row=0)

        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image, command=self.true_answer)
        self.true.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image, command=self.false_answer)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_answer(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)