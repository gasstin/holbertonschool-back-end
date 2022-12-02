#!/usr/bin/python3
"""
    Write a Python script that, using this REST API
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
if __name__ == '__main__':
    import requests
    import sys
    import urllib
    
    
    employee_id = sys.argv[1]
    
    employee_user_id = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()
    employee_info = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    
    # Variables
    EMPLOYEE_NAME = employee_user_id['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    LIST_OF_TASK = []
    for task in employee_info:
        if employee_user_id['id'] == task['userId']:
            if task['completed']:
                NUMBER_OF_DONE_TASKS += 1
                LIST_OF_TASK.append(task['title'])
            TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for line in LIST_OF_TASK:
        print("  {}".format(line))

    