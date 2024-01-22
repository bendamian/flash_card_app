import tkinter as tk
import pandas as pd
import random as ra

BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.title("Flashy")
window.minsize()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Read the cvs file
with open("data/french_words.csv", 'r') as data_cvs:
    df = pd.read_csv(data_cvs)
    js = df.to_json(orient='records')
    print(js)






# widgets
right_b = tk.PhotoImage(file="images/right.png",con)
wrong_b = tk.PhotoImage(file="images/wrong.png")
front = tk.PhotoImage(file='images/card_front.png')
back = tk.PhotoImage(file='images/card_back.png')

canvas = tk.Canvas(width=800, height=526, bg="white", highlightthickness=0, )
canvas.create_image(400, 263, image=front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 260, text="Title", font=("Ariel", 60, "bold"))
right = tk.Button(window, image=right_b, height=100, width=100, pady=10, padx=10)
wrong = tk.Button(window, image=wrong_b, height=100, pady=10, padx=10)
# define a grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=5)
window.rowconfigure(1, weight=1)

canvas.grid(row=0, column=0, columnspan=2)
right.grid(row=1, column=1, sticky='NEWS' )
wrong.grid(row=1, column=0, sticky='NEWS')






window.mainloop()
