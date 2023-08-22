#!/usr/bin/python3
"""Gather user's todo from API."""
import json
import requests as r


if __name__ == "__main__":
    user = r.get(f'https://jsonplaceholder.typicode.com/users').json()
    todo = r.get('https://jsonplaceholder.typicode.com/todos').json()
    userlist = []
    userdict = {}

    with open("todo_all_employees.json", "w") as file:
        for u in user:
            id = int(u["id"])
            for t in todo:
                if t["userId"] == id:
                    userlist.append({
                        "task": t["title"],
                        "completed": t["completed"],
                        "username": u["username"]
                    })
            userdict[str(id)] = userlist
            userlist = []
        json.dump({str(id): userlist}, file)
