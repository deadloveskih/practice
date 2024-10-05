import tkinter as tk
from questionare.Question import *
from .ResultWindow import ResultWindow

class QuestionWindow:
    def __init__(self, root, questionare):
        self.root = root
        self.questionare = questionare
    
    def construct(self):
        self.frames = []
        for _ in range(3):
            self.frames.append(tk.Frame(self.root))

        question = self.questionare.get_next_question()

        text = tk.Text(self.frames[0], height=10)
        text.insert(1.0, question.get())
        text['state'] = 'disabled'

        text.pack(side="left", expand=True)
        tk.Label(self.frames[1], text = "Ваш ответ: ").pack(side="left", expand=True)

        self.construct_answer_field(question)

        for frame in self.frames:
            frame.pack(fill="both", expand=False, padx=200, pady=10)

    def destruct(self, answer):
        self.questionare.user.add_answer(answer)
        for frame in self.frames:
            frame.destroy()
            
        if self.questionare.current_question != len(self.questionare.questions)-1:
            self.construct()
        else:
            self.questionare.user.save()
            result_window = ResultWindow(self.root, self.questionare)
            result_window.construct()

    def construct_answer_field(self, question):
        if isinstance(question, TextInputQuestion):
            answer = tk.Entry(self.frames[1])
            answer.focus()
            answer.pack(side="left", expand=True)
            tk.Button(self.frames[2], text = 'Ответить', \
                      command=lambda: self.destruct(answer.get())).pack(side="left", expand=True)
        elif isinstance(question, RadioButtonQuestion): 
            for answer in question.get_options():
                radio_button = tk.Radiobutton(self.frames[1], text=answer, value=answer, \
                                              command=lambda a=answer: self.destruct(a))
                radio_button.pack(side="left", expand=True)