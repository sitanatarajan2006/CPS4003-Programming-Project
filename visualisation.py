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

# This function creates a pie chart showing the distribution of videos across different categories
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

# This function creates a line plot showing average trending duration per category over time
def create_line(date_by_category):

    plt.figure(figsize=(10, 6))
    for category, date_values in date_by_category.items():
        dates = sorted(date_values.keys())
        averages = [date_values[date] for date in dates]

        plt.plot(dates, averages, label=f"Category {category}")

    plt.xlabel("Trending Date")
    plt.ylabel("Average Treding Duration (Days)")
    plt.title("Average Trending Duration per Category Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
