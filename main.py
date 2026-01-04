from data_loader import load_data
from user_comm import start_gui

# Main function to load data and start the GUI
def main():
    data = load_data("youtube_trending_videos.csv")
    start_gui(data)

if __name__ == "__main__":
    main()