import os
import shutil
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define your categories
CATEGORIES = ["shoulder", "knee", "spine", "wrist", "skull", "thigh_bones", "hand", "leg", "toe"]

# ========== DO NOT TOUCH THIS SECTION =============
SOURCE_DIR = "./image_folder"               
DEST_DIR = "./Categorized_XRays"     
# ========= DO NOT TOUCH THIS SECTION ==============


for cat in CATEGORIES:
    os.makedirs(os.path.join(DEST_DIR, cat), exist_ok=True)

# Get all images in root folder (excluding already categorized ones)
images = [f for f in os.listdir(SOURCE_DIR)
          if f.lower().endswith(('.png', '.jpg', '.jpeg'))
          and not os.path.isdir(os.path.join(SOURCE_DIR, f))]

img_index = 0

# GUI App
root = tk.Tk()
root.title("🩻 X-Ray Image Categorizer")
root.configure(bg="#1e1e2f")
root.geometry("600x700")

# Header Label
header = tk.Label(root, text="🩺 Manual X-Ray Categorization Tool",
                  font=("Helvetica", 18, "bold"), fg="#00ffe1", bg="#1e1e2f", pady=10)
header.pack()

# Image display frame
frame = tk.Frame(root, bg="#2a2a40", bd=2, relief=tk.RIDGE)
frame.pack(pady=10)

img_label = tk.Label(frame, bg="#2a2a40")
img_label.pack(padx=10, pady=10)

# Load and display image
def load_image():
    global img_index
    if img_index < len(images):
        img_path = os.path.join(SOURCE_DIR, images[img_index])
        try:
            img = Image.open(img_path)
            img.thumbnail((500, 500))
            tk_img = ImageTk.PhotoImage(img)
            img_label.config(image=tk_img)
            img_label.image = tk_img
            root.title(f"{img_index+1}/{len(images)} - {images[img_index]}")
        except:
            img_index += 1
            load_image()
    else:
        img_label.config(text="🎉 All images categorized!", fg="white", bg="#2a2a40", font=("Helvetica", 14, "bold"))
        for btn in buttons:
            btn.config(state='disabled')

# Categorize and move image
def categorize(category):
    global img_index
    src = os.path.join(SOURCE_DIR, images[img_index])
    dst = os.path.join(DEST_DIR, category, images[img_index])
    shutil.move(src, dst)
    img_index += 1
    load_image()

canvas_frame = tk.Frame(root, bg="#1e1e2f")
canvas_frame.pack(pady=20, fill="both", expand=True)

canvas = tk.Canvas(canvas_frame, bg="#1e1e2f", highlightthickness=0)
scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#1e1e2f")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add buttons to scrollable_frame
buttons = []
colors = ["#ff7675", "#74b9ff", "#55efc4", "#ffeaa7", "#fab1a0", "#a29bfe", "#81ecec", "#fd79a8", "#fdcb6e"]

for i, cat in enumerate(CATEGORIES):
    btn = tk.Button(scrollable_frame, text=cat.upper(), width=15, height=2,
                    font=("Arial", 10, "bold"), bg=colors[i], fg="black",
                    activebackground="#2d3436", activeforeground="white",
                    command=lambda c=cat: categorize(c))
    btn.grid(row=i//3, column=i%3, padx=10, pady=10)
    buttons.append(btn)

# Start with first image
load_image()

# Run app
root.mainloop()
