# Python To-Do Task Manager

A command-line task management application built with Python. Users can add tasks, view their task list, mark tasks as complete, and delete tasks. Task data is stored in a JSON file so it can be loaded again when the program starts.

## Features

- **Add tasks:** Create tasks with a description.
- **View tasks:** Display all tasks with their current status.
- **Mark tasks as complete:** Update a task's completion status.
- **Delete tasks:** Remove tasks by their list number.
- **Save tasks:** Store task data in a JSON file.
- **Load tasks:** Restore saved tasks when the program starts.
- **Input validation:** Handle invalid task numbers and menu choices.

## Technologies Used

- Python
- JSON module
- File handling
- Functions and loops
- Lists and dictionaries
- Exception handling

## Project Structure

```text
python-todo-task-manager/
├── todo.py
└── loadtask.json
```

`loadtask.json` is created when tasks are saved, depending on how the program is run and whether a task is added or modified.

## How to Run

1. Install Python.
2. Save the Python code as `todo.py`.
3. Open a terminal in the project directory.
4. Run:

   ```bash
   python todo.py
   ```

No external libraries are required.

## How It Works

Each task is stored as a dictionary containing its description and completion status. The task dictionaries are held in a list under the `tasks` key.

Example JSON structure:

```json
{
  "tasks": [
    {
      "description": "Practice Python",
      "complete": false
    },
    {
      "description": "Finish a project",
      "complete": true
    }
  ]
}
```

When the program starts, it loads existing tasks from `loadtask.json`. When a task is added, completed, or deleted, the updated task data is saved to the file.

## Available Operations

1. Add Task
2. View Task
3. Mark Task
4. Delete Task
5. Exit

## Possible Improvements

- Allow users to edit task descriptions.
- Add task priorities and due dates.
- Filter tasks by pending or completed status.
- Display the total number of pending and completed tasks.
- Improve error handling for missing or invalid JSON data.
- Add confirmation before deleting a task.

## Learning Objectives

This project demonstrates practical use of Python functions, lists, dictionaries, JSON serialization, file handling, input validation, and persistent data storage.
