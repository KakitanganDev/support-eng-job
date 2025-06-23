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
        high_priority = []
        for task in self.tasks:
            if task.priority == "high" or task.priority == 1: #Correction 3: added task.priority == 1 assuming 1 is high priority
                high_priority.append(task)
        return high_priority
