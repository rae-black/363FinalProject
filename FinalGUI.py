import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from InteractionsSorting import quick_sort
from CSV_sorting import FishPost, fish_post_objects
import csv
from csv import reader
import wget as wget
import pandas

path = "C:/Users/raybo/OneDrive/Documents/School/Comp 363/images/fish.csv"

root = tk.Tk()
root.geometry("800x600")
root. resizable(1, 1)
root.title("FISH")

canvas = Canvas(root)
scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)
frame = Frame(canvas)

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


photos = []

def displayImage(img):
    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)
    newPhoto_label = Label(frame, image=photo)
    newPhoto_label.pack()

fish_photos = []
image_sources = [fish.imageURL for fish in fish_post_objects]
print(image_sources)
for image in image_sources:
    wget.download(image, fish_photos)
    print(image)

for file in fish_photos:
    try:
        print(file)
        displayImage(file)
    except:
        print("fucking failed")
        pass

button_icon = tk.PhotoImage(file='C:/Users/raybo/OneDrive/Pictures/download.png')

Button(
    frame,
    text="sort by interactions",
    command=quick_sort(fish_post_objects)
).pack(
    ipadx=5,
    ipady=5,
    expand=True
)
Button(
    frame,
    text="sort by date")
.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


canvas.create_window(0, 0, anchor='nw', window=frame)
canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')

root.mainloop()
