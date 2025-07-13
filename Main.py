import os
import shutil
import tkinter as tk
from tkinter import messagebox, ttk
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
root.configure(bg="#0f1419")
root.geometry("700x800")
root.minsize(600, 700)

# Configure style for ttk widgets
style = ttk.Style()
style.theme_use('clam')

# Configure ttk scrollbar style
style.configure("Custom.Vertical.TScrollbar",
                background="#2a2d3a",
                troughcolor="#1a1d2a",
                bordercolor="#2a2d3a",
                arrowcolor="#00d4aa",
                darkcolor="#2a2d3a",
                lightcolor="#2a2d3a")

# Header Frame
header_frame = tk.Frame(root, bg="#0f1419", pady=15)
header_frame.pack(fill="x")

# Header Label with improved styling
header = tk.Label(header_frame, text="🩺 Manual X-Ray Categorization Tool",
                  font=("Segoe UI", 20, "bold"), fg="#00d4aa", bg="#0f1419")
header.pack()

# Progress info
progress_label = tk.Label(header_frame, text="",
                         font=("Segoe UI", 12), fg="#8892b0", bg="#0f1419")
progress_label.pack(pady=(5, 0))

# Image display frame with improved styling
image_frame = tk.Frame(root, bg="#1a1d2a", bd=0, relief=tk.FLAT)
image_frame.pack(pady=15, padx=20, fill="x")

# Add a subtle border effect
border_frame = tk.Frame(image_frame, bg="#00d4aa", height=2)
border_frame.pack(fill="x")

img_container = tk.Frame(image_frame, bg="#1a1d2a")
img_container.pack(pady=15, padx=15)

img_label = tk.Label(img_container, bg="#1a1d2a", fg="#ccd6f6")
img_label.pack()

# Load and display image
def load_image():
    global img_index
    if img_index < len(images):
        img_path = os.path.join(SOURCE_DIR, images[img_index])
        try:
            img = Image.open(img_path)
            # Maintain aspect ratio while fitting in display area
            img.thumbnail((450, 400), Image.Resampling.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            img_label.config(image=tk_img, text="")
            img_label.image = tk_img
            
            # Update progress
            progress_text = f"Image {img_index+1} of {len(images)} - {images[img_index]}"
            progress_label.config(text=progress_text)
            root.title(f"🩻 X-Ray Categorizer - {img_index+1}/{len(images)}")
        except Exception as e:
            print(f"Error loading image: {e}")
            img_index += 1
            load_image()
    else:
        img_label.config(image="", text="🎉 All images categorized!\nGreat job!", 
                        font=("Segoe UI", 16, "bold"), fg="#00d4aa")
        progress_label.config(text="Categorization complete!")
        for btn in buttons:
            btn.config(state='disabled')

# Categorize and move image
def categorize(category):
    global img_index
    if img_index < len(images):
        src = os.path.join(SOURCE_DIR, images[img_index])
        dst = os.path.join(DEST_DIR, category, images[img_index])
        try:
            shutil.move(src, dst)
            img_index += 1
            load_image()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to move image: {e}")

# Categories section header
categories_header = tk.Label(root, text="Select Category:",
                           font=("Segoe UI", 14, "bold"), fg="#ccd6f6", bg="#0f1419")
categories_header.pack(pady=(10, 5))

# Create main container for buttons with improved layout
main_container = tk.Frame(root, bg="#0f1419")
main_container.pack(fill="both", expand=True, padx=20, pady=(0, 20))

# Create a frame for the canvas and scrollbar
canvas_frame = tk.Frame(main_container, bg="#1a1d2a", bd=1, relief=tk.SOLID)
canvas_frame.pack(fill="both", expand=True)

# Create a canvas and scrollbar with improved styling
canvas = tk.Canvas(canvas_frame, bg="#1a1d2a", highlightthickness=0, bd=0)
scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview, style="Custom.Vertical.TScrollbar")
scrollable_frame = tk.Frame(canvas, bg="#1a1d2a")

# Configure the canvas scrolling
def configure_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_configure(event):
    # Update the scrollable frame width to match canvas width
    canvas.itemconfig(canvas_window, width=event.width)

scrollable_frame.bind("<Configure>", configure_scroll_region)
canvas.bind("<Configure>", on_canvas_configure)

canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Enable mouse wheel scrolling
def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def bind_mousewheel(event):
    canvas.bind_all("<MouseWheel>", on_mousewheel)

def unbind_mousewheel(event):
    canvas.unbind_all("<MouseWheel>")

canvas.bind('<Enter>', bind_mousewheel)
canvas.bind('<Leave>', unbind_mousewheel)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Add buttons to scrollable_frame with improved styling
buttons = []
colors = [
    "#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4", "#feca57", 
    "#ff9ff3", "#54a0ff", "#5f27cd", "#00d2d3"
]

hover_colors = [
    "#ff5252", "#26a69a", "#2196f3", "#66bb6a", "#ffc107",
    "#e91e63", "#3f51b5", "#673ab7", "#009688"
]

# Create a grid of buttons with better spacing
for i, cat in enumerate(CATEGORIES):
    btn = tk.Button(scrollable_frame, 
                    text=cat.replace("_", " ").title(), 
                    width=18, 
                    height=3,
                    font=("Segoe UI", 11, "bold"), 
                    bg=colors[i], 
                    fg="white",
                    activebackground=hover_colors[i], 
                    activeforeground="white",
                    relief=tk.FLAT,
                    bd=0,
                    cursor="hand2",
                    command=lambda c=cat: categorize(c))
    
    # Add hover effects
    def on_enter(event, btn=btn, color=hover_colors[i]):
        btn.config(bg=color)
    
    def on_leave(event, btn=btn, color=colors[i]):
        btn.config(bg=color)
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    # Grid layout with better spacing
    row = i // 3
    col = i % 3
    btn.grid(row=row, column=col, padx=15, pady=12, sticky="ew")
    buttons.append(btn)

# Configure grid weights for responsive design
for i in range(3):
    scrollable_frame.grid_columnconfigure(i, weight=1)

# Add some padding to the scrollable frame
scrollable_frame.configure(padx=20, pady=20)

# Keyboard shortcuts
def on_key_press(event):
    key = event.char.lower()
    if key.isdigit():
        index = int(key) - 1
        if 0 <= index < len(CATEGORIES):
            categorize(CATEGORIES[index])

root.bind('<KeyPress>', on_key_press)
root.focus_set()

# Add keyboard shortcuts info
shortcuts_frame = tk.Frame(root, bg="#0f1419")
shortcuts_frame.pack(fill="x", padx=20, pady=(0, 10))

shortcuts_label = tk.Label(shortcuts_frame, 
                          text="💡 Tip: Use number keys 1-9 for quick categorization",
                          font=("Segoe UI", 10), fg="#8892b0", bg="#0f1419")
shortcuts_label.pack()

# Start with first image
load_image()

# Center the window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# Run app
root.mainloop()
