import sys


# Returns an array of numbers in the fibonacci
# series whose sum is the inputted number or next closest
# without going over
# Ex: 4 -> [0, 1, 1, 2]
# Ex: 21 -> [0, 1, 1, 2, 3, 5, 8]
def main():
    args = sys.argv
    num = int(args[1])
    output = recursive_sequence_finder([0, 1], 0, num, 1)
    print(output)


def recursive_sequence_finder(sequence, position, target_num, sequence_sum):
    local_sum = sequence[position] + sequence[position + 1]
    sequence_sum = sequence_sum + local_sum
    if sequence_sum >= target_num:
        return sequence
    else:
        sequence.append(local_sum)
        return recursive_sequence_finder(sequence, position + 1, target_num, sequence_sum)


if __name__ == "__main__":
    main()
