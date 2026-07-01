tasks = []

while True:
    print("\n TO DO LIST ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No Tasks Available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No Tasks to Remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to remove: "))

            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task Removed Successfully!")
            else:
                print("Invalid Task Number")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")