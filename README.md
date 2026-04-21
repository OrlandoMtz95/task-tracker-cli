Task Tracker CLI

A simple Command Line Interface (CLI) application built with Python to
manage tasks.

Features

-   Add tasks
-   Update tasks
-   Delete tasks
-   Mark tasks as done or in-progress
-   List all tasks
-   Filter tasks by status:
    -   todo
    -   in-progress
    -   done
    -   not-done
    

Technologies Used

-   Python
-   JSON (for data storage)

Installation

    git clone https://github.com/OrlandoMtz95/task-tracker-cli.git
    cd task-tracker-cli

Usage

Add a task

    python app.py add "Learn backend"

List all tasks

    python app.py list

Filter tasks

    python app.py list todo
    python app.py list done
    python app.py list in-progress
    python app.py list not-done

Update task

    python app.py update 1 "New description"

Delete task

    python app.py delete 1

Mark task

    python app.py mark-done 1
    python app.py mark-in-progress 1

Project Structure

    app.py
    tasks.json (ignored)

Purpose

This project was built to practice backend fundamentals such as:

-   CLI development
-   File handling
-   CRUD operations
-   Data persistence

Author

Orlando Martinez