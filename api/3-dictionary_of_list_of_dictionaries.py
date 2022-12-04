#!/usr/bin/python3
""" Console Module """


if __name__ == "__main__":
    from json import dump
    import requests
    from sys import argv

    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    user_ids = map(lambda t: t["userId"], todos)

    json_todo_list = {}

    for user_id in user_ids:
        user = [user for user in users if user["id"] == user_id][0]
        user_todos = list(filter(lambda t: t["userId"] == user_id, todos))
        json_todo_list[user_id] = list(map(lambda t: {
            "username": user["username"],
            "task": t["title"],
            "completed": t["completed"],
        }, user_todos))

    with open("todo_all_employees.json", "w") as file:
        dump(json_todo_list, file)
