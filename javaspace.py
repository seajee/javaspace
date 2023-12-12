#!/usr/bin/env python3

import sys
import os
import re

JAVA_REGEX = "\s*public\s+static\s+void\s+main\s*\(\s*String\s*\[\]\s+args\s*\)\s*"
CPP_REGEX = "\s*int\s+main\s*\(\s*\)\s*"

JAVA_ENTRYPOINT = "\npublic static void main(String[] args)\n"
CPP_ENTRYPOINT = "\nint main()\n"

def main():
    if len(sys.argv) < 3:
        print("Javaspace compiler")
        print("ERROR: Not enough arguments")
        print("Usage: javaspace java/cpp <filepath>")
        exit(1)

    option = sys.argv[1]
    input_file = sys.argv[2]

    if option != "java" and option != "cpp":
        print("ERROR: Invalid option: " + option)
        exit(1)

    output_file = os.path.splitext(input_file)[0] + "." + option

    buffer = ""

    with open(input_file, "r") as f:
        buffer = f.read()

    if option == "java":
        buffer = re.sub(CPP_REGEX, JAVA_ENTRYPOINT, buffer)
    else:
        buffer = re.sub(JAVA_REGEX, CPP_ENTRYPOINT, buffer)

    with open(output_file, "w") as f:
        f.write(buffer)

if __name__ == "__main__":
    main()
