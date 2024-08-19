from tkinter import *

class search_question_via:
    def __init__(self):
        root = Tk()
        root.title("Speech or Text")
        root.geometry('250x50')

        question_label = Label(text='Would you like to ask via Speech or text?').grid(row=0, column=0, columnspan=2)

        def answer0():
            global answer
            self.answer = 0
            print(self.answer)
            root.destroy()

        def answer1():
            global answer
            self.answer = 1
            print(self.answer)
            root.destroy()

        speech_button = Button(root, text="Speech", command=answer0).grid(row=1, column=0)
        text_button = Button(root, text="Text", command=answer1).grid(row=1, column=1)

        root.mainloop()