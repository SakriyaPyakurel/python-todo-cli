import argparse 
import os  
import pyttsx3 
engine=pyttsx3.init()    
voices= engine.getProperty('voices') 
engine.setProperty('voice',voices[1].id)
def create_parser():
    parser = argparse.ArgumentParser(description="Command-line Todo List App")
    parser.add_argument("-a", "--add", metavar="", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="", help="Remove a task by name")
    parser.add_argument("-t", "--truncate",action="store_true", help="Remove all tasks")
    return parser
# python clitodo.py -a/--add  to add an task
def add_task(task):
    task = task.strip() 
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [t.strip() for t in file.readlines()]  
        if task not in tasks:
            with open("tasks.txt", "a") as file:
                if len(tasks) != 0:
                    file.write(f"\n{task}")
                else:
                    file.write(task)
            engine.say("Task added successfully.")
            engine.runAndWait()
        else:
            engine.say("Cannot add task as it already exists.")
            engine.runAndWait()
    else:
        with open("tasks.txt", "w") as file:
            file.write(task)
        engine.say("Task added successfully.")  
        engine.runAndWait()             
# python clitodo.py -l/--list to list all tasks
def list_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for index,task in enumerate(tasks):
                engine.say(f"task {index+1} {task}")
                engine.runAndWait()
    else:
        engine.say("No tasks found.")
        engine.runAndWait()
# python clitodo.py -r/--remove task_name to remove a task
def remove_task(task_name):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [t.strip() for t in file.readlines()]
        if task_name.strip() in tasks:
            with open("tasks.txt", "w") as file:
               for i, task in enumerate(tasks):
                  if tasks[i].strip()!=task_name.strip():
                    file.write(task+"\n")
            engine.say("Task removed successfully.")
            engine.runAndWait()
        else:
           engine.say("No task found with that name.")
           engine.runAndWait()
def truncate():
    with open("tasks.txt","r") as file:
        tasks=file.readlines()
    if len(tasks) != 0:
        with open("tasks.txt", "w") as file:
            file.write('')
        engine.say("Truncated successfully")
        engine.runAndWait()
    else:
        engine.say("theres no task to remove")
        engine.runAndWait()
#Driver code
def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.truncate:
        truncate()
    elif args.remove:
        remove_task(args.remove)
    else:
        parser.print_help()
        engine.say("Remember to seperate each word of a task with a single space while adding")
        engine.runAndWait()
if __name__ == "__main__":
    main()