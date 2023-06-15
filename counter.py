import tkinter as tk
from datetime import datetime
from pynput import keyboard

def on_press(key):
    global counter
    try:
        counter += 1
        label_counter.config(text=counter)
    except AttributeError:
        pass

def update_time():
    current_time = datetime.now() - start_time
    label_time.config(text=str(current_time).split('.')[0])
    window.after(1000, update_time)  # Actualizar cada segundo 

counter = 0
start_time = datetime.now()

window = tk.Tk()
window.title("Contador de caracteres")
window.geometry("100x100")
window.configure(bg="#000000")

label_counter = tk.Label(window, text="0", fg="#00ee00", bg="#000000", font=("Arial", 32))
label_counter.pack()

label_time = tk.Label(window, text="", fg="#00ee00", bg="#000000", font=("Arial", 12))
label_time.pack()

listener = keyboard.Listener(on_press=on_press)
listener.start()

update_time()

window.mainloop()
