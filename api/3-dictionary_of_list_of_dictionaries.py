#!/usr/bin/python3
"""
    Records all tasks from all employees
"""
if __name__ == '__main__':
    """
        task 3
    """
    import json
    import requests
    with open('todo_all_employees.json', 'w') as f:
        employee_user_id = requests.\
            get('https://jsonplaceholder.typicode.com/users/').json()
              # get all the users
        dict_to_json = {}
        for count_user in range(0, len(employee_user_id)):
            USERNAME = employee_user_id[count_user]['username']
              # choose username
            USER_ID = employee_user_id[count_user]['id']  # choose user_id
            employee_info = requests.\
            get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                format(employee_user_id[count_user]['id'])).\
                json()  # get the user's task
            
            list_to_json = []
            for dict_auxiliar in employee_info:
                del dict_auxiliar['id']  # delete id
                del dict_auxiliar['userId']  # delete userId
                dict_auxiliar['task'] = dict_auxiliar.pop('title')
                  # rename title
                dict_auxiliar['username'] = USERNAME
                  # add username
                list_to_json.append(dict_auxiliar)
                dict_to_json[USER_ID] = list_to_json  
                  # add the new list to the dict_to_json

        json.dump(dict_to_json, f)  # write the file
        f.close()
