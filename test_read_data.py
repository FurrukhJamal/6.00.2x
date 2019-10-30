# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:10:25 2018

@author: furrukh
"""
import re
rawdata = {}

file = open("testdata.csv", "r")
header = file.readline().strip().split(',')
print(header)

for line in file:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            print(date)
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))
            
            print("year:", year, "month:", month, "day:", day)
            
            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in rawdata:
                rawdata[city] = {}
            if year not in rawdata[city]:
                rawdata[city][year] = {}
            if month not in rawdata[city][year]:
                rawdata[city][year][month] = {}
            rawdata[city][year][month][day] = temperature
            
file.close()

print(rawdata)