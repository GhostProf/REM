import argparse
import os
import csv

####################################
# This script is designed to read the first two columns of a csv file.
# The first column will be the names of authors
# The second name will be the names of works
# It will compile all of the works and authors together, then search the titles of all
# of the directories within the given directory and try to match them to a combination of the names of the works.
# This code will process any command line arguments the script is given and makes sure they are input.
# Copyright 2015 Mike Poirier, poirier.mike@live.com


# Handles the command line arguments passed in. 
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', dest='file', type=str, required=True, action='store', help='CSV file to parse.')
parser.add_argument('-t', '--target', dest='path', type=str, action='store', required=True, help='Directory for the script to cross reference.')
parser.add_argument('-o', '--output', dest='output', default='output.txt', type=str, action='store', help='File you want to output the results.')
parser.add_argument('-d', '--delemiter', dest='delimiter', default='\t', type=str, action='store', help='Separator in your csv file. Defaults to a tab.')
args = parser.parse_args()

# Checks to see if the file name provided exists
if not os.path.isfile(args.file):
    print ("Error. File '" + args.file + "' does not exist.")
    exit(1)

# Checks to see if the target directory exists
if not os.path.isdir(args.path):
    print("Error. '" + args.path + "' is not a valid path")
    exit(1)

# Pulls the contents of the csv file into memory.
with open(args.file, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=args.delimiter)
    author = {}
    for row in reader:
            if str(row[0]) not in author.keys():
                author[str(row[0])] = [str(row[1]).lower()]
            else:
                author[str(row[0])].append(str(row[1]).lower())
#print (author)

# Pulls the contents of the target into memory.
items = os.listdir(args.path)

for i in range(len(items)):
    items[i] = items[i]

# Bulk of the algorithm
for key in author.keys():
    works = author[key]
    for work in works:
        words = work.split("_,- ")

        for item in items:
            match = True
            for word in words:
                if word not in item.lower():
                    match = False
            if match:
                with open(args.output, "a") as f:
                    f.write(key + ": " + item)


