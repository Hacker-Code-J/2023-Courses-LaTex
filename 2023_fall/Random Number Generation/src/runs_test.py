from scipy.special import erfc
from math import sqrt

# # Recalculating the necessary values for the 50-bit sequence
bit_sequence = "01100000010001101001100010011000110010100010111000"
n = len(bit_sequence)
n_1 = bit_sequence.count('1')

# Calculate the proportion pi
pi = n_1 / n

# Function to calculate V_n
def calculate_V_n(sequence):
    V_n = 1  # Starts with 1
    for k  in range(len(sequence) - 1):
        # r(k) = 1 if ε_k != ε_{k+1}, else 0
        if sequence[k] != sequence[k + 1]:
            V_n += 1
    return V_n

# Calculate V_50 for the given sequence
V_50 = calculate_V_n(bit_sequence)

# Recalculate the P-Value
p_value = erfc(abs(V_50 - 2 * n * pi * (1 - pi)) / (sqrt(2 * n) * pi * (1 - pi)))

print(n, n_1, pi, V_50, p_value)
