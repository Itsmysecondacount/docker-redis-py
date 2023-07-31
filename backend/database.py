import redis
import json  # para convertir los objetos a JSON

r = redis.Redis(host='redis', port=6379, db=0)

def fetch_all_todos():
    todos = []
    for key in r.keys('*'):
        value = r.get(key)
        value = value.decode("utf-8")
        # debes decodificar los objetos JSON guardados en Redis
        todo = json.loads(value)
        todos.append(todo)
    return todos

def create_todo(todo):
    key = f"timbre:{todo['datetime']}"
    # convierte el objeto todo a una cadena JSON antes de guardarla
    todo['datetime'] = todo['datetime'].isoformat()
    todo_str = json.dumps(todo)
    r.set(key, todo_str)
    return todo