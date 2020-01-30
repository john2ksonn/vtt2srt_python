#!/usr/bin/python
from sys import stdin
import re

def convert(source):
    counter = 1
    # match for the timestamp, an arrow and the other timestamp
    # also match opional padding between the timestamps and the arrow
    timing_regex = '([\d\:\.]{12,})\s*-->\s*([\d\:\.]{12,})'

    for line in source:
        line = line.strip()
        matches = re.findall(timing_regex, line)
        if len(matches) != 0:
            print(counter)
            counter+=1
            print(line.replace('.', ','))
            res = readUntilLine(source, '\n')
            print(res)

def readUntilLine(source, delimiter):
    result = ""
    for line in source:
        if (line == delimiter):
            return result
        result += line
    return result

if __name__ == '__main__':
    convert(stdin)

