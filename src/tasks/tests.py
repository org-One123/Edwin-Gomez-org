import unittest
from datetime import date, timedelta
from .models import Task

class TestTaskModel(unittest.TestCase):

    def test_create_valid_task(self):
        today = date.today()
        task = Task(task_id=1, title="Estudiar Git", due_date=today)
        self.assertEqual(task.title, "Estudiar Git")
        self.assertEqual(task.status, "PENDIENTE")

    def test_short_title_raises_error(self):
        with self.assertRaises(ValueError):
            Task(task_id=2, title="Ab", due_date=date.today())

    def test_past_date_raises_error(self):
        yesterday = date.today() - timedelta(days=1)
        with self.assertRaises(ValueError):
            Task(task_id=3, title="Tarea pasada", due_date=yesterday)

if __name__ == "__main__":
    unittest.main()
