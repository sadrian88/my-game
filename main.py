import tkinter as tk
import random

class TriviaGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Trivia Game")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "Berlin", "Madrid", "Rome"],
                "answer": "Paris"
            },
            {
                "question": "What is the currency of Japan?",
                "options": ["Dollar", "Euro", "Yen", "Pound"],
                "answer": "Yen"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Salvador Dali"],
                "answer": "Leonardo da Vinci"
            }
        ]

        self.current_question = None
        self.score = 0

        self.question_label = tk.Label(master, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", font=("Helvetica", 12), command=lambda i=i: self.answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=("Helvetica", 12))
        self.score_label.pack(pady=20)

        self.new_question()

    def new_question(self):
        self.current_question = random.choice(self.questions)
        self.question_label.config(text=self.current_question["question"])
        random.shuffle(self.current_question["options"])
        for i in range(4):
            self.option_buttons[i].config(text=self.current_question["options"][i])

    def answer(self, index):
        if self.current_question["options"][index] == self.current_question["answer"]:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.new_question()

if __name__ == "__main__":
    root = tk.Tk()
    trivia_game = TriviaGame(root)
    root.mainloop()
