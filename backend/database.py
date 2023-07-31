import redis
from model import Timbre
import json

r = redis.Redis(host='redis', port=6379, db=0)

def fetch_all_todos():
    keys = [key.decode() for key in r.keys('timbre:*')]
    todos = []
    for key in keys:
        value = r.get(key)
        todos.append(Timbre(**value))
    return todos

def create_todo(todo):
    key = f"timbre:{todo['datetime']}"
    todo_str = json.dumps(todo)
    r.set(key, todo_str)
    return todo
