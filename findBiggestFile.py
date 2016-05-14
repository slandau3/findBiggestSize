#! A program to find the largest specific files inside a general directory.
# findBiggestFile.py
# Created by Slandau3

import os
import time

sizedic = {}
def getSize(path):
    for i in os.listdir(path):
        try:
            pj = os.path.join(path, i)

            sizedic[os.path.getsize(pj)] = pj   # adds the size and path to dictionary

            getSize(pj)
        except Exception as e:
            pass

startTime = time.time()
getSize(r'C:\Users') # change this to any general sub directory of a drive. It should be C:\'Something'
endTime = time.time()

sizeList = (sorted(sizedic, reverse=True)) # gets a list of largest sizes (max -> min)

i = 0
for x in sizeList:
    print('\n')
    print(sizedic[x])
    print(x/1073741824)

    i += 1
    if (i == 10):
        break

print('\nTime to search: %s seconds' % (round(endTime-startTime, 2)))