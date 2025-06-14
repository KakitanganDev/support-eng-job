class TaskDisplay {
  constructor(tasks) {
    this.tasks = tasks ?? [];
  }

  displayTasks() {
    // The original falsy check is a dead code in current unit test, the empty list [] passed in to ctor is truthy,
    // the only proper use case is undefined and null,
    // so add more tests to exercise the possible code paths for the proper fix in ctor - covers all 3 functions.
    return this.tasks.map(task => `${task.id}: ${task.title} (${task.priority})`).join("\n");
  }

  filterByPriority(priority) {
    return this.tasks.filter(task => task.priority === priority.toLowerCase());
  }

  getTaskCount() {
    return this.tasks.length;
  }
}

module.exports = TaskDisplay;
