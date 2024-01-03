#!/usr/bin/python3
import csv
import json
import requests
import sys

def get_employee_todo_progress(employee_id):
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
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]

    # Export to CSV
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['employee_id', 'employee_name', 'task_status', 'task_title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            writer.writerow({
                'employee_id': employee_id,
                'employee_name': employee_name,
                'task_status':'True' if task['completed'] else 'False',
                'task_title': task['title']
                })


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
