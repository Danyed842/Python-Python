tasks = [ ]
while True:
    print(1, "add task")
    print(2, "show task")
    print(3, "clean tasks")
    print(4, "exit")
    option = int(input("choose an option: "))
    if option == 1:
        add_task = input("put a task to add: ")
        tasks.append(add_task)
    elif option == 2:
        print(tasks)
    elif option == 3:
        tasks.clear()
        print("tasks cleaned")
    elif option == 4:
        print("Goodbye")
        break
    else:
        print("isn't a valid number")