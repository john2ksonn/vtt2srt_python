#!/usr/bin/python
from __future__ import print_function
from sys import stdin
from os.path import join

def convert():
    counter = 1
    cue_flag = False
    cue = ''

    #iterate through every line
    for line in stdin:
        if isTimingLine(line) and not cue_flag:
            cue_flag = True
            print(counter)
            counter += 1
            print(cleanTimingLine(line), end = '')
        elif cue_flag:
            if isTimingLine(line) or str(line).startswith('\n'):
                print(cleanCueLine(cue), end = '')
                cue_flag = False
                print('\n', end = '')
                cue = ''
            else:
                cue += line


def isTimingLine(line):
    #return True if the line starts like a timing line and conatins an '-->'
    return (line[0].isdigit() and line[1].isdigit()
    and line[2] == ':' and line[5] == ':'
    and '-->' in line)

#removes any extra stuff that is not required
def cleanTimingLine(line):
    clean_line = ""
    for ch in line.strip():
        #in case of an alphabetic character retun
        if ch.isalpha():
            break
        clean_line += ch
    return clean_line.replace(".", ",") + '\n'

#removes the '\n' in the cue, removes any tags
#and returns the cue as single line with a '\n' at the end
def cleanCueLine(lines):
    tag_flag = False
    line = lines#.replace('\n', ' ')
    clean_line = ""
    for ch in line:
        if ch == '<':
            tag_flag = True
        elif ch == '>':
            tag_flag = False
        elif not tag_flag:
            clean_line += ch
    return clean_line.strip('\n') + '\n'

if __name__ == '__main__':
    convert()


