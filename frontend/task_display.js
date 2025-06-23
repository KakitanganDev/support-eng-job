class TaskDisplay {
  constructor(tasks) {
    this.tasks = tasks;
  }

  displayTasks() {
    if (!this.tasks) {
      //return;  // Should return ""
      // Return empty string if tasks list is null or empty
      return "";
    }
    return this.tasks.map(task => `${task.id}: ${task.title} (${task.priority})`).join("\n");
  }

  filterByPriority(priority) {
    //return this.tasks.filter(task => task.priority === priority);
    // Correction 1: Ensure priority comparison is case-insensitive
    return this.tasks.filter(task => task.priority.toLowerCase() === priority.toLowerCase());
  }

  getTaskCount() {
    //return this.tasks.length.toString();
    // Correction 2: Return the number of tasks as a number
    return this.tasks.length;
  }
}

module.exports = TaskDisplay;
