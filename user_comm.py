import tkinter as tk
from tkinter import ttk
from data_processor import *
from data_exporter import *

def start_gui(data):

    app = tk.Tk()
    app.title("Youtube Data Analyser")
    app.geometry("1600x1000")
    app.attributes("-topmost", True)
    app.after(100, lambda: app.attributes("-topmost", False))

    style = ttk.Style()
    style.configure("TNotebook.Tab", width=45, font=("Courier New", 12, "bold"))
    style.map("TNotebook.Tab", foreground=[("selected", "#5293bb")])


    left_frame = tk.Frame(app, bg="#003a6b")
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    right_frame = tk.Frame(app, bg="#003a6b")
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    
    menu_area = tk.Frame(left_frame, width=400, bg="#3776a1")
    menu_area.pack(fill=tk.Y, expand=True, padx=5, pady=5)
    menu_area.pack_propagate(False)

    content_area = tk.Frame(right_frame, bg="#5293bb")
    content_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    content_label = tk.Label(content_area, text="Select an option from the menu", bg="#89cff1", fg="#003a6b", font=("Courier New", 16), padx=20, pady=20, wraplength=900, justify="left")
    content_label.pack(pady=20, padx=20, anchor="nw")



    def clear_content():
        for widget in content_area.winfo_children():
            widget.destroy()


    def home():
        clear_content()
        home_label = tk.Label(content_area, text="Select an option from the menu", bg="#89cff1", fg="#003a6b", font=("Courier New", 16), padx=20, pady=20, wraplength=900, justify="left")
        home_label.pack(pady=20, padx=20, anchor="nw")
    home_button = tk.Button(menu_area, text="Home", command=home, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=25, height=2, relief="flat")
    home_button.pack(pady=20, padx=20)


    def show_videos():
        clear_content()
        total = count_total_videos(data)
        videos_label = tk.Label(content_area, text=f"Total number of unique videos: {total}", bg="#89cff1", fg="#003a6b", font=("Courier New", 16), padx=20, pady=20, justify="left")
        videos_label.pack(pady=20, padx=20, anchor="nw")
    videos_button = tk.Button(menu_area, text="Show Videos", command=show_videos, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=20, height=1)
    videos_button.pack(pady=20, padx=20)


    def show_categories():
        clear_content()
        category_counts = unique_categories(data)
        categories_text = "Number of videos per category:\n\n"
        for category in sorted(category_counts, key=int):
            categories_text += (
                f"Category ID {int(category):>3}     :     "
                f"Video count {category_counts[category]}\n"
                )
        categories_label = tk.Label(content_area, text=categories_text, bg="#89cff1", fg="#003a6b", font=("Courier New", 16), padx=20, pady=20, justify="left")
        categories_label.pack(pady=20, padx=20, anchor="nw")
    categories_button = tk.Button(menu_area, text="Show Categories", command=show_categories, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=20, height=1)
    categories_button.pack(pady=20, padx=20)



    def find_videos():
        clear_content()
        title = tk.Label(content_area, text="Find Video by ID or Title", bg="#89cff1", fg="#003a6b", font=("Courier New", 16), padx=20, pady=20, justify="left")
        title.pack(pady=10, padx=20, anchor="nw")

        found_video = {"data": None}

        def search():
            query = search_entry.get().strip()
            video = find_video(data, query)
            if video:
                found_video["data"] = video
                output = "Video found:\n\n"
                for key in video:
                    output += f"{key} : {video[key]}\n"
                result_label.config(text=output)
            else:
                found_video["data"] = None
                result_label.config(text="Video not found.")


        def export():
            if found_video["data"]:
                video = found_video["data"]
                filename = f"{video['channel_title']}.json"
                export_json(video, filename)
            else:
                result_label.config(text="No video to export.")

        search_row = tk.Frame(content_area, bg="#89cff1")
        search_row.pack(pady=10, padx=20, anchor="nw")

        search_entry = tk.Entry(search_row, width=68, font=("Courier New", 14))
        search_entry.pack(side=tk.LEFT, padx=(10,10))
        search_entry.focus()

        search_button = tk.Button(search_row, text="Search", command=search, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=15, height=1)
        search_button.pack(side=tk.LEFT)
        search_button.bind("<Return>", lambda event: search())

        export_button = tk.Button(search_row, text="Export to JSON", command=export, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=15, height=1)
        export_button.pack(side=tk.LEFT, padx=(10,0))

        result_label = tk.Label(content_area, text="Search result will appear here", bg="#89cff1", fg="#003a6b", font=("Courier New", 14), padx=20, pady=20, justify="left", wraplength=900)
        result_label.pack(pady=10, padx=20, anchor="nw")

    find_button = tk.Button(menu_area, text="Find Video", command=find_videos, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=20, height=1)
    find_button.pack(pady=20, padx=20)


    def show_top_10():
        clear_content()
        
        top10_frame = tk.Frame(content_area, bg="#5293bb")
        top10_frame.pack(fill=tk.BOTH, expand=True)
        
        # ---- NOTEBOOK (TABS AT TOP) ----
        notebook = ttk.Notebook(top10_frame)
        notebook.pack(fill=tk.X, padx=40, pady=(20, 10))

        tab_views = ttk.Frame(notebook)
        tab_likes = ttk.Frame(notebook)
        tab_comments = ttk.Frame(notebook)
        tab_engagement = ttk.Frame(notebook)

        notebook.add(tab_views, text="Views")
        notebook.add(tab_likes, text="Likes")
        notebook.add(tab_comments, text="Comments")
        notebook.add(tab_engagement, text="Engagement")
        

        # ---- DYNAMIC TITLE ----
        title_label = tk.Label(top10_frame, text="Top 10 Trending Videos by Views", font=("Courier New", 18, "bold"), fg="#000000", bg="#5caae9", padx=20, pady=10)
        title_label.pack(anchor="nw", padx=50, pady=(10, 5))
        
        text_frame = tk.Frame(top10_frame, bg ="#003a6b")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)
    
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        content_text = tk.Text(text_frame, font=("Courier New", 14, "bold"), wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#89cff1", fg="#003a6b")
        content_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=content_text.yview)
        content_text.config(state=tk.DISABLED)


        # ---- HELPER TO RENDER TOP 10 ----
        def render(videos, title_text):
            title_label.config(text=title_text)
            text = ""
            for i, video in enumerate(videos, start=1):
                text += (
                    f"{i:>2}. {video['title']}\n"
                    f"    Views    : {video['views']}\n"
                    f"    Likes    : {video['likes']}\n"
                    f"    Comments : {video['comment_count']}\n\n"
                )

            content_text.config(state=tk.NORMAL)
            content_text.delete(1.0, tk.END)
            content_text.insert(tk.END, text)
            content_text.config(state=tk.DISABLED)
            content_text.yview_moveto(0)

        # ---- INITIAL LOAD (VIEWS) ----
        render(top_views(data), "Top 10 Trending Videos by Views")

        # ---- TAB CHANGE HANDLER ----
        def on_tab_change(event):
            selected = notebook.index(notebook.select())

            if selected == 0:
                render(top_views(data), "Top 10 Trending Videos by Views")
            elif selected == 1:
                render(top_likes(data), "Top 10 Trending Videos by Likes")
            elif selected == 2:
                render(top_comments(data), "Top 10 Trending Videos by Comments")
            elif selected == 3:
                render(top_engagement(data), "Top 10 Trending Videos by Engagement")

        notebook.bind("<<NotebookTabChanged>>", on_tab_change)

    top_10_button = tk.Button(menu_area, text="Show Top 10", command=show_top_10, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=20, height=1)
    top_10_button.pack(pady=20, padx=20)

    app.mainloop()