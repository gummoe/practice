
import sys

# Tests if a word contains only unique characters
def main():
	# Get command line args
    args = sys.argv
    word = args[1]
    print(word)

    unique = _test_uniqueness(word)

    if unique:
        print('true')
    else:
        print('false')


def _test_uniqueness(word): 
    chars = []

    for char in word:
        if char in chars:
            return False
        chars.append(char)

    return True

if __name__ == "__main__":
    main()
