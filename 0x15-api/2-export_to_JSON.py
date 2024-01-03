#!/usr/bin/python3
"""export to CSV"""
import csv
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """MEHTOD TO EXPORT"""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('username')

    # Fetch todo list
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Prepare data for JSON export
    user_tasks = []
    for task in todo_data:
        user_tasks.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': employee_name
        })

    # Export to JSON
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump({employee_id: user_tasks}, jsonfile)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
