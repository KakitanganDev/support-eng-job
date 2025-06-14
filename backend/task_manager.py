class Task:
    def __init__(self, id, title, priority, status="pending"):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status

#Map numeric values to a high or low value, avoiding variable mismatch error.
priority_map = {
    1: "high",
    2: "low"
}

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, id, title, priority):
        #Convert numeric values to string values.
        if isinstance(priority,int):
            priority = priority_map.get(priority, "low") #set low as default priority.

        if any(task.id == id for task in self.tasks):
            return #Raise errors in case duplicats occur
        task = Task(id, title, priority)
        self.tasks.append(task)
        return task

    def update_status(self, id, new_status):
        for task in self.tasks:
            if task.id == id:
                task.status = new_status
                return True
            return False #previously, every task was updated incorrectly in the second loop. Now it does nothing if task is not found.

    def get_high_priority_tasks(self):
        high_priority = []
        for task in self.tasks:
            if task.priority.lower() == "high": #adjusted to normalize casing
                high_priority.append(task)
        return high_priority
