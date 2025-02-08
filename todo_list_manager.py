def add_task_to_list(task: str, todo_list: list, position: int = None):
    """
    Adds a task to the specified position in the list, or at the end if no position is specified.
    
    :param task: The task description to be added.
    :param todo_list: The list to which the task will be added.
    :param position: The position at which to add the task (optional).
    """
    if position is None:

        todo_list.append(task)

    elif position > (len(todo_list) + 1) or position < 1:

        raise IndexError(f"{position} is an invalid position for to do list of size {len(todo_list)}")
    
    else:

        todo_list.insert(position - 1, task)

def remove_task_from_list(position: int, todo_list: list):
    """
    Removes a task from the specified position in the list.
    
    :param position: The position of the task to be removed.
    :param todo_list: The list from which the task will be removed.
    """

    if position > (len(todo_list) + 1) or position < 1:

        raise IndexError(f"{position} is an invalid position for to do list of size {len(todo_list)}")
    
    else:

        todo_list.pop(position - 1)

def move_task(position1: int, position2: int, todo_list: list):
    """
    Moves a task from one position to another within the same list.
    
    :param position1: The current position of the task.
    :param position2: The new position to move the task to.
    :param todo_list: The list containing the task.
    """

    if position1 > (len(todo_list) + 1) or position1 < 1 or position2 > (len(todo_list) + 1) or position2 < 1:
        
        raise IndexError(f"Invalid positions for to do list of size {len(todo_list)}")
    
    else:
        
        temp = todo_list[position1 - 1]
        todo_list.pop(position1 - 1)
        todo_list.insert(position2 - 1, temp)

def move_task_to_other_list(position1: int, todo_list1: list, todo_list2: list, position2: int = None):
    """
    Moves a task from one list to another, optionally to a specified position in the new list.
    
    :param position1: The current position of the task in the original list.
    :param todo_list1: The original list containing the task.
    :param todo_list2: The new list to which the task will be moved.
    :param position2: The position in the new list to move the task to (optional).
    """
    if position1 > (len(todo_list1) + 1) or position1 < 1:

        raise IndexError(f"{position1} is an invalid position for to do list of size {len(todo_list1)}")
    
    elif position2 is None:

        todo_list2.append(todo_list1[position1 - 1])
        todo_list1.pop(position1 - 1)
    
    elif position2 > (len(todo_list2) + 1) or position2 < 1:

        raise IndexError(f"{position2} is an invalid position for to do list of size {len(todo_list2)}")
    
    else:

        todo_list2.insert(position2 - 1, todo_list1[position1 - 1])
        todo_list1.pop(position1 - 1)

def get_task(position: int, todo_list: list):
    """
    Returns the task located at the specified position in the list.
    
    :param position: The position of the task to be retrieved.
    :param todo_list: The list containing the task.
    :return: The task at the specified position.
    """

    if position > (len(todo_list) + 1) or position < 1:

        raise IndexError(f"{position} is an invalid position for to do list of size {len(todo_list)}")
    
    else:

        return todo_list[position - 1]

def show_list(todo_list: list):
    """
    Prints the content of the todo list in a formatted manner.
    
    :param todo_list: The list to be displayed.
    """
    
    print("_" * 34)

    for pos, task in enumerate(todo_list, start=1):

        task = str(pos) + ". " + task

        if len(task) > 30:
            task_str1 = task[:29]
            task_str2 = task[29:]

            while len(task_str2) > 30:

                print(f"| {task_str1}- |")
                task_str1 = task_str2[:29]
                task_str2 = task_str2[29:]

            print(f"| {task_str1}- |")

            wspace = " " * (30 - len(task_str2))

            print(f"| {task_str2}{wspace} |")
        
        else:

            wspace = " " * (30 - len(task))
            print(f"| {task}{wspace} |")
            
    print("_" * 34)
