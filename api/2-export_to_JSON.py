#!/usr/bin/python3
"""
    Write a Python script that, using this REST API
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
if __name__ == '__main__':
    """
        task 2
    """
    import json
    import requests
    import sys
    employee_id = sys.argv[1]
    employee_user_id = requests.\
        get('https://jsonplaceholder.typicode.com/users/{}'.
            format(employee_id)).json()
    employee_info = requests.\
        get('https://jsonplaceholder.typicode.com/todos?userId={}'.
            format(employee_user_id['id'])).json()

    # Variables
    USER_ID = employee_info[0]['userId']
    USERNAME = employee_user_id['username']
    list_to_json = []
    for task in employee_info:
        dict_to_json = {}
        dict_to_json['task'] = task['title']
        dict_to_json['completed'] = task['completed']
        dict_to_json['username'] = USERNAME
        list_to_json.append(dict_to_json)

    dict_to_json = {USER_ID: list_to_json}

    filename = str(USER_ID) + '.json'

    with open(filename, 'w') as f:
        line_to_write = json.dump(dict_to_json, f)
        f.close()
