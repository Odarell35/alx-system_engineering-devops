#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":

    _id = sys.argv[1]
    base_url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
            .format(_id))
    todos_res = requests.get('https://jsonplaceholder.typicode.com/todos')
    name = base_url.json().get('username')

    filecsv = _id + '.csv'
    with open(filecsv, mode='w', newline="") as f:
        write = csv.writer(f, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_ALL, lineterminator='\n')
        for i in todos_res.json():
            if i.get('_id') == int(_id):
                write.writerow([_id, name, str(i.get('completed')),
                            i.get('title')])
