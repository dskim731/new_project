import numpy as np

# Define the total population and the number of people that identify as each religion worldwide
total_population = 7_900_000_000
num_christians = 2_500_000_000
num_muslims = 1_900_000_000
num_hindus = 1_200_000_000
num_buddhists = 535_000_000
num_sikhs = 30_000_000
num_jews = 14_000_000

# Define the percentage of people in each country that identify as each religion
# These numbers are based on estimates from various sources and may not be accurate for all countries
country_religion_percentages = np.array([
    [33.2, 22.5, 2.3, 6.9, 0.3, 0.1],   # China
    [33.4, 1.8, 0.7, 0.2, 0.0, 0.1],   # United States
    [97.0, 1.0, 0.1, 0.1, 0.0, 0.0],   # Saudi Arabia
    [79.5, 14.4, 2.3, 1.7, 0.0, 0.1],  # India
    [96.2, 0.4, 0.2, 0.2, 0.0, 0.0]    # Israel
])

# Calculate the number of people in each country that identify as each religion
country_population = country_religion_percentages / 100 * total_population
num_country_religions = np.sum(country_population, axis=0)

# Create a NumPy array with the number of people in each religion worldwide and in each country
worldwide_population = np.array([num_christians, num_muslims, num_hindus, num_buddhists, num_sikhs, num_jews])
all_religions_population = np.vstack((worldwide_population, num_country_religions))

# Calculate the percentage of people in each religion worldwide and in each country
all_religions_percentages = all_religions_population / total_population * 100

# Print the results for the worldwide stats
print("Worldwide Religion Percentages:")
print("Christians: {:.2f}%".format(all_religions_percentages[0, 0]))
print("Muslims: {:.2f}%".format(all_religions_percentages[0, 1]))
print("Hindus: {:.2f}%".format(all_religions_percentages[0, 2]))
print("Buddhists: {:.2f}%".format(all_religions_percentages[0, 3]))
print("Sikhs: {:.2f}%".format(all_religions_percentages[0, 4]))
print("Jews: {:.2f}%".format(all_religions_percentages[0, 5]))
print()

# Print the results for the country-specific stats
print("Country-Specific Religion Percentages:")
for i in range(country_religion_percentages.shape[0]):
    print("Country {}: ".format(i+1))
    print("Christians: {:.2f}%".format(country_religion_percentages[i, 0]))
    print("
