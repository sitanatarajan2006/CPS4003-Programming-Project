from data_loader import load_data
from data_processor import(
    count_total_videos,
    find_video,
    unique_categories
)

#loading data from CSV file and printing number of rows
data = load_data("youtube_trending_videos.csv")
print("Data loaded successfully.")

while True:

    print("1.Show total number of videos")
    print("2. Show number of videos per category")
    print("3.Find video by ID or title")
    print("4.Show top 10 trending videos")
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

                save = input("Export to CSV? (y/n): ")
                if save.lower() == "y":
                    export_top_10_to_csv(top_10, "top_10_by_views.csv")

            elif sub_choice == "2":
                top_10 = get_top_10_by_likes(data)
                display_top_10(top_10)

                save = input("Export to CSV? (y/n): ")
                if save.lower() == "y":
                    export_top_10_to_csv(top_10, "top_10_by_likes.csv")

            elif sub_choice == "3":
                top_10 = get_top_10_by_comments(data)
                display_top_10(top_10)

                save = input("Export to CSV? (y/n): ")
                if save.lower() == "y":
                    export_top_10_to_csv(top_10, "top_10_by_comments.csv")

            elif sub_choice == "4":
                top_10 = get_top_10_by_total_engagement(data)
                display_top_10(top_10)

                save = input("Export to CSV? (y/n): ")
                if save.lower() == "y":
                    export_top_10_to_csv(top_10, "top_10_by_engagement.csv")

            elif sub_choice == "0":
                break

            else:
                print("Invalid trending option.")

    elif choice == "0" or choice.lower() == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.")
