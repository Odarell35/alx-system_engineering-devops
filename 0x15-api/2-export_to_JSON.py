#!/usr/bin/python3

"""script to export data in the JSON format."""

import json
import requests
import sys


if __name__ == "__main__":

    session = requests.Session()

    _id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
            .format(_id)

    emp_id = session.get(base_url)
    emp_name = session.get(user_url)

    json_results = emp_id.json()
    usernam = emp_name.json()['username']

    Tasks = []
    new_dict = {}

    for employees in json_results:
        Tasks.append(
            {
                "task": employees.get('title'),
                "completed": employees.get('completed'),
                "username": new_dict,
            })
    new_dict[_id] = Tasks

    filename = _id + ".json"
    with open(filename, 'w') as f:
        json.dump(new_dict, f)
