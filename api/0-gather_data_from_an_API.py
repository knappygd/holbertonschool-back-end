#!/usr/bin/python3
"""Gather user's todo from API."""
import requests as r
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    user = r.get(f'https://jsonplaceholder.typicode.com/users/{id}').json()
    todo = r.get('https://jsonplaceholder.typicode.com/todos').json()
    name = user["name"]
    tasks = int(len(todo) / 10)
    done = 0
    finished = []

    for t in todo:
        if t["userId"] == id and t["completed"]:
            finished.append(t["title"])
            done += 1

    print(f"Employee {name} is done with tasks({done}/{tasks}):")
    [print(f"\t {t}") for t in finished]
