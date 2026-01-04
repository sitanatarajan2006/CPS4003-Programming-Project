# importing tkinter for GUI, matplotlib for visualisations and various modules for data processing and exporting
import tkinter as tk
from tkinter import ttk
from data_processor import *
from data_exporter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from visualisation import *

def start_gui(data):

    # Setting up the main application window's attributes like size, title, opening and exit behavior
    app = tk.Tk()
    app.title("Youtube Data Analyser")
    app.geometry("1600x1000")
    app.attributes("-topmost", True)
    app.after(100, lambda: app.attributes("-topmost", False))

    def on_exit():
        plt.close('all')
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", on_exit)

    # ttk styling is used for better appearance of tabs
    style = ttk.Style()
    style.configure("TNotebook.Tab", width=45, font=("Courier New", 12, "bold"))
    style.map("TNotebook.Tab", foreground=[("selected", "#5293bb")])

    #laying out the basic app framing with a menu area on the left and content area on the right
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


    # Function to clear content area, and close any open matplotlib plots
    def clear_content():
        for widget in content_area.winfo_children():
            widget.destroy()
        plt.close('all')

    # Home button to reset content area to initial state
    def home():
        clear_content()
        home_label = tk.Label(content_area, text="Select an option from the menu", bg="#89cff1", fg="#003a6b", font=("Courier New", 16), padx=20, pady=20, wraplength=900, justify="left")
        home_label.pack(pady=20, padx=20, anchor="nw")
    home_button = tk.Button(menu_area, text="Home", command=home, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=25, height=2, relief="flat")
    home_button.pack(pady=20, padx=20)

    # Show total unique videos and channels and setting up a button in menu area
    def show_videos():
        clear_content()
        total_videos = count_total_videos(data)
        total_channels = count_total_channels(data)
        text = f"Total number of unique channels: {total_channels}\n\nTotal number of unique videos: {total_videos}"
        videos_label = tk.Label(content_area, text=text, bg="#89cff1", fg="#003a6b", font=("Courier New", 16), padx=20, pady=20, justify="left")
        videos_label.pack(pady=20, padx=20, anchor="nw")
    videos_button = tk.Button(menu_area, text="Show Videos", command=show_videos, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=20, height=1)
    videos_button.pack(pady=20, padx=20)

    # Show categories with list and pie chart by utilising tabs to switch views. Also setting up a button in menu area
    def show_categories():
        clear_content()

        category_frame = tk.Frame(content_area, bg="#5293bb")
        category_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(category_frame, text="Videos per Category", font=("Courier New", 18, "bold"), fg="#000000", bg="#5caae9", padx=20, pady=10)
        title_label.pack(anchor="nw", padx=50, pady=(20, 10))

        notebook = ttk.Notebook(category_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=40, pady=(0, 20))

        tab_list = ttk.Frame(notebook)
        tab_pie = ttk.Frame(notebook)

        notebook.add(tab_list, text="List View")
        notebook.add(tab_pie, text="Pie Chart")

        category_counts = unique_categories(data)

        list_container = tk.Frame(tab_list, bg="#003a6b")
        list_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        list_text = tk.Text(list_container, font=("Courier New", 14, "bold"), bg="#89cff1", fg="#003a6b", wrap=tk.NONE)
        list_text.pack(fill=tk.BOTH, expand=True)

        for category in sorted(category_counts, key=int):
            list_text.insert(
                tk.END,
                f"Category ID {int(category):>3}     :     "
                f"Video Count {category_counts[category]}\n"
            )

        list_text.config(state=tk.DISABLED)

        pie_container = tk.Frame(tab_pie, bg="#003a6b")
        pie_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        fig = create_pie(category_counts)

        canvas = FigureCanvasTkAgg(fig, master=pie_container)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)

        plt.close(fig)
    categories_button = tk.Button(menu_area, text="Show Categories", command=show_categories, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=20, height=1)
    categories_button.pack(pady=20, padx=20)

    # Find video by ID or title and setting up a button in menu area
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

        # Export found video to  JSON file
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

    # Show top 10 videos by views, likes or comments with tabs to switch views. Also setting up a button in menu area
    # The view utilises a scrollable text area for better navigation.
    def show_top_10():
        clear_content()

        top10_frame = tk.Frame(content_area, bg="#5293bb")
        top10_frame.pack(fill=tk.BOTH, expand=True)

        notebook = ttk.Notebook(top10_frame)
        notebook.pack(fill=tk.X, padx=40, pady=(20, 10))

        tab_views = ttk.Frame(notebook)
        tab_likes = ttk.Frame(notebook)
        tab_comments = ttk.Frame(notebook)

        notebook.add(tab_views, text="Views")
        notebook.add(tab_likes, text="Likes")
        notebook.add(tab_comments, text="Comments")

        title_row = tk.Frame(top10_frame, bg="#5293bb")
        title_row.pack(fill=tk.X, padx=50, pady=(10, 5))

        title_label = tk.Label(title_row, text="Top 10 Trending Videos by Views", font=("Courier New", 18, "bold"), fg="#000000", bg="#5caae9", padx=20, pady=10)
        title_label.pack(side=tk.LEFT)

        export_button = tk.Button(title_row, text="Export", font=("Courier New", 12, "bold"), fg="#000000", bg="#5caae9", padx=15, pady=8)
        export_button.pack(side=tk.RIGHT)

        text_frame = tk.Frame(top10_frame, bg ="#003a6b")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        content_text = tk.Text(text_frame, font=("Courier New", 14, "bold"), wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="#89cff1", fg="#003a6b")
        content_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=content_text.yview)
        content_text.config(state=tk.DISABLED)

        # Function to render top 10 videos in the text area
        def render(videos, title_text):
            title_label.config(text=title_text)
            text = ""
            for i, video in enumerate(videos, start=1):
                text += (
                    f"{i:>2}. {video['title']}\n"
                    f"    Views         : {video['views']}\n"
                    f"    Likes         : {video['likes']}\n"
                    f"    Comments      : {video['comment_count']}\n"
                )

            content_text.config(state=tk.NORMAL)
            content_text.delete(1.0, tk.END)
            content_text.insert(tk.END, text)
            content_text.config(state=tk.DISABLED)
            content_text.yview_moveto(0)

        render(top_views(data), "Top 10 Trending Videos by Views")

        def export_top_10():
            selected = notebook.index(notebook.select())

            if selected == 0:
                videos = top_views(data)
                filename = "top_10_by_views.csv"
            elif selected == 1:
                videos = top_likes(data)
                filename = "top_10_by_likes.csv"
            else:
                videos = top_comments(data)
                filename = "top_10_by_comments.csv"

            export_csv(videos, filename)

        export_button.config(command=export_top_10)

        def on_tab_change(event):
            selected = notebook.index(notebook.select())

            if selected == 0:
                render(top_views(data), "Top 10 Trending Videos by Views")
            elif selected == 1:
                render(top_likes(data), "Top 10 Trending Videos by Likes")
            elif selected == 2:
                render(top_comments(data), "Top 10 Trending Videos by Comments")


        notebook.bind("<<NotebookTabChanged>>", on_tab_change)

    top_10_button = tk.Button(menu_area, text="Show Top 10", command=show_top_10, bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=20, height=1)
    top_10_button.pack(pady=20, padx=20)

    # Show histograms for views, likes and comments with tabs to switch views. Also setting up a button in menu area
    def show_histograms(content_area, data):

        for widget in content_area.winfo_children():
            widget.destroy()

        container = tk.Frame(content_area, bg="#5293bb")
        container.pack(fill=tk.BOTH, expand=True)

        notebook = ttk.Notebook(container)
        notebook.pack(fill=tk.X, padx=40, pady=(20, 10))

        tab_views = ttk.Frame(notebook)
        tab_likes = ttk.Frame(notebook)
        tab_comments = ttk.Frame(notebook)

        notebook.add(tab_views, text="Views")
        notebook.add(tab_likes, text="Likes")
        notebook.add(tab_comments, text="Comments")

        title_label = tk.Label(container, text="Histogram", font=("Courier New", 18, "bold"), bg="#5caae9", padx=20, pady=10)
        title_label.pack(anchor="nw", padx=50, pady=(10, 5))

        plot_frame = tk.Frame(container, bg="#003a6b")
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=10)

        def render(values, title, xlabel):
            for widget in plot_frame.winfo_children():
                widget.destroy()

            plt.close('all')

            fig = create_histogram(values, title, xlabel)
            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        render(
            [v / 1_000_000 for v in views_list(data)],
            "Distribution of Video Views",
            "Views (millions)"
        )
        title_label.config(text="Distribution of Video Views")

        def on_tab_change(event):
            idx = notebook.index(notebook.select())

            if idx == 0:
                render(
                    [v / 1_000_000 for v in views_list(data)],
                    "Distribution of Video Views",
                    "Views (millions)"
                )
                title_label.config(text="Distribution of Video Views")

            elif idx == 1:
                render(
                    [v / 10_000 for v in likes_list(data)],
                    "Distribution of Video Likes",
                    "Likes (ten-thousands)"
                )
                title_label.config(text="Distribution of Video Likes")

            elif idx == 2:
                render(
                    [v / 10_000 for v in comments_list(data)],
                    "Distribution of Video Comments",
                    "Comments (ten-thousands)"
                )
                title_label.config(text="Distribution of Video Comments")


        notebook.bind("<<NotebookTabChanged>>", on_tab_change)
    histogram_button = tk.Button(menu_area, text="Show Histograms", command=lambda: show_histograms(content_area, data), bg="#89cff1", fg="#003a6b", font=("Courier New", 14, "bold"), width=20, height=1)
    histogram_button.pack(pady=20, padx=20)
    app.mainloop()