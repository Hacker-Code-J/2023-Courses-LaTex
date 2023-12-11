# New given bit string
bit_string = "0110000001000110100110001001100011001010001011100010001110010010000111111011010101000000010110100011"

# Compute total string length
n = len(bit_string)

# Function to count overlapping occurrences of a substring
def count_overlapping(substring, string):
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            count += 1
            start = pos + 1
        else:
            break
    return count

# Counting the number of occurrences of each subsequence again, allowing for overlap
n_00 = count_overlapping('00', bit_string)
n_01 = count_overlapping('01', bit_string)
n_10 = count_overlapping('10', bit_string)
n_11 = count_overlapping('11', bit_string)

# Counting the total number of 0's and 1's again
n0 = bit_string.count('0')
n1 = bit_string.count('1')

# Recalculating the chi-square statistic X2 with the correct string
X2 = (4/(n-1)) * (n_00**2 + n_01**2 + n_10**2 + n_11**2) - (2/n) * (n0**2 + n1**2) + 1

print(n, n_00, n_01, n_10, n_11, n0, n1, X2)