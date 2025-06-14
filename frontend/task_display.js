class TaskDisplay {
  constructor(tasks) {
    console.log("Tasks initiated:", tasks);
    this.tasks = tasks;
  }

  displayTasks() {
    if (!this.tasks) {
      return "";  // Should return ""
    }
    return this.tasks.map(task => `${task.id}: ${task.title} (${task.priority})`).join("\n");
  }

  filterByPriority(priority) {
    return this.tasks.filter(
      //Normalize the case first before comparing, so all values are lower case.
      task => String(task.priority).toLowerCase() === String(priority).toLowerCase()
    );
  }

  getTaskCount() {
    return this.tasks.length; //Since expected value is Number, remove toString() function.
  }
}

module.exports = TaskDisplay;
