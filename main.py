from data_loader import load_data
from data_processor import(
    count_total_videos,
    find_video,
    unique_categories,
    get_top_10_by_views,
    get_top_10_by_likes,
    get_top_10_by_comments,
    get_top_10_by_total_engagement
)
from visualisation import plot_category_distribution
from visualisation import plot_views_histogram
from visualisation import plot_likes_histogram
from visualisation import plot_comments_histogram

#loading data from CSV file and printing number of rows
data = load_data("youtube_trending_videos.csv")
print("Data loaded successfully.")

# Shows trending submenu options
def show_trending_menu():
    print("\n--- TRENDING VIDEOS MENU ---")
    print("1. Top 10 by views")
    print("2. Top 10 by likes")
    print("3. Top 10 by comments")
    print("4. Top 10 by engagement (views + likes + comments)")
    print("0. Back to main menu")

# Lists rank and video information
def display_top_10(videos):
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
    print("0. Back to main menu")

while True:

    print("1.Show total number of videos")
    print("2. Show number of videos per category")
    print("3.Find video by ID or title")
    print("4.Show top 10 trending videos")
    print("5.Show pie chart")
    print("6.Show histogram")
    print("0.Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Total number of videos:", count_total_videos(data))

    elif choice == '2':
        print("Number of videos per category:")
        category_counts = unique_categories(data)
        for category in category_counts:
            print(category, "->", category_counts[category])

    elif choice == "3":
        search_value = input("Enter the video's ID or title: ")
        video = find_video(data, search_value)

        if video:
            print("\nVideo found:")
            for key in video:
                print(key, ":", video[key])
        else:
            print("Video not found.")

    elif choice == "4":

        while True:
            show_trending_menu()
            sub_choice = input("Choose trending option: ")

            if sub_choice == "1":
                top_10 = get_top_10_by_views(data)
                display_top_10(top_10)

            elif sub_choice == "2":
                top_10 = get_top_10_by_likes(data)
                display_top_10(top_10)

            elif sub_choice == "3":
                top_10 = get_top_10_by_comments(data)
                display_top_10(top_10)

            elif sub_choice == "4":
                top_10 = get_top_10_by_total_engagement(data)
                display_top_10(top_10)

            elif sub_choice == "0" or sub_choice.lower() == "exit":
                break

            else:
                print("Invalid trending option.")

    elif choice == "5":
        category_counts = unique_categories(data)
        plot_category_distribution(category_counts, save=True)

    elif choice == "6":
         while True:
            show_hisogram_menu()
            histo_choice = input("Choose histogram option: ")

            if histo_choice == "1":
                plot_views_histogram(data)

            elif histo_choice == "2":
                plot_likes_histogram(data)

            elif histo_choice == "3":
                plot_comments_histogram(data)

            elif histo_choice == "0" or histo_choice.lower() == "exit":
                break

    elif choice == "0" or choice.lower() == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.")
