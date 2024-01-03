#!/usr/bin/python3
"""export to CSV"""
import csv
import json
import requests
import sys


def get_employee_todo():
    """MEHTOD TO EXPORT"""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/'

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    todo_all_employees = {}
    
    #fetch each users todo list
    for user in user_data:
        user_id = user['id']
        username = user['username']
        todo_url = f'{base_url}/todos?userId={user_id}'
    
    # Fetch todo list all users
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Prepare data for JSON export
    user_tasks = []
    for task in todo_data:
        user_tasks.append({
            'username': username,
            'task': task['title'],
            'completed': task['completed'],
         
        })

        todo_all_employees[user_id] = user_tasks

    # Export to JSON
    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        json.dump(todo_all_employees, jsonfile)


if __name__ == "__main__":
    get_employee_todo()
