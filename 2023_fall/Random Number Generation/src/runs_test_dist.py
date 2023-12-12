import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import sqrt

# Recalculating the necessary values for the 50-bit sequence
bit_sequence = "011000000100011010011000100110001101001010001011000"
n = len(bit_sequence)
n_0 = bit_sequence.count('0')
n_1 = bit_sequence.count('1')

# Calculate the proportion pi
pi = n_1 / n

# Function to calculate V_n using the provided formula
def calculate_V_n(sequence):
    V_n = 1  # Starts with 1 because the first bit is the start of the first run
    for k in range(len(sequence) - 1):
        # r(k) = 1 if ε_k != ε_{k+1}, else 0
        if sequence[k] != sequence[k + 1]:
            V_n += 1
    return V_n
# Define a large n to approximate infinity
n_large = 1000000

# Generate a range of V_n values around the expected value (2n * pi * (1 - pi))
expected_V_n = 2 * n_large * pi * (1 - pi)
V_n_values = np.linspace(expected_V_n - 1*sqrt(n_large), expected_V_n + 1*sqrt(n_large), 10)

# Calculate the test statistics for these V_n values
test_statistics = (V_n_values - 2 * n_large * pi * (1 - pi)) / (sqrt(2 * n_large) * pi * (1 - pi))

# Generate the standard normal distribution for comparison
x = np.linspace(-10, 10, 100)
standard_normal = norm.pdf(x, 0, 1)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(test_statistics, norm.pdf(test_statistics), label='Test Statistic Distribution (Large n)')
plt.plot(x, standard_normal, label='Standard Normal Distribution', linestyle='dashed')
plt.title('Comparison of Test Statistic Distribution and Standard Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()