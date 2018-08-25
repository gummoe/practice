import sys


# Tests if two strings are permutations of one another
def main():
    args = sys.argv
    word1 = args[1]
    word2 = args[2]
    print(word1)
    print(word2)

    if len(word1) != len(word2):
        print(False)

    are_permutations = _test_permutation(word1, word2)
    print(are_permutations)


def _test_permutation(word1, word2):
    for char in word1:
        if char not in word2:
            return False
    return True


if __name__ == "__main__":
    main()
