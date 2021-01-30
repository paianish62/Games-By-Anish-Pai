from tkinter import *
from random import shuffle
from random import choice
from tkinter import messagebox

jumbl = Tk()
jumbl.geometry("600x400")



slvar = StringVar()
hintvar = StringVar()
countries = ["India", "Canada", "Australia", "Qatar", "Ireland", "Brazil", "Spain","South Africa", "United States", "New Zeland", "Iceland"]
word = ""

def ans(wordg):
    global word
    if word == wordg:
        messagebox.showinfo(title = "Answer", message = "Congrats, You got it right !")
        shufflew()
    else:
        messagebox.showinfo(title = "Answer", message = "Sorry, wrong answer try again")

def hint():
    global hintvar
    global word
    l = len(hintvar.get())
    x = hintvar.get()
    x += word[l]
    print(x)
    hintvar.set(x)

def shufflew():
    slvar.set("")
    global countries
    global word
    word = choice(countries)
    wordlis = list(word)
    shword = "" 
    shuffle(wordlis)
    for i in wordlis:
        shword += i
    slvar.set(shword)


shufflew()
shuffled_letters = Label(jumbl, textvariable = slvar)
shuffled_letters.pack(pady=20)

ans_entry = Entry(jumbl)
ans_entry.pack(pady=20)

frame1 = Frame(jumbl)
frame1.pack(padx=20,pady=20)
ans_b = Button(frame1, text = "Submit", command = lambda : ans(ans_entry.get()))
ans_b.grid(row = 1, column = 0, padx = 10)

next_b = Button(frame1, text = "Pick Another Word", command = shufflew)
next_b.grid(row = 1, column = 1, padx = 10)

hint_b = Button(frame1, text = "Hint", command = hint)
hint_b.grid(row = 1, column = 2, padx = 10)

hint_l = Label(jumbl, textvariable = hintvar)
hint_l.pack(padx=10,pady=10)

jumbl.mainloop()

