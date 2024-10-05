import tkinter as tk
from .QuestionWindow import QuestionWindow
from .ResultWindow import ResultWindow
from user.User import User
from questionare.QuestionareLogic import QuestionareLogic

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.frames =  []
        self.entrys = []
        for _ in range(4):
            self.frames.append(tk.Frame(self.root))

    def construct(self):

        tk.Label(self.frames[0], text="Имя: ").pack(side="left", expand=True)
        tk.Label(self.frames[1], text="Фамилия: ").pack(side="left", expand=True)
        tk.Label(self.frames[2], text="Группа: ").pack(side="left", expand=True)

        for i in range(3):
            self.entrys.append(tk.Entry(self.frames[i]))
        
        for i in range(3):
            self.entrys[i].pack(side="left", expand=True, fill="x")

        tk.Button(self.frames[3], \
                  text="Продолжить", \
                    command=lambda: \
                    self.destruct(self.entrys[0].get(), self.entrys[1].get(), self.entrys[2].get())).\
                    pack(side="left", expand=True, fill="x")

        for i in range(4):
            self.frames[i].pack(fill="both", expand=False, padx=250, pady=10)
        
        self.entrys[0].focus()

    def destruct(self, name, second_name, group):
        for frame in self.frames:
            frame.destroy()

        user = User(name, second_name, group)
        questionare = QuestionareLogic(user)
        questionare.load_questions("./data/questions.csv")

        if user.load():
            result_window = ResultWindow(self.root, questionare)
            result_window.construct()
        else:
            question_window = QuestionWindow(self.root, questionare)
            question_window.construct()