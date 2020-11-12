# Script: filecounter.py
# By: Avalyn Jasenn
# Date: Nov 11/2020
# Description: A command-line tool which counts file types and prints out results
# > uses file extensions to determine type of each file(no ext == unknown type)
# Run: Python3 [script name] [-s] [-f] [path/to/files/*] [-t] [listoftypes]
# > counts and displays all file types by default
# Credit: Script modified from .pptx slidecount tool example in 'Building Tools With Python' course by Scott Simpson

import os
import argparse

# Define or gather the options and files to count
parser = argparse.ArgumentParser(description="Count the number of each type of file and return a count")
parser.add_argument("-s", "--summary", help="Generate a summary of files", action="store_true")
parser.add_argument("-f", "--files", help="A list of files to process", type=argparse.FileType("r"), nargs="*")
parser.add_argument("-t", "--types", help="A list of file types to show", nargs="*")  # prints all by default
args = parser.parse_args()

# Declare a dictionary to hold the [file type, count]
filecount = {}

no_ext = 0  # number of files that have no extension
total_count = 0  # number of files successfully typed(by extensions)

# if successfully received file names in arguments -
if args.files:
    # iterate through the files.
    for file in args.files:
        # determine file extension/type
        filename, extension = os.path.splitext(file.name)
        # if has .ext, add file to count
        if len(extension) > 0:
            if extension not in filecount:
                filecount[extension] = 0
            filecount[extension] += 1
            total_count += 1
        else:  # if file has no extension
            no_ext += 1

print("Count\tType")
num_types = len(filecount)  # number of file types

# Iterate through a sorted version of the dictionary and print out each count and type.
if args.types:  # if type args given, only print out those counts
    for typ in sorted(args.types):
        ext = "."+typ
        if ext not in filecount:  # if type was not found, add to dict w/ 0 value
            filecount[ext] = 0
        print("%s\t%s" % (filecount[ext], ext))
else:  # if no type args given, print out all file types found
    for file, count in sorted(filecount.items()):
        print("%s\t%s" % (count, file))

if no_ext > 0:  # print out total count of files w/ no ext as 'unknown'
    print("%s\tunknown" % no_ext)

# If the user has requested a summary, print it.
if args.summary:
    print("- - - - -")
    print("%s total files parsed." % len(args.files))  # total num of files received
    print("%s files identified of %s type(s)." % (total_count, num_types))  # total num files w/ ext & num file types
    if no_ext > 0:
        print("the type of %s file(s) could not be determined" % no_ext)  # total num files w/o ext
