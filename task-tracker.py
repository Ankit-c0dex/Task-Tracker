import os
import json

tasks = []
# l = len(tasks)

if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    
def add_task():
    name = input("Description: ")
    tasks.append({"task": name, "status": "incomplete"})
    save_tasks()

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    for i in range(len(tasks)):
        print(f"{i + 1}: {tasks[i]['task']} - {tasks[i]['status']}")

def update_status():
    view_tasks()
    try:
        id = int(input("Enter task ID: "))
        status = input("Is this task \n 1. In Progress \n 2. Completed \n Enter:")
        if status == "1" or status in "complete":
            tasks[id - 1]["status"] = "complete"
        elif status == "2" or status in "progress":
            tasks[id - 1]["status"] = "In Progress"
    except(ValueError, IndexError):
        print("Enter correct task ID.")


def show_progress():
    if tasks:
        prg = 0
        for _ in range(len(tasks)):
            t = tasks[_]
            if t["status"] == "In Progress":
                print(f"{_ + 1}: {t['task']}")
                prg += 1
        if prg == 0:
            print("No tasks are currently in progress!")


def show_completed():
    if tasks:
        inc = 0
        l = len(tasks)
        for _ in range(l):
            t = tasks[_]            #temporary variable for better readability
            if t["status"] == "complete":
                print(f"{_ + 1}: {t['task']}")
            else:
                inc += 1
        if inc == l:
            print("No tasks completed so far.")

    else:
        print("No tasks yet")

def show_incompleted():
    if tasks:
        comp = 0
        for _ in range(len(tasks)):
            t = tasks[_ + 1]
            if t["status"] == "incomplete":
                print(f"{_ + 1}: {t['task']}")
            else:
                comp += 1
        if comp == len(tasks):
            print("No tasks are currently incomplete")
    else:
        print("No tasks yet!")
        

def update_task():
    view_tasks()
    try:
        id = int(input("Enter task number to edit: "))
        new = input("Enter new description: ")
        tasks[id - 1]["task"] = new
    except (ValueError, IndexError):
        print("Enter correct task ID")

def delete_task():
    view_tasks()
    try:
        id = int(input("Enter task number to remove: "))
        tasks.pop(id - 1)
    except (ValueError, IndexError):
        print("Enter correct task id!")


while True:
    print("\n---   Task Tracker   ---")
    print("1. Add Task \n 2. View Tasks \n 3. Update Status")
    print("4. Show completed tasks \n 5. Show incomplete tasks \n 6. Show tasks in progress")
    print("7. Delete a task \n 8. Update a task \n X. Exit")

    choice = input("Enter choice from the menu: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_status()
    elif choice == "4":
        show_completed()
    elif choice == "5":
        show_incompleted()
    elif choice == "6":
        show_progress()
    elif choice == "7":
        delete_task()
    elif choice == "8":
        update_task()
    elif choice.upper() == "X":
        print("Thanks for using Task Tracker")
        break
    else:
        print("Choose a valid task")

