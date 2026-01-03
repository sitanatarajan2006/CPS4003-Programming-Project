# Keep only the latest trending video entry based on the trending date this removes duplicates
def clean_data(data):

    clean = {}

    for row in data:
        video_id = row["video_id"]

        if video_id not in clean:
            clean[video_id] = row
        else:
            if row["trending_date"] > clean[video_id]["trending_date"]:
                clean[video_id] = row
    return list(clean.values())



# Count total unique videos in the dataset
def count_total_videos(data):

    clean = clean_data(data)

    return len(clean)


# Get unique videos per unique category
def unique_categories(data):

    clean = clean_data(data)

    category_count = {}
    for row in clean:
        category = row["category_id"]
        if category not in category_count:
            category_count[category] = 1
        else:
            category_count[category] += 1
    return category_count


# Find one video by video_id or title, will always return the latest trending entry
def find_video(data, search_value):

    clean = clean_data(data)
    for row in clean:
        if row["video_id"] == search_value or row["title"] == search_value:
            return row
    return None


# Get top 10 videos by views and sort in descending order from most views to least
def top_views(data):

    clean = clean_data(data)

    sorted_views = sorted(clean, key=lambda row: int(row["views"]), reverse=True)
    return sorted_views[:10]


# Get top 10 videos by likes and sort in descending order from most likes to least
def top_likes(data):

    clean = clean_data(data)

    sorted_likes = sorted(clean, key=lambda row: int(row["likes"]), reverse=True)
    return sorted_likes[:10]


# Get top 10 videos by comments and sort in descending order from most comments to least
def top_comments(data):

    clean = clean_data(data)

    sorted_comments = sorted(clean, key=lambda row: int(row["comment_count"]), reverse=True)
    return sorted_comments[:10]


# Get top 10 videos by an engagement metric (views + likes + comments) and sort in descending order from most to least
def top_engagement(data):

    clean = clean_data(data)

    sorted_engagement = sorted(clean, key=lambda row: int(row["views"]) + int(row["likes"]) + int(row["comment_count"]), reverse=True)
    return sorted_engagement[:10]