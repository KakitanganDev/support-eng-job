from enum import Enum

# Use enum to streamline comparison
Priority = Enum("Priority", ["high", "low"])


class Task:
    def __init__(self, id, title, priority, status="pending"):
        self.id = id
        self.title = title
        if isinstance(priority, str):
            # This needs to watch out for future use case with "1" integer string
            self.priority = getattr(Priority, priority.lower())
        else:
            # This assumes int, need to also watch for future True for high priority
            self.priority = Priority(priority)
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, id, title, priority):
        task = Task(id, title, priority)
        if any(t.id == id for t in self.tasks):
            # Quick check with generator expression on any to prevent duplicate task,
            # - using set is easier but requires quite some changes
            #   - also, convert to list vice versa will be slow
            # - using dictionary requires explicitly spliting k-v(object) and a ton of changes
            return None
        self.tasks.append(task)
        return task

    def update_status(self, id, new_status):
        for task in self.tasks:
            if task.id == id:
                task.status = new_status
                return True
        # Don't update status for all elements
        return False

    def get_high_priority_tasks(self):
        # Use list comprehension for quick filtering
        return [task for task in self.tasks if task.priority == Priority.high]
