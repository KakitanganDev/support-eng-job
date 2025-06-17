class TaskDisplay {
  constructor(tasks) {
    this.tasks = tasks;
  }

  displayTasks() {
    if (!this.tasks || this.tasks.length == 0) {
      return "";
    }
    return this.tasks
      .map((task) => `${task.id}: ${task.title} (${task.priority})`)
      .join("\n");
  }

  filterByPriority(priority) {
    const filteredTask = this.tasks.filter(
      (task) => task.priority.toLowerCase() === priority.toLowerCase()
    );

    return filteredTask;
  }

  getTaskCount() {
    return this.tasks.length;
  }
}

module.exports = TaskDisplay;
