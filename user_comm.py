import tkinter as tk
from tkinter import ttk
from data_processor import *

def start_gui(data):

    window = tk.Tk()

    window.title("Youtube Data Analyzer")
    window.geometry("640x360")
    window.attributes("-topmost", True)
    window.after(100, lambda: window.attributes("-topmost", False))

    title = tk.Label(window, text="Welcome to the Video Data Analyzer", font=("Arial", 16))
    title.pack(pady=20)

    label = tk.Label(window, text="Click for total unique videos.", font=("Arial", 12))
    label.pack(pady=20)

    def show_total_videos():
        total = count_total_videos(data)
        label.config(text=f"Total Unique Videos: {total}")

    total_button = tk.Button(window, text="Show Total Unique Videos", command=show_total_videos, width=30)
    total_button.pack(pady=20)

    window.mainloop()