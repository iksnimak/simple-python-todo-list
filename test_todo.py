# test_todo.py

import pytest
from todo import TodoApp


def test_add_task(capsys):
    app = TodoApp()

    app.add_task("Buy milk")

    captured = capsys.readouterr()

    assert len(app.tasks) == 1
    assert app.tasks[0]["task"] == "Buy milk"
    assert app.tasks[0]["completed"] is False
    assert "Task 'Buy milk' added!" in captured.out


def test_remove_task(capsys):
    app = TodoApp()
    app.add_task("Buy milk")

    app.remove_task(0)

    captured = capsys.readouterr()

    assert len(app.tasks) == 0
    assert "Task 'Buy milk' removed!" in captured.out


def test_remove_task_invalid_index(capsys):
    app = TodoApp()

    app.remove_task(5)

    captured = capsys.readouterr()

    assert "Invalid task index." in captured.out


def test_mark_completed(capsys):
    app = TodoApp()
    app.add_task("Learn pytest")

    app.mark_completed(0)

    captured = capsys.readouterr()

    assert app.tasks[0]["completed"] is True
    assert "marked as completed" in captured.out


def test_mark_completed_invalid_index(capsys):
    app = TodoApp()

    app.mark_completed(2)

    captured = capsys.readouterr()

    assert "Invalid task index." in captured.out


def test_view_tasks_empty(capsys):
    app = TodoApp()

    app.view_tasks()

    captured = capsys.readouterr()

    assert "No tasks to show." in captured.out


def test_view_tasks_with_data(capsys):
    app = TodoApp()

    app.add_task("Task 1")
    app.add_task("Task 2")
    app.mark_completed(1)

    # Clear previous output
    capsys.readouterr()

    app.view_tasks()

    captured = capsys.readouterr()

    assert "0. Task 1 - Not Completed" in captured.out
    assert "1. Task 2 - Completed" in captured.out