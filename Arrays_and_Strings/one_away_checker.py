import sys


"""
3 types of edits are possible:
1. Inserting a character
2. Removing a character
3. Replacing a character

Given two strings, see if they are no more than 1 edit away

Note: doesn't quite work - this will fail for many situations where the order of the 
letters changed significantly, but the count of each letter remains the same 
i.e. 'pale' and 'alep'
"""


def main():
    args = sys.argv
    word1 = args[1]
    word2 = args[2]
    print(word1)
    print(word2)

    if abs(len(word1) - len(word2)) > 1:
        print(False)
        exit(1)

    word1_counts = _get_letter_counts(word1)
    word2_counts = _get_letter_counts(word2)

    are_one_edit_away = _are_one_edit_away(word1_counts, word2_counts)
    print(are_one_edit_away)


def _are_one_edit_away(word1_counts, word2_counts):
    change_count = 0
    for key, value in word1_counts.items():
        if value != word2_counts.get(key):
            change_count += 1
            if change_count > 1:
                return False
    return True


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
