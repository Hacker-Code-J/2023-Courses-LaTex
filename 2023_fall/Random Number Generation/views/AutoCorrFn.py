import numpy as np
import matplotlib.pyplot as plt

# Define a sample N-periodic sequence
N = 5  # Period of the sequence
s = np.array([0, 1, 0, 1, 1])  # A sample binary sequence

# Define the autocorrelation function
def autocorrelation(sequence, t):
    N = len(sequence)
    return (1/N) * np.sum((2*sequence - 1) * (2*np.roll(sequence, -t) - 1))

# Calculate the autocorrelation for each t
t_values = np.arange(N)
C_t = np.array([autocorrelation(s, t) for t in t_values])

# Plotting
plt.figure(figsize=(10, 5))
plt.stem(t_values, C_t, basefmt=" ")
plt.title('Autocorrelation Function of a N-Periodic Sequence')
plt.xlabel('t')
plt.ylabel('C(t)')
plt.grid(True)
plt.ylim(min(C_t) - 1, max(C_t) + 1)
plt.xticks(t_values)
plt.show()