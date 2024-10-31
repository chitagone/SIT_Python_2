import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Login System")
window.geometry("400x400")
window.configure(highlightthickness=4, highlightbackground="black")

def login():
    username = entry_username.get()
    password = entry_password.get()
   
    
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password.")

# Function to load and resize images
def load_and_resize_image(path, size):
    try:
        image = Image.open(path)
        image = image.resize(size, Image.Resampling.LANCZOS)  # Resize the image
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image '{path}': {e}")
        return None

image1 = load_and_resize_image("./man.png", (30, 30))
image2 = load_and_resize_image("./lock.png", (30, 30))



label1 = Label(window, image=image1)
label1.pack(pady=5)
label_username = tk.Label(window, text="Username:", fg='blue', font=("bold", 15))
label_username.pack(pady=5)

entry_username = tk.Entry(window,bd=5)
entry_username.pack(pady=5)


label2 = Label(window, image=image2)
label2.pack(pady=5)
label_password = tk.Label(window, text="Password:", fg='blue', font=("bold", 15))
label_password.pack(pady=5)
entry_password = tk.Entry(window, show="*",width=20,bd=5)
entry_password.pack(pady=5)

login_button = tk.Button(window, text="Login", command=login,fg='blue',width=22,bd=5)
login_button.pack(pady=20)

window.mainloop()