"""Develop a Map Reduce program that mines weather data and displays appropriate messages indicating the weather conditions of the day."""

with open('weather.txt', 'w') as f:
    f.write("""2024-04-01,Sunny
2024-04-01,Rainy
2024-04-01,Sunny
2024-04-02,Cloudy
2024-04-02,Cloudy
2024-04-02,Rainy
2024-04-03,Sunny
""")

print("weather.txt file created.")


def mapper(line):
    date, condition = line.strip().split(',')
    return (date, condition)


def reducer(date, conditions):
    condition_counts = {}

    for condition in conditions:
        if condition in condition_counts:
            condition_counts[condition] += 1
        else:
            condition_counts[condition] = 1

    most_frequent_condition = max(condition_counts, key=condition_counts.get)

    return (date, most_frequent_condition)


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    mapped_data = [mapper(line) for line in lines]

    grouped_data = {}

    for date, condition in mapped_data:
        if date in grouped_data:
            grouped_data[date].append(condition)
        else:
            grouped_data[date] = [condition]

    reduced_data = {
        date: reducer(date, conditions)
        for date, conditions in grouped_data.items()
    }

    for date, (date_key, condition) in reduced_data.items():
        print(f"Weather on {date_key}: {condition}")


main('weather.txt')