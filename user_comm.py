import tkinter as tk
from data_processor import *

def start_gui(data):

    app = tk.Tk()
    app.title("Youtube Data Analyser")
    app.geometry("1600x900")
    app.attributes("-topmost", True)
    app.after(100, lambda: app.attributes("-topmost", False))


    left_frame = tk.Frame(app, width=500, bg="#0f5875")
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    right_frame = tk.Frame(app, bg="#2d83a5")
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


    app.mainloop()