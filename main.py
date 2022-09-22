from tkinter import *

FONT = ("Arial", 12)
window = Tk()
window.title("My first GUI program! :D")  # Title of the window
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


def button_pressed():
    kilometers = int(user_input.get()) * 1.60934  # Mile to kilometer conversion formula.
    answer.delete(0, END)  # Deletes the previous text inside the answer box. 
    answer.insert(END, str(kilometers))  # Inserts the new answer in the answer box.
    print("BUTTON PRESSED!")


# Where the number that will be converted is inputted.
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# Where the converted Mile number will be placed.
answer = Entry(width=10)
answer.grid(column=1, row=1)

# Placed right beside the answer.
label = Label(text="is equal to", font=FONT)
label.grid(column=0, row=1)

# The calculate button, calls the function "button_pressed" when it is pressed.
button = Button(text="Calculate", command=button_pressed)
button.grid(column=1, row=2)

# Label of the mile input.
m_label = Label(text="Miles", font=FONT)
m_label.grid(column=2, row=0)

# Label if the kilometer answer.
km_label = Label(text="kilometers", font=FONT)
km_label.grid(column=2, row=1)

window.mainloop()
