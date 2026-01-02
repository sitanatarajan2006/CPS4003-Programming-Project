import tkinter as tk
from data_processor import *

def start_gui(data):

    app = tk.Tk()
    app.title("Youtube Data Analyser")
    app.geometry("1600x900")
    app.attributes("-topmost", True)
    app.after(100, lambda: app.attributes("-topmost", False))


    left_frame = tk.Frame(app, bg="#003a6b")
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    right_frame = tk.Frame(app, bg="#003a6b")
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    menu_area = tk.Frame(left_frame, width=500, bg="#3776a1")
    menu_area.pack(fill=tk.Y, expand=True, padx=5, pady=5)
    menu_area.pack_propagate(False)

    content_area = tk.Frame(right_frame, bg="#5293bb")
    content_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    content_label = tk.Label(content_area, text="Select an option from the menu", bg="#89cff1", fg="#003a6b", font=("Courier New", 16, "bold"), padx=20, pady=20, wraplength=900, justify="left")
    content_label.pack(pady=20, padx=20, anchor="nw")



    def clear_content():
        for widget in content_area.winfo_children():
            widget.destroy()
    
    
    def home():
        clear_content()
        home_label = tk.Label(content_area, text="Select an option from the menu", bg="#89cff1", fg="#003a6b", font=("Courier New", 16, "bold"), padx=20, pady=20, wraplength=900, justify="left")
        home_label.pack(pady=20, padx=20, anchor="nw")
    home_button = tk.Button(menu_area, text="Home", command=home, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=25, height=2, relief="flat")
    home_button.pack(pady=20, padx=20)
    
    app.mainloop()