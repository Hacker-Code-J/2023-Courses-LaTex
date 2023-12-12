import matplotlib.pyplot as plt
import numpy as np

def visualize_run_conditions(n, k, i):
    """
    Visualizes the conditions for a run of length k starting at position i in a binary sequence of length n.

    :param n: Total length of the binary sequence.
    :param k: Length of the run.
    :param i: Starting position of the run.
    """
    # Create a random binary sequence of length n
    sequence = np.random.randint(0, 2, n)

    # Adjust the sequence to meet the run conditions
    sequence[i-1:i-1+k] = np.random.randint(0, 2) # Same bits for the run
    if i > 1:
        sequence[i-2] = 1 - sequence[i-1] # Different bit before the run
    if i+k <= n:
        sequence[i+k-1] = 1 - sequence[i+k-2] # Different bit after the run

    # Visualization
    plt.figure(figsize=(10, 2))
    plt.plot(sequence, 'o-', color='black')
    
    # Highlight the run
    plt.plot(range(i-1, i-1+k), sequence[i-1:i-1+k], 'o-', color='red', label='Run of length k')
    
    # Annotations for the bits before and after the run
    if i > 1:
        plt.text(i-2, sequence[i-2], f'Bit before\nposition {i}', verticalalignment='bottom', horizontalalignment='center')
    if i+k <= n:
        plt.text(i+k-1, sequence[i+k-1], 'Bit after\nthe run', verticalalignment='bottom', horizontalalignment='center')

    # Setting plot details
    plt.xticks(range(n), [f'{j+1}' for j in range(n)])
    plt.yticks([0, 1], ['0', '1'])
    plt.xlabel('Position in Sequence')
    plt.ylabel('Bit Value')
    # plt.title(f'Binary Sequence Visualization for a Run of Length {k}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example parameters
n = 30  # Length of the binary sequence
k = 7   # Length of the run
i = 4   # Starting position of the run

visualize_run_conditions(n, k, i)
