import matplotlib.pyplot as plt
import numpy as np

def information_weight(prob_distributions):
    fig, ax = plt.subplots(figsize=(12, 7))

    # Colors for different distributions
    colors = ['skyblue', 'lightgreen', 'salmon']
    labels = ['Uniform', 'Uneven', 'Skewed']

    # Iterate over each distribution
    for i, probabilities in enumerate(prob_distributions):
        num_probs = len(probabilities)
        x_vals = np.arange(num_probs) + (0.25 * i)  # Offset each bar for clarity

        # Calculate p_i * -log2(p_i) for each probability
        values = probabilities * -np.log2(probabilities)

        # Calculate the weighted average (entropy)
        weighted_avg = np.sum(values)

        # Bar chart for p_i * -log2(p_i) of each probability in the distribution
        bars = ax.bar(x_vals, values, width=0.25, color=colors[i], label=f'{labels[i]} Distribution')

        # Annotating the probability values
        for bar, p in zip(bars, probabilities):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{p:.2f}', ha='center', va='bottom')
  
        # Line for the weighted average
        ax.plot(x_vals, [weighted_avg] * num_probs, color=colors[i], linestyle='--', label=f'{labels[i]} Avg: {weighted_avg:.2f}')

    ax.set_xlabel('Probabilities')
    ax.set_ylabel('p_i * -log2(p_i)')
    ax.set_title('p_i * -log2(p_i) and Weighted Average for Different Probability Distributions')
    ax.legend()

    # Adjust x-ticks to show probability labels
    prob_labels = [f'p{j+1}' for j in range(num_probs)]
    ax.set_xticks(np.arange(num_probs) + 0.5)
    ax.set_xticklabels(prob_labels)

    plt.show()

# Example of different probability distributions
# prob_distributions = [
#     np.array([0.2, 0.2, 0.2, 0.2, 0.2]),  # Uniform distribution
#     np.array([0.4, 0.3, 0.2, 0.05, 0.05]), # Uneven distribution
#     np.array([0.5, 0.25, 0.15, 0.05, 0.05]) # More skewed distribution
# ]
prob_distributions = [
    np.array([0.5, 0.5]),  # Uniform distribution
    np.array([0.6, 0.4]), # Uneven distribution
    np.array([0.2, 0.8]) # More skewed distribution
]

# Generate the combined plot for the three distributions
information_weight(prob_distributions)