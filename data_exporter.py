import csv
import json


def export_top_10_to_csv(videos, filename):
    # Export top 10 videos to a CSV file

    if not videos:
        print("No data to export.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "rank",
            "title",
            "views",
            "likes",
            "comment_count"
        ])

        for index, video in enumerate(videos, start=1):
            writer.writerow([
                index,
                video["title"],
                video["views"],
                video["likes"],
                video["comment_count"]
            ])

    print(f"Exported top 10 videos to {filename}")


def export_video_to_json(video, filename):
    # Export a single selected video to JSON

    if not video:
        print("No video to export.")
        return

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(video, file, indent=4)

    print(f"Exported video to {filename}")
