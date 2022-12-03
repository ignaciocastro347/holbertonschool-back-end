#!/usr/bin/python3
""" Console Module """


if __name__ == "__main__":
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

    done_todos = list(filter(
        lambda t: t["completed"], todos))

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"],
        len(done_todos),
        len(todos)
    ))
    for todo in done_todos:
        print("\t {}".format(todo["title"]))
