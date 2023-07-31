import aioredis
from model import Timbre

redis = aioredis.from_url("redis://localhost")

async def fetch_all_todos():
    keys = await redis.keys('timbre:*')
    todos = []
    for key in keys:
        value = await redis.get(key)
        todos.append(Timbre(**value))
    return todos

async def create_todo(todo):
    key = f"timbre:{todo.datetime}"
    await redis.set(key, todo)
    return todo
