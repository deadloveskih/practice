from windows.LoginWindow import LoginWindow
import tkinter as tk

class Questionare:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Questionare")
        self.root.geometry("750x400")
        self.root.resizable(False, False)

    def start(self):
        self.login_window = LoginWindow(self.root)
        self.login_window.construct()
        self.root.mainloop()


if __name__ == "__main__":
    app = Questionare()
    app.start()