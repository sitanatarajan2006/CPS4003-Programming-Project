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

# Count total unique channels in the dataset
def count_total_channels(data):

    clean = clean_data(data)
    channels = set()

    for video in clean:
        channels.add(video["channel_title"])
    return len(channels)

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


def views_list(data):
    clean = clean_data(data)
    return [int(video["views"]) for video in clean]

def likes_list(data):
    clean = clean_data(data)
    return [int(video["likes"]) for video in clean]

def comments_list(data):
    clean = clean_data(data)
    return [int(video["comment_count"]) for video in clean]


def average_engagement(data):

    category_totals = {}
    category_counts = {}

    for video in data:
        category = video["category_id"]
        likes = int(video["likes"])
        dislikes = int(video["dislikes"])
        comments = int(video["comment_count"])

        if category not in category_totals:
            category_totals[category] = {"likes": 0, "dislikes": 0, "comments": 0}
            category_counts[category] = 0

        category_totals[category]["likes"] += likes
        category_totals[category]["dislikes"] += dislikes
        category_totals[category]["comments"] += comments
        category_counts[category] += 1

    averages = {}

    for category in category_totals:
        count = category_counts[category]

        averages[category] = {
            "avg_likes": category_totals[category]["likes"] / count,
            "avg_dislikes": category_totals[category]["dislikes"] / count,
            "avg_comments": category_totals[category]["comments"] / count
        }

    return averages
