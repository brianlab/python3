#!/usr/bin/env python

import sys
import pandas as pd
import excel2json
import json

# This function is to convert xlsx file to csv file
my_xls = pd.read_excel('program_info.xlsx', 'Sheet1', index_col=None)
my_xls.to_csv('program_info.csv', encoding='utf-8', index=False)


#This function is to convert xlsx file to JSON file
#https://www.journaldev.com/33335/python-excel-to-json-conversion

excel_data_input = pd.read_excel('program_info.xlsx', sheet_name='Sheet1')

json_string = excel_data_input.to_json(orient='records')

print('Excel Sheet to JSON:\n', json_string)

#Create new JSON file
excel2json.convert_from_file('program_info.xlsx')

#How to read a JSON file in path /data/sftp/MyProgram

#1.Open file
JSON_PATH = '/data/sftp/MyProgram/Sheet1.json'

#Load JSON File to a dictionary
with open(JSON_PATH) as f:
    data = json.load(f)

for i in data:
    print(i)

#3.Close file
f.close()

print(data)
