#!/usr/bin/python3
""" Python script that creates a csv file """

if __name__ == "__main__":
    """ script that does what is asked above
    and is import protected """
    import csv
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

    # writers a csv file now with #.csv as the file name
    with open("{}.csv".format(employee_id), "w") as f:
        row = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
        for each_todo in todo_list:
            row.writerow([employee_id, user_info.get("username"),
                         each_todo.get("completed"), each_todo.get("title")])
