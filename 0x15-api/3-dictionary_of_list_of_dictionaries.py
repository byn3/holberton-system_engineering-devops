#!/usr/bin/python3
""" Python script that uses rest api to fetch data """

if __name__ == "__main__":
    """ script that does what is asked above """
    import json
    import requests
    from sys import argv

    # retrieve the user info, holds name, company json, website, phone, email,
    # username, address, geo location, city, zip, suite, and id
    user_info = requests.get(
                    "https://jsonplaceholder.typicode.com/users").json()
    # Gets the todo list which contains userid, id, title, completed
    todo_list = requests.get(
                "https://jsonplaceholder.typicode.com/todos").json()
    all_dict = {}
    all_users = {}
    # build the massive dict of each user and data
    # this vuilds all_users and a key for all dicts
    for each_user in user_info:
        identity = each_user.get("id")
        all_dict[identity] = []
        all_users[identity] = each_user.get("username")
    # this builds all dicts
    for each_todo in todo_list:
        temp = {}
        identity = each_todo.get("userId")
        temp["task"] = each_todo.get("title")
        temp["completed"] = each_todo.get("completed")
        temp["username"] = all_users.get(identity)
        all_dict.get(identity).append(temp)
    # JASON DERULOOOO
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_dict, f)
