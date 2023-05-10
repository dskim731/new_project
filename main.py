import numpy as np

# Define the total population and the number of people that identify as each religion
total_population = 7_900_000_000
num_christians = 2_500_000_000
num_muslims = 1_900_000_000
num_hindus = 1_200_000_000
num_buddhists = 535_000_000
num_sikhs = 30_000_000
num_jews = 14_000_000

# Create a NumPy array with the number of people in each religion
religion_population = np.array(
    [num_christians, num_muslims, num_hindus, num_buddhists, num_sikhs, num_jews])

# Calculate the percentage of people in each religion
religion_percentages = religion_population / total_population * 100

# Print the results
print("Religion Percentages:")
print("Christians: {:.2f}%".format(religion_percentages[0]))
print("Muslims: {:.2f}%".format(religion_percentages[1]))
print("Hindus: {:.2f}%".format(religion_percentages[2]))
print("Buddhists: {:.2f}%".format(religion_percentages[3]))
print("Sikhs: {:.2f}%".format(religion_percentages[4]))
print("Jews: {:.2f}%".format(religion_percentages[5]))
