def count_total_videos(data):
    return len(data)



def unique_categories(data):
    category_count = {}
    for row in data:
        category = row["category_id"]
        if category in category_count:
            category_count[category] = category_count[category] + 1
        else:
            category_count[category] = 1
    return category_count

def find_video(data, search_value):
    # Find one video by video_id or title

    for row in data:
        if row["video_id"] == search_value or row["title"] == search_value:
            return row

    return None