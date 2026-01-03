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

