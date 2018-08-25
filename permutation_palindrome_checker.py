import sys


# Tests if a string is a permutation of a palindrome
# True: 'tact coa' -> 'taco cat', 'atco cta'
def main():
    args = sys.argv
    string = "".join(args[1:])
    print(string)

    letter_counts = _get_letter_counts(string)
    is_permutation_palindrome = _is_permutation_palindrome(letter_counts)
    print(is_permutation_palindrome)


def _is_permutation_palindrome(letter_counts):
    odds = [key for key, value in letter_counts.items() if value % 2 > 0]
    return len(odds) <= 1


def _get_letter_counts(string):
    letter_count = {}
    for char in string:
        if letter_count.get(char):
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1
    return letter_count


if __name__ == "__main__":
    main()
