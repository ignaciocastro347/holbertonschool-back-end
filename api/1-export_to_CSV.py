#!/usr/bin/python3
""" Console Module """


if __name__ == "__main__":
    import csv
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

    with open(argv[1] + '.csv', 'w') as file:
        for todo in todos:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow([todo['userId'],
                             user["username"],
                             todo['completed'],
                             todo['title']])
