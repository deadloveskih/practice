import csv
import os.path

class User:
    def __init__(self, name, second_name, group):
        self.name = name
        self.second_name = second_name
        self.group = group
        self.answers = []

    def __str__(self):
        return f"{self.name} {self.second_name} {self.group}"

    def __repr__(self):
        return f"{self.name} {self.second_name} {self.group}"
    
    def load(self):
        if os.path.exists(f"./data/users/{self.name+self.second_name+self.group}.csv"):
            with open(f"./data/users/{self.name+self.second_name+self.group}.csv", "r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file, delimiter=";")
                for row in reader:
                    self.name = row["name"]
                    self.second_name = row["second_name"]
                    self.group = row["group"]
                    self.answers = row["answers"].split(",")
                
                return True
        
        return False

    def save(self):
        with open(f"./data/users/{self.name+self.second_name+self.group}.csv", "w", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["name", "second_name", "group", "answers"], delimiter=";")

            writer.writeheader()
            writer.writerow(self.__dict__)

    def add_answer(self, answer):
        if answer:
            self.answers.append(answer)
        else:
            self.answers.append("Вопрос пропущен")