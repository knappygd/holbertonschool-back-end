#!/usr/bin/python3
"""Gather user's todo from API."""
import requests as r
import sys


if __name__ == "__main__":
    id = int(sys.argv[1])
    user = r.get(f'https://jsonplaceholder.typicode.com/users/{id}').json()
    todo = r.get('https://jsonplaceholder.typicode.com/todos').json()
    username = user["username"]

    with open(f"{id}.csv", "w") as file:
        for t in todo:
            completed = t['completed']
            title = t['title']
            if t['userId'] == id:
                file.write(f'"{id}","{username}","{completed}","{title}"\n')
