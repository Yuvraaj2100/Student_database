from tkinter import *
import csv
from tkinter import messagebox


def submit_form():
    # Retrieve form data
    name = e1.get()
    subject = e2.get()
    marks = e3.get()

    # Check if marks is a valid integer value
    if not marks.isdigit():
        messagebox.showerror("Error", "Please enter a valid integer value for marks.")
        return

    selected_grade = var.get()

    # Save form data to a CSV file
    with open("students.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "subject", "marks", "grade"])
        writer.writerow([name, subject, marks, selected_grade])

    # Clear form fields
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    var.set("A")  # reset the default radio but


def save_option():
    # Get the selected option
    selected_grade = var.get()

    # Save the selected option to a CSV file
    with open("students.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([selected_grade])


def exit_form():
    window.quit()


# Create the main window
window = Tk()


# Set window title and geometry
window.wm_title("Student Vault")
window.wm_geometry("1098x689+400+200")
window.title("Student Form")


def on_entry_click(event):
    if e1.get() == "Add entry":
        e1.delete(0, "end")  # delete all the text in the entry widget

    if e2.get() == "Add entry":
        e2.delete(0, "end")  # delete all the text in the entry widget
    if e3.get() == "Add entry":
        e3.delete(0, "end")


def on_entry_exit(event):
    if e1.get() == "":
        e1.insert(0, "Add entry")  # add a placeholder text
    if e2.get() == "":
        e2.insert(0, "Add entry")  # add a placeholder text
    if e3.get() == "":
        e3.insert(0, "Add entry")


# Create form fields
# {
L1 = Label(text="Name: ", font=20)
L1.config(bg="#E7D287", fg="black")
L1.place(relx=0.3, rely=0.2, anchor="center")
e1 = Entry(window, font=("Ink Free", 25), bg="#fff4b4", fg="#5A5A5A", width=20)
e1.place(relx=0.5, rely=0.2, anchor="center")
e1.insert(0, "Add entry")  # set the placeholder text
e1.bind(
    "<FocusIn>", on_entry_click
)  # bind the on_entry_click function to the FocusIn event
e1.bind(
    "<FocusOut>", on_entry_exit
)  # bind the on_entry_exit function to the FocusOut event
e1.place(relx=0.5, rely=0.2, anchor="center")
# }


# {
L1 = Label(text="Subject: ", font=20)
L1.config(bg="#E7D287", fg="black")
L1.place(relx=0.3, rely=0.35, anchor="center")

e2 = Entry(window, font=("Ink Free", 25), bg="#fff4b4", fg="#5A5A5A", width=20)
e2.insert(0, "Add entry")  # set the placeholder text
e2.bind(
    "<FocusIn>", on_entry_click
)  # bind the on_entry_click function to the FocusIn event
e2.bind(
    "<FocusOut>", on_entry_exit
)  # bind the on_entry_exit function to the FocusOut event
e2.place(relx=0.5, rely=0.35, anchor="center")
# }


# {
L1 = Label(text="Marks: ", font=20)
L1.config(bg="#E7D287", fg="black")
L1.place(relx=0.3, rely=0.5, anchor="center")

e3 = Entry(window, font=("Ink Free", 25), bg="#fff4b4", fg="#5A5A5A", width=20)
e3.insert(0, "Add entry")  # set the placeholder text
e3.bind(
    "<FocusIn>", on_entry_click
)  # bind the on_entry_click function to the FocusIn event
e3.bind(
    "<FocusOut>", on_entry_exit
)  # bind the on_entry_exit function to the FocusOut event
e3.place(relx=0.5, rely=0.5, anchor="center")
# }
# Create the radio buttons
var = StringVar()
rb1 = Radiobutton(window, text="A", variable=var, value="A")
rb2 = Radiobutton(window, text="B", variable=var, value="B")
rb3 = Radiobutton(window, text="C", variable=var, value="C")
rb4 = Radiobutton(window, text="D", variable=var, value="D")
rb5 = Radiobutton(window, text="E", variable=var, value="E")

# Place the radio buttons on the window using the place function
rb1.place(relx=0.35, rely=0.615)
rb2.place(relx=0.4, rely=0.615)
rb3.place(relx=0.45, rely=0.615)
rb4.place(relx=0.5, rely=0.615)
rb5.place(relx=0.55, rely=0.615)

rb1.config(bg="#E7D287", fg="#439E62")
rb2.config(bg="#E7D287", fg="#DDB166")
rb3.config(bg="#E7D287", fg="#DD924F")
rb4.config(bg="#E7D287", fg="#D06E3F")
rb5.config(bg="#E7D287", fg="#882424")
# }


# Create submit button
submit = Button(
    window,
    text="SUBMIT",
    width=10,
    height=2,
    highlightbackground="#E7D287",
    fg="#7F9E8C",
    command=submit_form,  # call submit_form when the button is clicked
)
exit = Button(
    window,
    text="EXIT",
    width=10,
    height=2,
    highlightbackground="#E7D287",
    fg="#A25752",
    command=exit_form,  # call exit_form when the button is clicked
)
exit.place(relx=0.5, rely=0.85, anchor="center")


submit.place(relx=0.5, rely=0.75, anchor="center")
window.config(background="#E7D287")
# Start the main event loop
window.mainloop()
