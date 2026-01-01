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

def get_top_10_by_total_engagement(data):
    # Rank videos using views + likes + comments

    def score(row):
        views = int(row["views"])
        likes = int(row["likes"])
        comments = int(row["comment_count"])
        return views + likes + comments

    sorted_videos = sorted(data, key=score, reverse=True)
    return sorted_videos[:10]


def get_top_10_by_views(data):
    # Rank videos by views only

    def key_func(row):
        return int(row["views"])

    sorted_videos = sorted(data, key=key_func, reverse=True)
    return sorted_videos[:10]


def get_top_10_by_likes(data):
    # Rank videos by likes only

    def key_func(row):
        return int(row["likes"])

    sorted_videos = sorted(data, key=key_func, reverse=True)
    return sorted_videos[:10]


def get_top_10_by_comments(data):
    # Rank videos by comments only

    def key_func(row):
        return int(row["comment_count"])

    sorted_videos = sorted(data, key=key_func, reverse=True)
    return sorted_videos[:10]