""" add task feature steps"""
from io import StringIO
from behave import given, when, then
from todo_list import TodoList, InvalidInputError


@given("the todo list app is started")
def step_todo_list_started(context):
    """Start the todo list app"""
    context.todo_list = TodoList()


@given('the todo list app is started with "{tasks}" in the list')
def step_todo_list_started_with_tasks(context, tasks):
    """Start the todo list app with tasks"""
    context.todo_list = TodoList()
    for task in tasks.split(","):
        context.todo_list.add_task(task)


@when('the user adds "{task}" to the to-do list app')
def step_add_task(context, task):
    """Add a task to the to-do list"""
    try:
        context.todo_list.add_task(task)
    except InvalidInputError:
        context.error = True


@then('the to-do list should contain "{task}"')
def step_check_task_in_list(context, task):
    """Check that the task is in the to-do list"""
    assert not hasattr(context, "error"), "Invalid input error"
    task_obj = context.todo_list.get_task(task)
    assert task_obj.get_task() == task


@when('the user marks "{task}" as complete')
def step_mark_task_complete(context, task):
    """Mark a task as complete"""
    try:
        context.todo_list.mark_task_complete(task)
    except InvalidInputError:
        context.error = True


@then('the to-do list should contain "{task}" as complete')
def step_check_task_marked_complete(context, task):
    """Check that a task is marked as complete"""
    assert not hasattr(context, "error"), "Invalid input error"
    task_obj = context.todo_list.get_task(task)
    assert task_obj.is_complete() is True


@when('the user marks "{task}" as incomplete')
def step_mark_task_incomplete(context, task):
    """Mark a task as incomplete"""
    try:
        context.todo_list.mark_task_incomplete(task)
    except InvalidInputError:
        context.error = True


@then('the to-do list should contain "{task}" as incomplete')
def step_check_task_marked_incomplete(context, task):
    """Check that a task is marked as incomplete"""
    assert not hasattr(context, "error"), "Invalid input error"
    task_obj = context.todo_list.get_task(task)
    assert task_obj.is_complete() is False


@when('the user removes "{task}" from the to-do list app')
def step_remove_task(context, task):
    """Remove a task from the to-do list"""
    try:
        context.todo_list.remove_task(task)
    except InvalidInputError:
        context.error = True


@then('the to-do list does not contain "{task}"')
def step_check_task_not_in_list(context, task):
    """Check that the task is not in the to-do list"""
    assert not hasattr(context, "error"), "Invalid input error"
    try:
        context.todo_list.get_task(task)
        assert False, "Task found"
    except InvalidInputError:
        pass


@when("the user clears the to-do list")
def step_clear_tasks(context):
    """Clear the to-do list"""
    context.todo_list.clear_tasks()


@then("the to-do list should be empty")
def step_check_tasks_empty(context):
    """Check that the to-do list is empty"""
    assert len(context.todo_list.tasks) == 0


@when("the user lists the tasks")
def step_list_tasks(context):
    """List the tasks"""
    context.todo_list.list_tasks()


@then("the user should see all tasks {tasks}")
def step_check_tasks_listed(context, tasks):
    """Check that the tasks are listed"""
    for task in tasks.split(","):
        task = task.replace('"', "")
        assert task in context.stdout_capture.getvalue()
