

# 📝 CLI To-Do App

A simple, colorful command-line To-Do application built with **Typer**, **Rich**, and **SQLite**.
Add tasks, list them in a formatted table, and mark them as completed — all from the terminal.

---

## 🚀 Features

* 📋 Display all tasks in a Rich-styled table
* ➕ Add new tasks
* ✅ Mark tasks as completed
* 💾 Persistent local storage using SQLite (`todo.db`)
* 🐍 Built with clean, modern Python CLI tools (Typer + Rich)

---

## 📦 Requirements

* Python 3.10+
* Typer
* Rich

Install dependencies:

```bash
pip install typer rich
```

SQLite is included with Python, so no extra installation is needed.

---

## 📂 Project Structure

```
.
├── main.py         # CLI app
├── todo.db         # (Auto-created) SQLite DB
└── README.md
```

---

## ▶️ Running the App

Run the CLI using:

```bash
python main.py
```

Or install it as a command-line tool (optional):

```bash
pip install .
```

---

## 🧑‍💻 Available Commands

### 1. **Show all tasks**

Displays your to-do list in a Rich-formatted table.

```bash
python main.py show
```

Example output:

```
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Item                 ┃ Status     ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ Buy milk             │ pending    │
│ Finish project       │ completed  │
└──────────────────────┴────────────┘
```

---

### 2. **Add a new task**

```bash
python main.py add "Your task here"
```

Examples:

```bash
python main.py add "Buy groceries"
python main.py add Finish homework
```

* Prevents duplicate tasks
* Automatically sets status to `pending`

---

### 3. **Mark a task as completed**

Command name: `c`

```bash
python main.py c "task name"
```

Examples:

```bash
python main.py c "Buy groceries"
python main.py c Finish homework
```

Marks the task's `status` column as `"completed"`.

---

## 🗃 How Data is Stored

Tasks are stored in a simple SQLite database:

```
todo.db
```

With one table:

```
todo_items(item TEXT, status TEXT)
```

---

## 🛠 Future Improvements

If you plan to extend the app, here are some ready ideas:

* Delete tasks
* Edit tasks
* Add priority levels
* Add timestamps (created_at, completed_at)
* Color-coded statuses
* Export tasks to JSON or CSV
* Support for task IDs instead of full text matching

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request
