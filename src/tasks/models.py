from datetime import date

class Task:
    def __init__(self, task_id: int, title: str, due_date: date, status: str = "PENDIENTE"):
        if not title or len(title.strip()) < 3:
            raise ValueError("El título debe tener al menos 3 caracteres.")
        
        if due_date < date.today():
            raise ValueError("La fecha de vencimiento no puede ser anterior a la fecha actual.")

        self.id = task_id
        self.title = title.strip()
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "due_date": self.due_date.isoformat(),
            "status": self.status
        }
