import os
import sys
from pathlib import Path


def reverse_file(in_file):
    size = 2 ** 10  # we consider that we can have big files, so we will take chunks of 1 MB at a time
    if not Path(in_file).is_file():
        print(in_file + " doesn't exist")
        return

    with open(in_file, 'rb') as fin, open(in_file + '.out', 'wb') as fout:
        fin.seek(0, os.SEEK_END)  # move to the end of file

        for pos in reversed(range(0, fin.tell(), size)):
            fin.seek(pos, os.SEEK_SET)
            fout.write(fin.read(size)[::-1])

    print(in_file + " processed")


def main(argv):
    if len(sys.argv) == 1:
        print("Please give input files")
        return

    if str(sys.argv[1]).lower() == "-h":
        print("python binary_reverse.py file1 [file2, ...]")
        return

    for i in range(1, len(sys.argv)):
        reverse_file(argv[i])

if __name__ == "__main__":
   main(sys.argv)