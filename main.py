from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_save():
    site = website_entry.get()
    email = email_entry.get()
    passw = password_entry.get()

    if len(site) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showwarning(title="Complete the Form", message="Please you forgot to complete the data")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"Do you want to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{site} --- {email} --- {passw}\n")
                clear()

def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creating Canvas
locker_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=locker_img)
canvas.grid(column=1, row=1, columnspan=3)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=1, row=2)
email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)
password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

# Entries
website_entry = Entry(width=39)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "ericbobcamargo@gmail.com")

password_entry = Entry(width=19)
password_entry.grid(column=2, row=4)

# Buttons
generate_btn = Button(text="Generate Password", command=password_generator)
generate_btn.grid(column=3, row=4)

add_btn = Button(text="Add", width=34, command=password_save)
add_btn.grid(column=2, row=5, columnspan=2)

window.mainloop()
