#!/usr/bin/python3
""" Python script that uses rest api to fetch data """

if __name__ == "__main__":
    """ script that does what is asked above """
    import json
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
    # Get the username in the json
    username = user_info.get("username")
    array = []
    for each_todo in todo_list:
        temp = {}
        temp["task"] = each_todo.get("title")
        temp["completed"] = each_todo.get("completed")
        temp["username"] = username
        array.append(temp)
    # JASON DE RULLLOOO!! JJJJJ ARRR!! YEE!!
    jsonderulo = {}
    jsonderulo[employee_id] = array
    with open("{}.json".format(employee_id), "w") as jasonderulo:
        json.dump(jsonderulo, jasonderulo)
