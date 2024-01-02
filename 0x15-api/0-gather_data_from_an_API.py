#!/usr/bin/python3
'''returns information about his/her TODO list progress.
'''
import json
import requests
import sys


def employee_data(_id):
    """
    Get employee data.
    """
    _url = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get(f"{_url}/users/{_id}")
    user_data = user_resp.json()
    _name = user_data.get('name')

    todo_results = requests.get(f"{_url}/todos?userId={_id}")
    todo_data = todo_results.json()

    return _name, todo_data


def display_todo(_name, todo_data):
    """
    Display employee's TODO list.
    """
    t_tasks = len(todo_data)
    c_tasks = sum(task['completed'] for task in todo_data)
    
    print("Employee {} is done with tasks({}/{}):".
          format(_name, c_tasks, t_tasks))

    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    _id = int(sys.argv[1])

    try:
        _name, todo_data = employee_data(_id)
        display_todo(_name, todo_data)
    except requests.RequestException as e:
        print(f"Error: {e}")
