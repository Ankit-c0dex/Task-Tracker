import os
import sys
import json
from datetime import datetime

tasks = []

if os.path.exists("tasks.json"):
    with open ("tasks.json") as file:
        tasks = json.load(file)

if len(sys.argv) < 2:
    sys.exit("Enter arguments!")

def main():
    def save_tasks():
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

    def add_task(name):
        tasks.append({"id": len(tasks) + 1, "task": name, "status": "Not Done", "created": datetime.now().isoformat(), "updated": datetime.now().isoformat()})
        save_tasks()

    def update_task(id, name):
        tasks[id - 1]["task"] = name
        tasks[id - 1]["updated"] = datetime.now().isoformat()
        save_tasks()
    
    def delete_task(id):
        tasks.pop(id - 1)
        save_tasks()
    
    def in_progress(id):
        tasks[id - 1]["status"] = "In Progress"
        save_tasks()
    
    def mark_done(id):
        tasks[id - 1]["status"] = "Done"
        save_tasks()
    
    def view_tasks(i = 0):
        if i == 0:
            for j in range(len(tasks)):
                print(f"{tasks[j]['id']}. {tasks[j]['task']} - {tasks[j]['status']}")
        elif i == 1:
            for j in range(len(tasks)):
                if tasks[j]['status'] == "Done":
                    print(f"{tasks[j]['id']}. {tasks[j]['task']} - {tasks[j]['status']}")
        elif i == 2:
            for j in range(len(tasks)):
                if tasks[j]['status'] == "Not Done":
                    print(f"{tasks[j]['id']}. {tasks[j]['task']} - {tasks[j]['status']}")
        elif i == 3:
            for j in range(len(tasks)):
                if tasks[j]['status'] == "In Progress":
                    print(f"{tasks[j]['id']}. {tasks[j]['task']} - {tasks[j]['status']}")
    
    try:
        if sys.argv[1] == "add":
            add_task(sys.argv[2])
            print(f"Task added successfully. ID: {len(tasks)}")
        elif sys.argv[1] == "update":
            update_task(int(sys.argv[2]), sys.argv[3])
        elif sys.argv[1] == "delete":
            delete_task(int(sys.argv[2]))
        elif sys.argv[1] == "mark-in-progress":
            in_progress(int(sys.argv[2]))
        elif sys.argv[1] == "mark-done":
            mark_done(int(sys.argv[2]))
        elif sys.argv[1] == "list":
            if len(sys.argv) < 3:
                view_tasks()
            else:
                if sys.argv[2] == "done":
                    view_tasks(1)
                elif sys.argv[2] == "todo":
                    view_tasks(2)
                elif sys.argv[2] == "in-progress":
                    view_tasks(3)
    except (ValueError, IndexError):
        print("Enter correct ID")


if __name__ == "__main__":
    main()