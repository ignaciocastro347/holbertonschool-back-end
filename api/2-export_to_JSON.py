#!/usr/bin/python3
""" Console Module """


if __name__ == "__main__":
    from json import dump
    import requests
    from sys import argv

    r = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            argv[1]))
    user = r.json()

    r = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            argv[1]))
    todos = r.json()

    todos = list(map(lambda t: {
        "task": t["title"],
        "completed": t["completed"],
        "username": user["username"]
    }, todos))

    with open(str(argv[1]) + '.json', 'w') as file:
        dump({"{}".format(argv[1]): todos}, file)
