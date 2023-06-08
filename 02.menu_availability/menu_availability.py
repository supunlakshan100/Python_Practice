# menu = ['chicken brest', 'chicken nuggets', 'chicken leg peace']
# eat = str(input('What do you want ? :'))
# if eat in menu:
#     print('Available !')

# else:
#     print('Out of our menu !')


import tkinter as tk

def check_availability():
    menu = ['chicken breast', 'chicken nuggets', 'chicken leg piece']
    eat = entry.get()
    if eat in menu:
        result_label.config(text='Available!')
    else:
        result_label.config(text='Out of our menu!')

# Create the main window
window = tk.Tk()
window.title("Menu Availability")
window.geometry("300x150")

# Create and position the GUI elements
label = tk.Label(window, text="What do you want?")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

check_button = tk.Button(window, text="Check Availability", command=check_availability)
check_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

# Start the main GUI loop
window.mainloop()