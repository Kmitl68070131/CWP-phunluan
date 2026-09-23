#!/usr/bin/env python3
import sys
import re

def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print("none")
        return

    keyword = args[0]
    text = args[1]

    matches = re.findall(re.escape(keyword), text)

    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))

if __name__ == "__main__":
    main()

