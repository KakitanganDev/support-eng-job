class Task:
    def __init__(self, id, title, priority, status="pending"):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, id, title, priority):

        # Correction 1: added this to prevent adding a task with an existing ID
        if any(task.id == id for task in self.tasks):
            return None 

        task = Task(id, title, priority)
        self.tasks.append(task)
        return task

    def update_status(self, id, new_status):
        for task in self.tasks:
            if task.id == id:
                task.status = new_status
                return True

        #Correction 2: removed this to prevent updating every task if the ID is not found
        #for task in self.tasks:
            #task.status = new_status

        return False

    def get_high_priority_tasks(self):
        # Maps multiple input values to normalized priority levels
        PRIORITY_MAP = {
            "high": "high",
            1: "high",
            "medium": "medium",
            2: "medium",
            "low": "low",
            3: "low"
        }
        high_priority = []
        for task in self.tasks:
            normalized_priority = PRIORITY_MAP.get(task.priority)
            #if task.priority == "high":
            if normalized_priority == "high": #Correction 3: changed to use normalized priority
                high_priority.append(task)
        return high_priority
