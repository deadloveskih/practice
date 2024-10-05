from .Question import *
import csv

class QuestionareLogic:
    def __init__(self, user):
        self.user = user
        self.current_question = -1
        self.questions = []
        self.fieldnames = ["id", "question", "answers"]

    def load_questions(self, path):
        with open(path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=self.fieldnames)

            for row in reader:
                q = self.create_question(int(row["id"]), row["question"], row["answers"])
                self.questions.append(q)

    def get_next_question(self):
        self.current_question += 1
        return self.questions[self.current_question]
    
    @staticmethod
    def create_question(id, question, answers):
        if "|" in answers:
            answers = answers.split("|")
            return RadioButtonQuestion(id, question, answers[:-1], answers[int(answers[-1])])
        else:
            return TextInputQuestion(id, question, answers)