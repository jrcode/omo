#!/usr/bin/env python3

##############################
#Name: nOmO
#Author: Jose R. Hernandez
#Version:0.2
##############################

import sys
import csv
import time
import argparse


#variable to hold the parser
parser = argparse.ArgumentParser(description='Parse The Manage Sign-Ups CSV File',prog='Names Open mic Ordinaire - nOmO')

#file argument
parser.add_argument('-f', type=argparse.FileType('r'), required=True, metavar='sign-up-sheets-2017.csv',help='CSV File')

#variable to hold arguments
args = parser.parse_args()

#hold csv content
contents = csv.reader(args.f)

#variable to hold list
data = []

# fill the data with the contents of the csv file
for row in contents:
    data.append(row)

#variable to hold second list
names = []

#fill names array with all names
for i in range(1,25):
    names.append(str(data[i][7]) + str(" ") + str(data[i][8]))

#remove In Person Sign-Up from names array
for j in range(0,24):
    if names[j] == "Reserved For In Person Sign-up":
        names[j] = " "


#write stuff to file
with open(time.strftime("names_%m%d%Y.csv"), 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["Open Mic Ordinaire"])
    spamwriter.writerow(["Date:", time.strftime("%A, %B %d, %Y")])
    spamwriter.writerow(["Spot", "Name"])
    for k in range(0,24):
        spamwriter.writerow(["Spot %s" % (k + 1), names[k]])

    for l in range(1,5):
        spamwriter.writerow(["Walk-in Spot %s" % (l)])
