import sys
import json


def main():
    file = open("sample.json")
    data = json.load(file)

    for key, value in data.items():
        print(key, value)


if __name__ == "__main__":
    main()
