from data_loader import load_data
from data_processor import(
    count_total_videos,
    count_videos_per_category
)

#loading data from CSV file and printing number of rows
data = load_data("youtube_trending_videos.csv")
print("Data loaded successfully.")

while True:

    print("1.Show total number of videos")
    print("0.Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Total number of videos:", count_total_videos(data))
        
    elif choice == "0" or choice.lower() == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Please try again.")
