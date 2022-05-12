#!python3

import os
import sys
import fnmatch

PATHS = [
    "/Volumes/Discworld/nexus/library/readings/",
    "/Users/Matt/unsorted/",
]

def main():
    # Interpret command line arguments
    if not (args := sys.argv[1:]):
        print("usage: rd <query string>", file=sys.stderr)
        sys.exit(1)
    
    # Perform search
    # TODO: smarter queries? fuzzy finding, etc.?
    pattern = " ".join(args) + "*"
    matches = list(find_files(pattern, *PATHS))
    print("found", len(matches), "matches")

    # Display results
    for index, match in enumerate(matches):
        file = os.path.basename(match)
        print(f"{index:x} {file[:60]}")
    if not matches:
        print("sorry, bye!")
        sys.exit(2)

    # Offer to open some results
    to_open = input("open? ")
    for index_str in to_open.split():
        if index_str.endswith("d"):
            # open containing directory
            index = int(index_str[:-1], base=16)
            open_file(os.path.dirname(matches[index]))
        else:
            index = int(index_str, base=16)
            open_file(matches[index])


def open_file(path):
    os.system(f'open "{path}"')


def find_files(pattern, *paths):
    # TODO: Wrap find if this becomes too slow
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if fnmatch.fnmatch(filename, pattern):
                    yield os.path.join(dirpath,filename)


if __name__ == "__main__":
    main()
