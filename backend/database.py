import redis
from model import Timbre
import json

r = redis.Redis(host='redis', port=6379, db=0)

def fetch_all_todos():
    todos = []
    for key in r.keys('*'):
        value = r.get(key)
        value = value.decode("utf-8")
        todos.append(value)
    return todos

def create_todo(todo):
    key = f"timbre:{todo['datetime']}"
    todo_str = str(todo)
    r.set(key, todo_str)
    return todo
