
# contains list about task
tasks = []


def menu():
    c = 0
    while c<1 or c>4:
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task complete")
        print("4. List the tasks")
        print("")
        c = int(input("What would you like to do? "))
        if c<1 or c>4:
            print("Invalid choice")
            print("")
    return c

def addTask():
    name = input('Enter task: ')
    tasks.append((name, False))
    print("")

def removeTask():
    listTask(True)
    c = int(input("Which task do you want to remove? "))
    if c>=1 and c<=len(tasks):
       tasks.pop(c - 1)
    print("")

def markTask():
    listTask(False)
    c = int(input("Which task do you want to mark complete? "))

    n = 0
    # Find c-th not completed task 
    for t in tasks:
        if not t[1]:
            if c > 1:
                 # Decrement counter 
                 c = c - 1
            else:
                 # Mark as Complete if found
                 tasks[n] = (t[0], True)
                 print("")
                 return
        n = n + 1
    print("")    


def listTask(showComplete):
    n = 1
    for t in tasks:
        if t[1]:
            if showComplete:
                print(str(n) + ". " + t[0] + " (COMPLETE)")
                n = n + 1
        else:
            print(str(n) + ". " + t[0])
            n = n + 1

    print("")


while True:
    c = menu()
    if c == 1:
       addTask()
    if c == 2:
       removeTask()
    if c == 3:
       markTask()
    if c == 4:
       listTask(True)