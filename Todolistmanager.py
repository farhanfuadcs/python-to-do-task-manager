import json


filename="loadtask.json"

def load_task():
    try:
        with open (filename,'r') as f:
            return json.load(f)
    except:
        return {"tasks": []}


def save_task(tasks):
    try:
        with open (filename,'w') as f:
             json.dump(tasks,f)
    except:
        print("Failed to save!")



def add_task(tasks):
    addtask=input("Enter the task name: ")
    if addtask:
        tasks['tasks'].append({"description": addtask, "complete": False})
        print("Task Added!")
        save_task(tasks)
    else:
        print("Something is wrong!")


def view_task(tasks):
    if len(tasks['tasks'])!=0:
        for i,task in enumerate(tasks['tasks']):
            status="Complete" if task['complete'] else "Pending"
            print(f"{i+1}.{task['description']} | {status}")
    else:
        print("No task added yet!")


def mark_task(tasks):
    view_task(tasks)
    try:
        mark=int(input("Enter the task number that is completed: "))
        if 1<=mark<=len(tasks['tasks']):
            tasks['tasks'][mark-1]['complete']=True
            print("Task marked as complete!")
            save_task(tasks)
        else:
            print("Invalid Input!")
    except:
        print("Enter a valid number!")



def delete_task(tasks):
    view_task(tasks)
    try:
        delete=int(input("Enter the task number you want to delete: "))
        if 1<=delete<=len(tasks['tasks']):
            tasks['tasks'].pop(delete-1)
            print("Task deleted!")
            save_task(tasks)
        else:
            print("Invalid Input!")
    except:
        print("Enter a valid number!")




def main():
    tasks=load_task()
    print("Welcome to TO-Do-Task-Manager")
    while True:
        print("1.Add Task\n2.View Task\n3.Mark Task\n4.Deleter Task\n5.Exit")
        user=input("Enter your choice(1-4): ")
        if user=="1":
            add_task(tasks)
        elif user=="2":
            view_task(tasks)
        elif user=="3":
            mark_task(tasks)
        elif user=="4":
            delete_task(tasks)
        elif user=="5":
            break
        else:
            print("Invalid Choice!")



main()