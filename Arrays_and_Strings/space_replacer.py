import sys


space_replace_value = "%20"


# Tests if two strings are permutations of one another
def main():
    args = sys.argv
    word = " ".join(args[1:])
    print(word)

    replaced_string = _string_replacer(word, space_replace_value)
    print(replaced_string)


def _string_replacer(word, space_replacer):
    return word.replace(" ", space_replacer)


if __name__ == "__main__":
    main()
