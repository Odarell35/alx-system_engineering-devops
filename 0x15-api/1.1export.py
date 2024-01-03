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

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")
    print(f"\t{employee_name}: {len(done_tasks)} tasks completed out of {total_tasks}")

    # Export to CSV
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': 'True' if task['completed'] else 'False',
                'TASK_TITLE': task['title']
            })

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
