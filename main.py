from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_save():
    site = website_entry.get()
    email = email_entry.get()
    passw = password_entry.get()
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
generate_btn = Button(text="Generate Password")
generate_btn.grid(column=3, row=4)

add_btn = Button(text="Add", width=34, command=password_save)
add_btn.grid(column=2, row=5, columnspan=2)

window.mainloop()
