# This is the main program file that integrates all modules and provides a user interface.
# It allows users to load data, view statistics, search for videos, see trending videos, visualize data, and export data.

# Importing all necessary modules
from data_loader import *
from data_processor import *
from visualisation import *
from data_exporter import *

# Loading data from CSV file into the program and lets the user know data is loaded
data = load_data("youtube_trending_videos.csv")
print("\nData loaded successfully.")

# Shows trending submenu options
def show_trending_menu():
    print("\n--- TRENDING VIDEOS MENU ---")
    print("1. Top 10 by views")
    print("2. Top 10 by likes")
    print("3. Top 10 by comments")
    print("4. Top 10 by engagement")
    print("0. Back to main menu")

# Lists rank and video information
def top_10(videos):
    for i, video in enumerate(videos, start=1):
        print("\nRank:", i)
        print("Title:", video["title"])
        print("Views:", video["views"])
        print("Likes:", video["likes"])
        print("Comments:", video["comment_count"])

# Shows histogram submenu options
def show_hisogram_menu():
    print("\n--- HISTOGRAM MENU ---")
    print("1. Views")
    print("2. Likes")
    print("3. Comments")
    print("4. Engagement")
    print("0. Back to main menu")

# Main program loop
while True:
    print("\n--- MAIN MENU ---")
    print("1.Show total number of videos")
    print("2.Show number of videos per category")
    print("3.Find video by ID or title")
    print("4.Show top 10 trending videos")
    print("5.Show pie chart")
    print("6.Show histogram")
    print("0.Exit")
    choice = input("Enter your choice: ")

    # If the user chooses 1 then show total number of videos
    if choice == '1':
        print("\nTotal number of videos:", count_total_videos(data))

    # If the user chooses 2 then show number of videos per category
    elif choice == '2':
        print("\nNumber of videos per category:")
        category_counts = unique_categories(data)
        for category in category_counts:
            print(category, "->", category_counts[category])

    # If the user chooses 3 then find video by ID or title and export to JSON if the user wants to, the JSON will be named after the channel title
    elif choice == "3":
        search_value = input("\nEnter the video's ID or title: ")
        video = find_video(data, search_value)

        if video:
            print("\nVideo found:")
            for key in video:
                print(key, ":", video[key])
            save = input("\nExport this video to JSON? (y/n): ")
            if save.lower() == "y":
                filename = f"{video['channel_title']}.json"
                export_json(video, filename)
        else:
            print("\nVideo not found.")

    # If the user chooses 4 then show trending submenu
    elif choice == "4":

        while True:
            show_trending_menu()
            sub_choice = input("\nChoose trending option: ")

            # If the user chooses 1 in the trending submenu then show top 10 by views and export to CSV if the user wants to
            if sub_choice == "1":
                videos = top_views(data)
                top_10(videos)
                save = input("\nExport to CSV? (y/n): ")
                if save.lower() == "y":
                    export_csv(videos, "top_10_by_views.csv")

            # If the user chooses 2 in the trending submenu then show top 10 by likes and export to CSV if the user wants to
            elif sub_choice == "2":
                videos = top_likes(data)
                top_10(videos)
                save = input("\nExport to CSV? (y/n): ")
                if save.lower() == "y":
                    export_csv(videos, "top_10_by_likes.csv")

            # If the user chooses 3 in the trending submenu then show top 10 by comments and export to CSV if the user wants to
            elif sub_choice == "3":
                videos = top_comments(data)
                top_10(videos)
                save = input("\nExport to CSV? (y/n): ")
                if save.lower() == "y":
                    export_csv(videos, "top_10_by_comments.csv")

            # If the user chooses 4 in the trending submenu then show top 10 by engagement and export to CSV if the user wants to
            elif sub_choice == "4":
                videos = top_engagement(data)
                top_10(videos)
                save = input("\nExport to CSV? (y/n): ")
                if save.lower() == "y":
                    export_csv(videos, "top_10_by_engagement.csv")

            # If the user chooses 0 or types "exit" in lower or upper case then break the trending submenu loop and go back to main menu
            elif sub_choice == "0" or sub_choice.lower() == "exit":
                break

            # This is to handle anything other than the valid options in the trending submenu
            else:
                print("\nInvalid trending option.")

    # if the user chooses 5 then show pie chart of video distribution by category
    elif choice == "5":
        category_counts = unique_categories(data)
        plot_category_distribution(category_counts, save=True)

    # If the user chooses 6 then show histogram submenu loop
    elif choice == "6":
         while True:
            show_hisogram_menu()
            histo_choice = input("\nChoose histogram option: ")

            # If the user chooses 1 then show views histogram
            if histo_choice == "1":
                plot_views_histogram(data)

            # If the user chooses 2 then show likes histogram
            elif histo_choice == "2":
                plot_likes_histogram(data)

            # If the user chooses 3 then show comments histogram
            elif histo_choice == "3":
                plot_comments_histogram(data)

            # If the user chooses 4 then show engagement histogram
            elif histo_choice == "4":
                plot_engagement_histogram(data)

            # If the user chooses 0 or types "exit" in lower or upper case then break the histogram submenu loop and go back to main menu
            elif histo_choice == "0" or histo_choice.lower() == "exit":
                break

            # This is to handle anything other than the valid options in the histogram submenu
            else:
                print("\nInvalid histogram option.")

    # If the user chooses 0 or types "exit" in lower or upper case then exit the program with a message
    elif choice == "0" or choice.lower() == "exit":
        print("\nExiting program.")
        break

    # This is to handle anything other than the valid options in the main menu
    else:
        print("\nInvalid option. Please try again.")