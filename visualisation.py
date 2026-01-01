import matplotlib.pyplot as plt


def plot_category_distribution(category_counts, save=False):
    categories = list(category_counts.keys())
    counts = list(category_counts.values())

    plt.figure()
    plt.pie(counts, labels=categories)
    plt.title("Video Distribution by Category")
    plt.show()

