tasks = []
def add_task():
    description_of_task = input("enter description of the task")
    due_date_of_task = input("enter due date of the task in the form dd-mm-yyyy")
    priority_of_task = int(input("enter priority of the task as 1 or 2 or 3 etc"))
    status_of_task = bool(input("enter status of the task True if completed or False "))
    new_task = {
        "description" : description_of_task,
        "due_date" : due_date_of_task,
        "priority" : priority_of_task,
        "status" : priority_of_task
    }
    tasks.append(new_task)
    print("task added successfully")
def display_task(task_num):
    if(task_num > len(tasks)):
        print("incorrect input")
    else:
        print(tasks[task_num])
        print("task removed successfully")
def remove_task(task_num):
    tasks.pop(0)
def update_task(task_num):
    description_of_task = input("enter new description of the task")
    due_date_of_task = input("enter new due date of the task in the form dd-mm-yyyy")
    priority_of_task = int(input("enter new priority of the task as 1 or 2 or 3 etc"))
    status_of_task = bool(input("enter new status of the task True if completed or False "))
    tasks[task_num].update({
        "description" : description_of_task,
        "due_date" : due_date_of_task,
        "priority" : priority_of_task,
        "status" : priority_of_task
    })
    print("task updated successfully")
t = 1
while(t != 0):
    print("1.add task\n 2.update task\n 3.remove tasks\n4.display tasks\n5.terminate")
    t = int(input("enter operation to perform"))
    if(t == 1):
        add_task()
    elif (t == 2):
        task_num = int(input("enter task number"))
        update_task(task_num)
    elif(t == 3):
        task_num = int(input("enter task number"))
        remove_task(task_num)
    elif(t == 4):
        task_num = int(input("enter task number"))
        display_task(task_num)
    elif(t == 5) :
        t = 0 
    else:
        print("incorect input")

        


