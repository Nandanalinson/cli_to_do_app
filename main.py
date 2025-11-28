import typer
import sqlite3
from rich.table import Table
from rich.console import Console

app = typer.Typer()


@app.command()
def show():
    connect = sqlite3.connect('todo.db')
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todo_items (item TEXT, status TEXT)')
    cursor.execute('SELECT item, status FROM todo_items')
    rows = cursor.fetchall()
    connect.close()

    table = Table(title="To-Do List")
    table.add_column("Item", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    for item, status in rows:
        table.add_row(item, status)
    console = Console()
    console.print(table)
    return ""
    
@app.command()
def add(task: list[str] = typer.Argument(...)):
    item = " ".join(task)
    connect = sqlite3.connect('todo.db')
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todo_items (item TEXT, status TEXT)')
    if item == "":
        print("Please provide a valid to-do item.")
        return
    if item in [row[0] for row in cursor.execute('SELECT item FROM todo_items')]:
        print("This item already exists in your to-do list.")
    else:
        cursor.execute('INSERT INTO todo_items (item, status) VALUES (?, ?)', (item, 'pending'))
        connect.commit()
        connect.close()
    print(f"{show()} ")
    print("cli_to_do")

@app.command()
def c(task: list[str] = typer.Argument(...)):
    item = " ".join(task)
    connect = sqlite3.connect('todo.db')
    cursor = connect.cursor()
    cursor.execute('UPDATE todo_items SET status = "completed" WHERE item = ?', (item,))
    connect.commit()
    connect.close()
    print(f"{show()} ")
   


if __name__ == "__main__":
    app()


