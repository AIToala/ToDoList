"""Todo List App that adds, lists, marks and clears tasks"""

# Imports
import os


class InvalidInputError(Exception):
    """InvalidInputError: an error raised when the user inputs an invalid value"""

    def __init__(self, message):
        super().__init__(message)


class InvalidState(Exception):
    """InvalidState: an error raised when the user gets to a state that is invalid"""

    def __init__(self, message):
        super().__init__(message)


class Task:
    """Class to create a task object"""

    def __init__(self, task):
        """Initialize task object"""
        self.task = task
        self.completed = False

    def __str__(self):
        """Return task object as a string"""
        completed = "✔ Complete" if self.completed else "❌ Incomplete"
        return f"{self.task:^30} | {completed:^15}"

    def mark_complete(self):
        """Mark task as complete"""
        self.completed = True

    def mark_incomplete(self):
        """Mark task as incomplete"""
        self.completed = False

    def is_complete(self):
        """Return True if task is complete, False if not"""
        return self.completed

    def get_task(self):
        """Return task"""
        return self.task

    def set_task(self, task):
        """Set task"""
        self.task = task


class TodoList:
    """Class to create a todo list object"""

    def __init__(self):
        """Initialize todo list object"""
        self.tasks = []

    def __str__(self):
        """Return todo list object as a string"""
        return str(self.tasks)

    def add_task(self, task):
        """Add task to todo list"""
        if not task:
            raise InvalidInputError("Task cannot be empty.")
        task_item = Task(task)
        self.tasks.append(task_item)
        print("Task added.")

    def remove_task(self, task):
        """Remove task from todo list"""
        if not self.tasks:
            raise InvalidState("No tasks in list.")
        self.tasks.remove(self.get_task(task))
        print("Task removed.")

    def list_tasks(self):
        """List all tasks in todo list"""
        if not self.tasks:
            raise InvalidState("No tasks in list.")
        print(f"{'Tasks':^30} | {'Status':^15}")
        for task in self.tasks:
            print(f"{task}")
        print("-----------------------------")

    def mark_task_complete(self, task):
        """Mark task as complete"""
        if not self.tasks:
            raise InvalidState("No tasks in list.")
        task_item = self.get_task(task)
        task_item.mark_complete()
        print("Task marked complete.")

    def mark_task_incomplete(self, task):
        """Mark task as incomplete"""
        if not self.tasks:
            raise InvalidState("No tasks in list.")
        task_item = self.get_task(task)
        task_item.mark_incomplete()
        print("Task marked incomplete.")

    def get_task(self, task):
        """Get task"""
        if not self.tasks:
            raise InvalidState("No tasks in list.")
        for task_item in self.tasks:
            if task_item.get_task() == task:
                return task_item
        raise InvalidInputError("Task not found.")

    def clear_tasks(self):
        """Clear all tasks from todo list"""
        self.tasks = []
        print("Tasks cleared.")


def main():
    """Main function"""
    clear_console()
    try:
        todo_list = TodoList()
        while True:
            choice = menu()
            if choice == "1":
                print("--- Add task ---")
                task = input("Enter task: ")
                todo_list.add_task(task)
                input("Press enter to continue...")
            elif choice == "2":
                print("--- List tasks ---")
                todo_list.list_tasks()
                input("Press enter to continue...")
            elif choice == "3":
                print("--- Mark task complete ---")
                task = input("Enter task: ")
                todo_list.mark_task_complete(task)
                input("Press enter to continue...")
            elif choice == "4":
                print("--- Mark task incomplete ---")
                task = input("Enter task: ")
                todo_list.mark_task_incomplete(task)
                input("Press enter to continue...")
            elif choice == "5":
                print("--- Remove task ---")
                task = input("Enter task: ")
                todo_list.remove_task(task)
                input("Press enter to continue...")
            elif choice == "6":
                todo_list.clear_tasks()
                input("Press enter to continue...")
            elif choice == "7":
                print("Exiting...")
                exit()
            else:
                print("Invalid choice")
            clear_console()
    except InvalidInputError as error:
        print(error)
        input("Press enter to continue...")
        main()
    except InvalidState as error:
        print(error)
        input("Press enter to continue...")
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()


def menu():
    """Print menu"""
    print("Todo List App")
    print("\nMenu:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task complete")
    print("4. Mark task incomplete")
    print("5. Remove task")
    print("6. Clear tasks")
    print("7. Exit")
    choice = input("Enter choice: ")
    print("-----------------------------")
    return choice


def clear_console():
    """Clear console"""
    os.system("cls")


if __name__ == "__main__":
    main()
