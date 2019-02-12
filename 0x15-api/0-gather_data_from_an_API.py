#!/usr/bin/python3
""" Python script that uses rest api to fetch data """

if __name__ == "__main__":
    """ script that does what is asked above """
    import requests
    from sys import argv

    # get the id and cast into an int
    employee_id = int(argv[1])
    # retrieve the user info, holds name, company json, website, phone, email,
    # username, address, geo location, city, zip, suite, and id
    user_info = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                             format(employee_id)).json()
    # Gets the todo list which contains userid, id, title, completed
    todo_list = requests.get(
                "https://jsonplaceholder.typicode.com/todos?userId={}".
                format(employee_id)).json()
    completed_array = []
    # store only the completed tasks
    for eachTodo in todo_list:
        if eachTodo.get("completed"):
            completed_array.append(eachTodo.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
                user_info.get('name'), len(completed_array), len(todo_list)))
    for element in completed_array:
        print("\t {}".format(element))
