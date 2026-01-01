from data_loader import load_data

#loading data from CSV file and printing number of rows
data = load_data("youtube_trending_videos.csv")
print("Data loaded successfully.")
print("Total videos loaded:", len(data))