#!python3

import os
import sys
import shutil
import fnmatch

PATHS = [
    "/Volumes/Discworld/nexus/library/readings/",
    "/Users/Matt/unsorted/",
]

def main():
    # Interpret command line arguments
    if not (args := sys.argv[1:]):
        print("usage: rd [-r] [-d] <query string>", file=sys.stderr)
        sys.exit(1)
    REM = False
    DIR = False
    while args[0][0] == "-":
        if args[0][1] == "r":
            REM = True
        if args[0][1] == "d":
            DIR = True
        args.pop(0)
    
    # Perform search
    # TODO: smarter queries? fuzzy finding, etc.?
    pattern = " ".join(args) + "*"
    matches = list(find_files(pattern, *PATHS))
    print("found", len(matches), "matches")
    
    # Sort results
    matches = sorted(matches, key=os.path.basename)

    # Display results
    for index, match in enumerate(matches):
        file = os.path.basename(match)
        print(f"{index:d} {file[:60]}")

    # Offer to open some results
    if len(matches) == 0:
        print("sorry, bye!")
        sys.exit(2)
    elif len(matches) == 1:
        # TODO: ALLOW OPEN CONTAINING DIRECTORY
        print("opening", matches[0])
        to_open = ["0"]
    else:
        to_open = input("open? ").split()

    # Open some results
    for index_str in to_open:
        dir = DIR
        rem = REM
        while not index_str[-1].isdigit():
            if index_str.endswith("d"):
                dir = True
            if index_str.endswith("r"):
                rem = True
            index_str = index_str[:-1]
        index = int(index_str)
        if dir:
            open_file(os.path.dirname(matches[index]))
        elif rem:
            push_file(matches[index])
        else:
            open_file(matches[index])

def push_file(src):
    # TODO: Push straight to rem
    dst = os.path.join("/Users/matt/Desktop", os.path.basename(src))
    shutil.copy(src, dst)

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
