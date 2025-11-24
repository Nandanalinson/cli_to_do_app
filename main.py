import typer
import sqlite3

app = typer.Typer()


items = []

@app.command()
def to_do_list(item: str):
    print(f"item added : {item}")
    connect = sqlite3.connect('todo.db')
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todo_items (item TEXT)')
    cursor.execute('INSERT INTO todo_items (item) VALUES (?)', (item,))
    cursor.execute('SELECT * FROM todo_items')
    todo = cursor.fetchall()
    connect.commit()
    connect.close()
    items.append(item)
    print(f"Current to-do list: {todo} ")


@app.command()
def done_list(item : str):
    connect = sqlite3.connect('todo.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM todo_items WHERE item = ?', (item,))
    if cursor.rowcount == 0:
        print(f"Item '{item}' not found in the to-do list.")
    else:
        print(f"item removed : {item}")
    connect.commit()
    cursor.execute('SELECT * FROM todo_items')
    todo = cursor.fetchall()
    connect.close()
    print(f"Current to-do list: {todo}")


if __name__ == "__main__":
    app()


