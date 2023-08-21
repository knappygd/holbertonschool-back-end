#!/usr/bin/python3
"""Gather user's todo from API."""
import requests as r
import sys
import json


if __name__ == "__main__":
    id = int(sys.argv[1])
    user = r.get(f'https://jsonplaceholder.typicode.com/users/{id}').json()
    todo = r.get('https://jsonplaceholder.typicode.com/todos').json()
    userlist = []

    with open("{}.json".format(id), "w") as file:
        for t in todo:
            if t["userId"] == id:
                userlist.append({
                    "task": t["title"],
                    "completed": t["completed"],
                    "username": user["username"]
                })

        json.dump({str(id): userlist}, file)
