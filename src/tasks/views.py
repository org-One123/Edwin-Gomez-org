from datetime import datetime
from .models import Task

tasks_db = []
current_id = 1

def create_task(data: dict):
    global current_id
    title = data.get("title")
    due_date_str = data.get("due_date")

    if not title or not due_date_str:
        return {"error": "Todos los campos son obligatorios."}, 400

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        new_task = Task(task_id=current_id, title=title, due_date=due_date)
        tasks_db.append(new_task)
        current_id += 1
        return {"message": "Tarea creada exitosamente", "task": new_task.to_dict()}, 201
    except ValueError as e:
        return {"error": str(e)}, 400

def get_all_tasks(status_filter: str = None):
    if status_filter:
        filtered = [t.to_dict() for t in tasks_db if t.status.upper() == status_filter.upper()]
        return filtered, 200
    return [task.to_dict() for task in tasks_db], 200

def complete_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            task.status = "COMPLETED"
            return {"message": "Tarea marcada como completada", "task": task.to_dict()}, 200
    return {"error": "Tarea no encontrada"}, 404
