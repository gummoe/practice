import sys


# Tests if a string is a palindrome
def main():
    args = sys.argv
    string = "".join(args[1:])
    print(string)

    is_palindrome = _is_palindrome(string, 0, len(string) - 1)
    print(is_palindrome)


def _is_palindrome(string, start, end):
    if start > end:
        return True
    if string[start] == string[end]:
        return _is_palindrome(string, start + 1, end - 1)
    else:
        return False


if __name__ == "__main__":
    main()
