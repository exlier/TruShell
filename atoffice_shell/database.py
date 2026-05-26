from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import List

from platformdirs import user_data_dir

from .model import Todo

APP_NAME = "AtOfficeShell"
APP_AUTHOR = "AkshajSinghal"
DATA_DIR = Path(user_data_dir(APP_NAME, APP_AUTHOR))
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "todos.db"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()


def _create_table() -> None:
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS todos (
            task TEXT,
            category TEXT,
            date_added TEXT,
            date_completed TEXT,
            status INTEGER,
            position INTEGER
        )"""
    )
    conn.commit()


_create_table()


def insert_todo(todo: Todo) -> None:
    cursor.execute("SELECT count(*) FROM todos")
    count = cursor.fetchone()[0]
    todo.position = count if count else 0
    with conn:
        cursor.execute(
            "INSERT INTO todos VALUES (:task, :category, :date_added, :date_completed, :status, :position)",
            {
                "task": todo.task,
                "category": todo.category,
                "date_added": todo.date_added,
                "date_completed": todo.date_completed,
                "status": todo.status,
                "position": todo.position,
            },
        )


def get_all_todos() -> List[Todo]:
    cursor.execute("SELECT * FROM todos")
    results = cursor.fetchall()
    return [Todo(*result) for result in results]


def delete_todo(position: int) -> None:
    cursor.execute("SELECT count(*) FROM todos")
    count = cursor.fetchone()[0]

    with conn:
        cursor.execute("DELETE FROM todos WHERE position = :position", {"position": position})
        for pos in range(position + 1, count):
            _change_position(pos, pos - 1, commit=False)
        conn.commit()


def _change_position(old_position: int, new_position: int, commit: bool = True) -> None:
    cursor.execute(
        "UPDATE todos SET position = :position_new WHERE position = :position_old",
        {"position_old": old_position, "position_new": new_position},
    )
    if commit:
        conn.commit()


def update_todo(position: int, task: str | None, category: str | None) -> None:
    with conn:
        if task is not None and category is not None:
            cursor.execute(
                "UPDATE todos SET task = :task, category = :category WHERE position = :position",
                {"task": task, "category": category, "position": position},
            )
        elif task is not None:
            cursor.execute(
                "UPDATE todos SET task = :task WHERE position = :position",
                {"task": task, "position": position},
            )
        elif category is not None:
            cursor.execute(
                "UPDATE todos SET category = :category WHERE position = :position",
                {"category": category, "position": position},
            )


def complete_todo(position: int) -> None:
    from datetime import datetime

    with conn:
        cursor.execute(
            "UPDATE todos SET status = 2, date_completed = :date_completed WHERE position = :position",
            {"position": position, "date_completed": datetime.now().isoformat()},
        )
