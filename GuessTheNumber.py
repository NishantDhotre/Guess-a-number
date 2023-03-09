from tkinter import *
import random
import tkinter


def start():
    h = random.randrange(1, 201)
    startButton.destroy()
    heading.destroy()

    def result(x):
        hidden = h
        if x == hidden:
            heading2.configure(text="Nailed it!")
            endButton.destroy()
        elif x < hidden:
            heading2.configure(text="Your guess is too low")
        else:
            heading2.configure(text="Your guess is too high")

    instructionPromt = Label(window, text="enter you'r guess:  ", fg="green")
    instructionPromt.place(relx=0.2, rely=0.4, anchor=CENTER)
    heading2 = Label(window, text="\" Let's start the game\"", fg="black")
    heading2.place(relx=0.5, rely=0.2, anchor=CENTER)



    inputSection = Entry(window, width=10, bg="white")
    inputSection.focus()
    inputSection.place(relx=0.5, rely=0.4, anchor=CENTER)

    def up():
        instructionPromt.destroy()
        submitButton.destroy()
        inputSection.destroy()
        endButton.destroy()
        heading2.configure(text="   the ans = " + str(h))
        return

    def clicked():
        x = int(inputSection.get())
        result(x)

    submitButton = Button(window,
                 text="submit",
                 bg="green",
                 fg="white",
                 command=clicked)
    submitButton.place(relx=0.8, rely=0.4, anchor=CENTER)
    endButton = Button(window, text="Give up.!", fg="red", command = up)
    endButton.place(relx=0.5, rely=0.6, anchor=CENTER)


if __name__ == "__main__":
    window = Tk()
    window.title("Guess It..!")
    window.geometry('350x200')
    heading = Label(window, text="\"Guess the Number\"")
    heading.pack()
    heading.place(relx=0.5, rely=0.3, anchor=CENTER)
    startButton = tkinter.Button(window,
                        text=">start<",
                        bg="gray",
                        fg="white",
                        command=start)
    startButton.pack()
    startButton.flash()
    startButton.place(relx=0.5, rely=0.5, anchor=CENTER)
    window.mainloop()
