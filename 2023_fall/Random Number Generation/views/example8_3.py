import matplotlib.pyplot as plt
import numpy as np

# Values, probabilities, and entropy calculations
values = ['a', 'b', 'c', 'd']
probabilities = [1/2, 1/4, 1/8, 1/8]
entropy_terms = [-p * np.log2(p) for p in probabilities]
total_entropy = sum(entropy_terms)

# Setting up a figure with two subplots
fig, ax1 = plt.subplots(figsize=(12, 6))

# Colors for each bar and point
colors = ['blue', 'green', 'red', 'purple']

# First subplot: Bar chart for probabilities
bars = ax1.bar(values, probabilities, color=colors)
ax1.set_xlabel('Values')
ax1.set_ylabel('Probability', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Adding a second y-axis to the same subplot for entropy
ax2 = ax1.twinx()  
ax2.plot(values, entropy_terms, color='darkorange', marker='o', linestyle='dashed', linewidth=2, markersize=10)
ax2.set_ylabel('Entropy Contribution', color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')

# Annotating each bar and point for clarity
for bar, color, entropy_term in zip(bars, colors, entropy_terms):
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval, f'{yval}', va='bottom', ha='center', color=color)
    ax2.text(bar.get_x() + bar.get_width()/2, entropy_term, f'{entropy_term:.2f}', va='bottom', ha='center', color='darkorange')

# Annotating total entropy on the plot
plt.title('Probability Distribution and Entropy Calculation of Variable X')
plt.figtext(0.5, 0.01, f'Total Entropy: H(X) = {total_entropy:.2f} bits', ha='center', fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})

plt.show()