from tkinter import *

class TextRequest:
    def __init__(self):
        root = Tk()
        root.geometry('200x200')
        root.title("Google Search")

        search_label = Label(root, text="What would you like to search?").grid(row=0, column=0, pady=10, padx=5)
        my_google_search = StringVar()
        my_search_request = Entry(root, textvariable=my_google_search).grid(row=1, column=0, pady=10, padx=5)

        def my_search():
            global search_data
            self.search_data = my_google_search.get()
            print(self.search_data)
            root.destroy()

        submit_search_request = Button(root, text="Submit", command=my_search).grid(row=2, column=0, pady=10, padx=5)

        root.mainloop()