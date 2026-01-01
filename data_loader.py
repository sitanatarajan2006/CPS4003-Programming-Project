import csv

# Function to load data from a CSV file and return it as a list of dictionaries
def load_data(filename):
    data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data