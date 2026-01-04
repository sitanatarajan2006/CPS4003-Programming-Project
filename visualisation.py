#import matplotlib for data visualisation
import matplotlib.pyplot as plt

# Creating a generic function to create histogram plots, that can be reused for views, likes and comments, avioding code duplication
def create_histogram(values, title, xlabel):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(values, bins=20)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Number of Videos")
    fig.tight_layout()
    return fig

# creating pie chart function for category distribution, this can be imported and used in user_comm.py
def create_pie(category_counts, title = "Video Distribution by Category"):
    categories = list(category_counts.keys())
    counts = list(category_counts.values())

    fig, ax = plt.subplots(figsize=(10, 6))
    wedges, _ = ax.pie(counts, startangle=90)

    legend_labels = [
        f"Category {cat}: ({count})"
        for cat, count in zip(categories, counts)
    ]
    ax.legend(wedges, legend_labels, title="Categories ID", loc="center left", bbox_to_anchor=(1, 0.5))
    ax.set_title(title)
    fig.tight_layout()
    return fig

