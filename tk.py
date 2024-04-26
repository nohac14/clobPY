import tkinter as tk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()
root.title("Scrollable Grid")

# Width of each title label
font_size = 15

# Create a frame for titles (no scrollbar)
title_frame = tk.Frame(root)
title_frame.pack(side=tk.TOP, fill=tk.X)

# Add titles to the title frame
titles = ['    ticker', '        trader', '       side', '          limit', '      quantity', '       filled', '       status']
for title in titles:
    title_label = tk.Label(title_frame, text=title, font=('Arial', font_size), pady=5)
    title_label.pack(side=tk.LEFT)

# Create a canvas for the scrollable columns
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar to the canvas
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the columns
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add columns to the frame
columns = []
for i in range(7):
    column = tk.Frame(frame, bd=1, relief=tk.SOLID)
    column.grid(row=0, column=i, sticky="nsew")
    columns.append(column)

    # Fill each column with some text
    text = "\n".join([f"Item {j+1}" for j in range(20)])  # 20 example items
    content_label = tk.Label(column, text=text, padx=10, pady=10)
    content_label.pack()

# Configure the grid to expand with the window
for i in range(7):
    frame.grid_columnconfigure(i, weight=1)

# Bind the canvas to the scrollbar and configure scrolling
canvas.bind("<Configure>", on_configure)

root.mainloop()
