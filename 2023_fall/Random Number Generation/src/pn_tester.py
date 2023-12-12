def golombs_postulates(sequence):
    N = len(sequence)
    count_1 = sum(sequence)
    count_0 = N - count_1

    # R1: Balance Property
    balance_property = abs(count_1 - count_0) <= 1

    # R2: Run Distribution
    def count_runs(seq):
        runs = {'0': {}, '1': {}}
        current_run = 1
        current_type = seq[0]

        for i in range(1, len(seq)):
            if seq[i] == current_type:
                current_run += 1
            else:
                if current_run in runs[str(current_type)]:
                    runs[str(current_type)][current_run] += 1
                else:
                    runs[str(current_type)][current_run] = 1
                current_run = 1
                current_type = seq[i]

        # Counting the last run
        if current_run in runs[str(current_type)]:
            runs[str(current_type)][current_run] += 1
        else:
            runs[str(current_type)][current_run] = 1

        return runs

    runs = count_runs(sequence)
    total_runs = sum(sum(lengths.values()) for lengths in runs.values())
    run_distribution = True

    # Check the required number of runs for each length
    for l in range(1, len(sequence)):
        required_runs = total_runs / (2**l)
        if required_runs <= 1:
            break
        actual_runs = runs['0'].get(l, 0) + runs['1'].get(l, 0)
        run_distribution &= actual_runs >= required_runs
        run_distribution &= abs(runs['0'].get(l, 0) - runs['1'].get(l, 0)) <= 1
        
    # R3: Autocorrelation Property
    def autocorrelation(seq, t):
        sum_product = 0
        for i in range(N):
            sum_product += (2*seq[i] - 1) * (2*seq[(i+t) % N] - 1)
        return sum_product / N

    autocorrelation_property = True
    for t in range(1, N):
        if autocorrelation(sequence, t) != -1/N:
            autocorrelation_property = False
            break

    return balance_property, run_distribution, autocorrelation_property

# Example sequence
# sequence = [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]

# Problem sequence
sequence = [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1]

print(golombs_postulates(sequence))
