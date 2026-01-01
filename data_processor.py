def count_total_videos(data):
    return len(data)



def count_videos_per_category(data):
    category_count = {}
    for row in data:
        category = row["category_id"]
        if category in category_count:
            category_count[category] = category_count[category] + 1
        else:
            category_count[category] = 1
    return category_count