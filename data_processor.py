def clean_data(data):
    # Keep only the latest trending entry for each video
    clean = {}
    for row in data:
        video_id = row["video_id"]

        if video_id not in clean:
            clean[video_id] = row
        else:
            if row["trending_date"] > clean[video_id]["trending_date"]:
                clean[video_id] = row
    return list(clean.values())



def count_total_videos(data):
    clean = clean_data(data)
    return len(clean)


def unique_categories(data):
    # Get unique videos per category
    clean = clean_data(data)
    category_count = {}
    for row in clean:
        category = row["category_id"]
        if category not in category_count:
            category_count[category] = 1
        else:
            category_count[category] += 1
    return category_count

def find_video(data, search_value):
    # Find one video by video_id or title
    clean = clean_data(data)
    for row in clean:
        if row["video_id"] == search_value or row["title"] == search_value:
            return row
    return None


def top_views(data):

    clean = clean_data(data)

    sorted_views = sorted(clean, key=lambda row: int(row["views"]), reverse=True)
    return sorted_views[:10]


def top_likes(data):

    clean = clean_data(data)
    sorted_likes = sorted(clean, key=lambda row: int(row["likes"]), reverse=True)
    return sorted_likes[:10]


def top_comments(data):

    clean = clean_data(data)
    sorted_comments = sorted(clean, key=lambda row: int(row["comment_count"]), reverse=True)
    return sorted_comments[:10]


def top_engagement(data):

    clean = clean_data(data)
    sorted_engagement = sorted(clean, key=lambda row: int(row["views"]) + int(row["likes"]) + int(row["comment_count"]), reverse=True)
    return sorted_engagement[:10]