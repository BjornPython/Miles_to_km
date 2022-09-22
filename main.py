from tkinter import *

FONT = ("Arial", 12)
window = Tk()
window.title("My first GUI program! :D")  # Title of the window
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)


def mtokm_button_pressed():
    """Deletes the previous answer, and Calculates and inputs the ammount of Kilometers. """
    kilometers = int(user_input.get()) * 1.60934  # Miles to kilometers conversion formula.
    answer.delete(0, END)  # Deletes the previous text inside the answer box.
    answer.insert(END, str(kilometers))  # Inserts the new answer in the answer box.
    print("BUTTON PRESSED!")


def kmtom_button_pressed():
    """Deletes the previous answer, and Calculates and inputs the ammount of Miles. """
    kilometers = int(user_input.get()) * 0.621371  # Kilometers to Miles conversion formula.
    answer.delete(0, END)  # Deletes the previous text inside the answer box.
    answer.insert(END, str(kilometers))  # Inserts the new answer in the answer box.
    print("BUTTON PRESSED!")


def switch():
    """Switches the text of first_label and second_label,
    and changes the command of the calculate button."""
    if first_label["text"] == "Miles":
        answer.delete(0, END)  # Deletes the answer in the answer box.
        first_label.config(text="Kilometers")
        second_label.config(text="Miles")
        calculate.config(command=kmtom_button_pressed)

    else:
        answer.delete(0, END)
        first_label.config(text="Miles")
        second_label.config(text="Kilometers")
        calculate.config(command=mtokm_button_pressed)


# Where the number that will be converted is inputted.
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

# Where the converted Mile number will be placed.
answer = Entry(width=10)
answer.grid(column=1, row=1)

#  Placed right beside the user input.
input_label = Label(text="Input here: ", font=FONT)
input_label.grid(column=0, row=0)

# Placed right beside the answer.
answer_label = Label(text="is equal to", font=FONT)
answer_label.grid(column=0, row=1)

# The calculate button. Calls the function "mtokm_button_pressed" when it is pressed.
calculate = Button(text="Calculate", command=mtokm_button_pressed)
calculate.grid(column=1, row=2)

button = Button(text="Switch Conversion", command=switch)
button.grid(column=1, row=3)

# Label of the first box.
first_label = Label(text="Miles", font=FONT)
first_label.grid(column=2, row=0)

# Label of the second box.
second_label = Label(text="kilometers", font=FONT)
second_label.grid(column=2, row=1)

window.mainloop()
