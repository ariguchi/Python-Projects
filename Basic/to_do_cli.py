
tasks = []

def manage_tasks():
    for i in range(len(tasks)):
        print(i+1, '.', tasks[i])


while True:
    ch = int(input(' 1. Add task\n 2. See tasks\n 3. Delete tasks\n 4. Exit\n'))
    if ch == 1:
        add = input('Enter task')
        tasks.append(add)
    elif ch == 2:
        manage_tasks()
    elif ch == 3:
        manage_tasks()
        rem = int(input('Enter task to be removed'))
        del tasks[rem-1]
    elif ch == 4:
        break
