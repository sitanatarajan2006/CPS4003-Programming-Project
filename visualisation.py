import matplotlib.pyplot as plt


def create_histogram(values, title, xlabel):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(values, bins=20)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Number of Videos")
    fig.tight_layout()
    return fig



def plot_category_distribution(category_counts, save=False):
    categories = list(category_counts.keys())
    counts = list(category_counts.values())

    plt.figure()
    plt.pie(counts, labels=categories)
    plt.title("Video Distribution by Category")
    plt.show()

def plot_views_histogram(data):

    views = []

    for row in data:

        views.append(int(row["views"]) / 1000000)

    plt.figure()
    plt.hist(views, bins=20)
    plt.title("Distribution of Video Views")
    plt.xlabel("Number of Views (millions)")
    plt.ylabel("Number of Videos")
    plt.show()

def plot_likes_histogram(data):

    likes = []

    for row in data:

        likes.append(int(row["likes"]) / 10000)

    plt.figure()
    plt.hist(likes, bins=20)
    plt.title("Distribution of Video Likes")
    plt.xlabel("Number of Likes (ten-thousands)")
    plt.ylabel("Number of Videos")
    plt.show()

def plot_comments_histogram(data):

    comments = []

    for row in data:

        comments.append(int(row["comment_count"]) / 10000)
    plt.figure()
    plt.hist(comments, bins=20)
    plt.title("Distribution of Video Comments")
    plt.xlabel("Number of Comments (ten-thousands)")
    plt.ylabel("Number of Videos")
    plt.show()
