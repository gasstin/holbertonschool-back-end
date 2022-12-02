#!/usr/bin/python3
"""
    Write a Python script that, using this REST API
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
if __name__ == '__main__':
    """
        task 0
    """
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

    filename = str(USER_ID) + '.csv'

    with open(filename, 'w') as f:
        for task in employee_info:
            f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".
                    format(USER_ID, USERNAME,
                           task['completed'], task['title']))
        f.close()
