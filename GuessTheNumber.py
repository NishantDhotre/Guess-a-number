from tkinter import *
import random
import tkinter


def start():
    h = random.randrange(1, 201)
    bt.destroy()
    lbll3.destroy()

    def result(x):
        hidden = h
        if x == hidden:
            lbl2.configure(text="Nailed it!")
            btnn.destroy()
        elif x < hidden:
            lbl2.configure(text="Your guess is too low")
        else:
            lbl2.configure(text="Your guess is too high")

    lbl = Label(window, text="enter you'r guess:  ", fg="green")
    lbl.grid(column=1, row=4)
    lbl2 = Label(window, text="\" Let's start the game\"", fg="black")
    lbl2.grid(column=2, row=1)

    lbl3 = Label(window, text="")
    lbl3.grid(column=1, row=2)
    lbl4 = Label(window, text="")
    lbl4.grid(column=1, row=3)
    lbl6 = Label(window, text="")
    lbl6.grid(column=1, row=5)

    txt = Entry(window, width=10, bg="white")
    txt.focus()
    txt.grid(column=2, row=4)

    def up():
        lbl.destroy()
        btn.destroy()
        txt.destroy()
        btnn.destroy()
        lbl2.configure(text="   the ans = " + str(h))
        return

    def clicked():
        x = int(txt.get())
        result(x)

    btn = Button(window,
                 text="submit",
                 bg="green",
                 fg="white",
                 command=clicked)
    btn.grid(column=3, row=4)
    btnn = Button(window, text="Give up.!", fg="red", command = up)
    btnn.grid(column=2, row=6)


if __name__ == "__main__":
    window = Tk()
    window.title("Guess It..!")
    window.geometry('350x200')
    lbll3 = Label(window, text="\"Guess the Number\"")
    lbll3.pack()
    bt = tkinter.Button(window,
                        text=">start<",
                        bg="gray",
                        fg="white",
                        command=start)
    bt.pack()
    bt.flash()
    window.mainloop()
