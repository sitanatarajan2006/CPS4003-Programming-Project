import matplotlib.pyplot as plt
def plot_category_distribution(category_counts, save=False):
    categories = list(category_counts.keys())
    counts = list(category_counts.values())

    plt.figure()
    plt.pie(counts, labels=categories)
    plt.title("Video Distribution by Category")

    if save:
        plt.savefig("category_distribution.png", bbox_inches="tight")

    plt.show()
    categories = list(category_counts.keys())
    counts = list(category_counts.values())
    plt.figure()
    plt.pie(counts, labels=categories)
    plt.title("Video Distribution by Category")
    plt.show()
def plot_views_histogram(data):
    views = []
    for row in data:

        views.append(int(row["views"]) / 1_000_000)
    plt.figure()
    plt.hist(views, bins=20)
    plt.title("Distribution of Video Views")
    plt.xlabel("Number of Views (millions)")
    plt.ylabel("Number of Videos")

    plt.show()
