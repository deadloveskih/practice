class Question:
    def __init__(self, id, question):
        self.id = id
        self.question = question

    def get(self):
        return self.question
    
class RadioButtonQuestion(Question):
    def __init__(self, id, question, options, answer):
        super().__init__(id, question)
        self.options = options
        self.answer = answer

    def get(self):
        return self.question

    def get_answer(self):
        return self.answer
    
    def get_options(self):
        return self.options

class TextInputQuestion(Question):
    def __init__(self, id, question, answer):
        super().__init__(id, question)
        self.answer = answer

    def get(self):
        return self.question

    def get_answer(self):
        return self.answer