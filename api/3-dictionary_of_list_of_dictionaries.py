#!/usr/bin/python3
"""Gather user's todo from API."""
import json
import requests as r


if __name__ == "__main__":
    user = r.get('https://jsonplaceholder.typicode.com/users').json()
    todo = r.get('https://jsonplaceholder.typicode.com/todos').json()
    userdict = {}

    for u in user:
        userlist = []
        for t in todo:
            id = int(u["id"])
            if t["userId"] == id:
                userlist.append({
                    "username": u["username"],
                    "task": t["title"],
                    "completed": t["completed"],
                })
        userdict[str(id)] = userlist

    with open("todo_all_employees.json", "w") as file:
        json.dump(userdict, file)
