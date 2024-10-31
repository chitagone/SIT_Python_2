from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()
root.title("Home work2")

# Configure grid to center and distribute space
root.grid_columnconfigure(0, weight=1)  # Add extra columns to center
root.grid_columnconfigure(6, weight=1)  # Assuming 5 columns for the labels

# Function to load and resize images
def load_and_resize_image(path, size):
    try:
        image = Image.open(path)
        image = image.resize(size, Image.Resampling.LANCZOS)  # Resize the image
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image '{path}': {e}")
        return None

# Function to toggle the visibility of the text label
def toggle_text(label):
    if label.winfo_viewable():  # Check if the label is currently visible
        label.grid_remove()  # Hide the label
    else:
        label.grid()  # Show the label

# Load and resize the images
image1 = load_and_resize_image("./coffee.png", (100, 100))
image2 = load_and_resize_image("./drink.png", (100, 100))
image3 = load_and_resize_image("./burger.png", (100, 100))
image4 = load_and_resize_image("./cupcake.png", (100, 100))
image5 = load_and_resize_image("./donut.png", (100, 100))

# Create labels for the images and toggle text on click
label1 = Label(root, image=image1)
label1.grid(row=1, column=1, padx=10, pady=10)  # Added padding
label1.bind("<Button-1>", lambda e: toggle_text(text_label1))

label2 = Label(root, image=image2)
label2.grid(row=1, column=2, padx=10, pady=10)  # Added padding
label2.bind("<Button-1>", lambda e: toggle_text(text_label2))

label3 = Label(root, image=image3)
label3.grid(row=1, column=3, padx=10, pady=10)  # Added padding
label3.bind("<Button-1>", lambda e: toggle_text(text_label3))

label4 = Label(root, image=image4)
label4.grid(row=1, column=4, padx=10, pady=10)  # Added padding
label4.bind("<Button-1>", lambda e: toggle_text(text_label4))

label5 = Label(root, image=image5)
label5.grid(row=1, column=5, padx=10, pady=10)  # Added padding
label5.bind("<Button-1>", lambda e: toggle_text(text_label5))

# Create text labels for each image, initially hidden
text_label1 = Label(root, text='Coffee', fg='red')
text_label1.grid(row=2, column=1, padx=20, pady=0.5)
text_label1.grid_remove()  # Hide initially

text_label2 = Label(root, text='Drink', fg='red')
text_label2.grid(row=2, column=2, padx=20, pady=0.5)
text_label2.grid_remove()  # Hide initially

text_label3 = Label(root, text='Burger', fg='red')
text_label3.grid(row=2, column=3, padx=20, pady=0.5)
text_label3.grid_remove()  # Hide initially

text_label4 = Label(root, text='Cupcake', fg='red')
text_label4.grid(row=2, column=4, padx=20, pady=0.5)
text_label4.grid_remove()  # Hide initially

text_label5 = Label(root, text='Donut', fg='red')
text_label5.grid(row=2, column=5, padx=20, pady=0.5)
text_label5.grid_remove()  # Hide initially

# Start the Tkinter event loop
root.mainloop()