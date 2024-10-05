import tkinter as tk

class ResultWindow:
    def __init__(self, root, questionare):
        self.root = root
        self.questionare = questionare
        self.frames = []
        for _ in range(len(self.questionare.questions)):
            self.frames.append(tk.Frame(self.root))

    def construct(self):
        for i in range(len(self.frames)):
            correct_answer = self.questionare.questions[i].get_answer()
            user_answer = self.questionare.user.answers[i]
            tk.Label(self.frames[i], text=f"{i+1}").pack(side="left", expand=True)
            tk.Label(self.frames[i], text=f"{correct_answer}").pack(side="left", expand=True)
            tk.Label(self.frames[i], text=f"{user_answer}").pack(side="left", expand=True)
            tk.Label(self.frames[i], text=f"{"+" if correct_answer == user_answer else "-"}").pack(side="left", expand=True)

        for frame in self.frames:
            frame.pack(fill="both", expand=False, padx=200, pady=10)

    def destruct(self):
        pass