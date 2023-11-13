from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []
completed = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            add_task(request.form)
        elif action == 'remove':
            task_num = int(request.form.get('task_num'))
            if task_num and 1 <= task_num <= len(tasks):
                remove_task(task_num)
        elif action == 'update':
            task_num = int(request.form.get('task_num'))
            if task_num and 1 <= task_num <= len(tasks):
                update_task(task_num, request.form)

    incomplete_tasks = [task for task in tasks if not task['status']]
    completed_tasks = [task for task in tasks if task['status']]

    return render_template('index.html', tasks=incomplete_tasks, completed=completed_tasks)

def add_task(form_data):
    description_of_task = form_data.get('description')
    due_date_of_task = form_data.get('due_date')
    priority_of_task = form_data.get('priority')
    status_of_task = form_data.get('status')

    # Ensure due_date_of_task is parsed as a string in the desired format for display
    if due_date_of_task:
        due_date_of_task = due_date_of_task.replace("T", " ")

    new_task = {
        "description": description_of_task,
        "due_date": due_date_of_task,
        "priority": priority_of_task,
        "status": status_of_task == 'True'
    }
    tasks.append(new_task)

def remove_task(task_num):
    if task_num <= len(tasks):
        tasks.pop(task_num - 1)  # Adjusting for 0-based indexing

def update_task(task_num, form_data):
    task = tasks[task_num - 1]

    description_of_task = form_data.get('description')
    due_date_of_task = form_data.get('due_date')
    priority_of_task = form_data.get('priority')
    status_of_task = form_data.get('status')

    if description_of_task:
        task['description'] = description_of_task
    if due_date_of_task:
        task['due_date'] = due_date_of_task
    if priority_of_task:
        task['priority'] = int(priority_of_task)
    if status_of_task == 'True':
        task['status'] = True
        completed.append(tasks.pop(task_num - 1))

if __name__ == '__main__':
    app.run(debug=True)
