import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.title("Flashy")
window.minsize(width=600, height=500)
window.config(bg=BACKGROUND_COLOR)

# widgets
right_b = tk.PhotoImage(file="images/right.png")
wrong_b = tk.PhotoImage(file="images/wrong.png")
front = tk.PhotoImage(file='images/card_front.png')
back = tk.PhotoImage(file='images/card_back.png')

canvas = tk.Canvas(width=220, height=224, bg="white", highlightthickness=0, )
right = tk.Button(window, image=right_b, height=100, width=100, pady=10, padx=10)
wrong = tk.Button(window, image=wrong_b, height=100, pady=10, padx=10)
# define a grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=5)
window.rowconfigure(1, weight=1)

right.grid(row=2, column=1, sticky='NEWS')
wrong.grid(row=2, column=0, sticky='NEWS')
canvas.grid(row=0, column=0, columnspan=2)
window.mainloop()
