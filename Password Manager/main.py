from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import string
import pyperclip
import json

DIR = "./Password Manager/passwords.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Generate random password
def password_gen():
    password_input.delete(0, END)
    password_letters= [choice(string.ascii_letters) for _ in range(randint(8, 10))]
    symbol_range = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))
    password_symbols= [chr(choice(symbol_range)) for _ in range(randint(2, 4))]
    password_numbers= [str(randint(0,9)) for _ in range(randint(2, 4))]

    password = password_letters + password_symbols + password_numbers
    shuffle(password)
    print(password)
    password_char = "".join(password)
    password_input.insert(0, password_char)
    pyperclip.copy(password_char)
    # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showwarning(title="Warning", message="There are empty fields.")
    else:
        try:
            with open(DIR, "r") as passwords_file:
                # Read already stored data
                data = json.load(passwords_file)
                
        except FileNotFoundError:
            with open(DIR, "w") as passwords_file:
                # Write updated data do json file
                json.dump(new_data, passwords_file, indent=4)
        
        else:
            # Update data with new generated data
            data.update(new_data)
            with open(DIR, "w") as passwords_file:
                # Write updated data do json file
                json.dump(new_data, passwords_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def search():
    website = website_input.get()
    try:
        with open(DIR, "r") as passwords_file:
            data = json.load(passwords_file)
            
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found.")
    
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="error", message=f"No register for {website} found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./Password Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_input = Entry(width=25)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = Entry(width=43)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "email@email.com")
password_input = Entry(width=25)
password_input.grid(row=3, column=1)


generate_password_button = Button(text="Generate Password", command=password_gen)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=12, command=search)
search_button.grid(row=1 , column=2)


window.mainloop()