from todo_list_manager import show_list, add_task_to_list, remove_task_from_list, move_task, move_task_to_other_list

kanban = {
    "backlog": [],
    "doing": [],
    "review": [],
    "done": [],
}

def move_task_up(current_position: int, list_name: str, new_position: int = None):
    """
    Move a task up to the next list or to a new position within the same list.
    
    :param current_position: The current position of the task in the list.
    :param list_name: The name of the list where the task is currently located.
    :param new_position: The new position to move the task to within the same list (optional).
    """
    if list_name not in ("backlog", "doing", "review", "done"):
        raise KeyError
    
    elif new_position is None:

        if list_name == "backlog":

            move_task_to_other_list(current_position, get_kanban()["backlog"], get_kanban()["doing"])

        elif list_name == "doing":

            move_task_to_other_list(current_position, get_kanban()["doing"], get_kanban()["review"])

        elif list_name == "review":

            move_task_to_other_list(current_position, get_kanban()["review"], get_kanban()["done"])
    
    elif current_position > (len(get_kanban()[list_name]) + 1) or current_position < 1:

        raise IndexError
    
    else:
        if list_name == "backlog":

            move_task_to_other_list(current_position, get_kanban()["backlog"], get_kanban()["doing"], new_position)
        
        elif list_name == "doing":

            move_task_to_other_list(current_position, get_kanban()["doing"], get_kanban()["review"], new_position)
        
        elif list_name == "review":

            move_task_to_other_list(current_position, get_kanban()["review"], get_kanban()["done"], new_position)

def move_task_down(current_position: int, list_name: str, new_position: int = None):
    """
    Move a task down to the previous list or to a new position within the same list.
    
    :param current_position: The current position of the task in the list.
    :param list_name: The name of the list where the task is currently located.
    :param new_position: The new position to move the task to within the same list (optional).
    """
    if list_name not in ("backlog", "doing", "review", "done"):

        raise KeyError
    
    elif new_position is not None and (current_position > (len(kanban.get(list_name)) + 1) or current_position < 1):
        
        raise IndexError
    
    else:

        if list_name == "done":

            move_task_to_other_list(current_position, kanban.get("done"), kanban.get("review"), new_position)
        
        elif list_name == "review":

            move_task_to_other_list(current_position, kanban.get("review"), kanban.get("doing"), new_position)
        
        elif list_name == "doing":

            move_task_to_other_list(current_position, kanban.get("doing"), kanban.get("backlog"), new_position)

def change_task_priority(current_position: int, new_position: int, list_name: str):
    """
    Change the priority of a task within the same list.
    
    :param current_position: The current position of the task in the list.
    :param new_position: The new position to move the task to within the same list.
    :param list_name: The name of the list where the task is currently located.
    """
    if list_name not in ("backlog", "doing", "review", "done"):

        raise KeyError
    
    elif current_position > (len(get_kanban()[list_name]) + 1) or current_position < 1 or new_position > (len(get_kanban()[list_name]) + 1) or new_position < 1:
        
        raise IndexError
    
    else:

        move_task(current_position, new_position, get_kanban()[list_name])

def add_new_task(task: str):
    """
    Add a new task to the 'backlog' list.
    
    :param task: The task description to be added.
    """
    add_task_to_list(task, get_kanban()["backlog"])

def remove_task(position: int, list_name: str):
    """
    Remove a task from a specified list.
    
    :param position: The position of the task in the list.
    :param list_name: The name of the list where the task is currently located.
    """
    if list_name not in ("backlog", "doing", "review", "done"):

        raise KeyError
    
    elif position > (len(get_kanban()[list_name]) + 1) or position < 1:

        raise IndexError
    
    else:

        remove_task_from_list(position, get_kanban()[list_name])

def apply_task_limit(limit_amount: int):
    """
    Apply a limit to the number of tasks in the 'doing' list.
    
    :param limit_amount: The maximum number of tasks allowed in the 'doing' list.
    """
    while len(get_kanban()["doing"]) > limit_amount:
        
        move_task_to_other_list(len(get_kanban()["doing"]), get_kanban()["doing"], get_kanban()["backlog"])

def get_kanban():
    """
    Get the current state of the Kanban board.
    
    :return: The Kanban board dictionary.
    """
    return kanban

def show_kanban():
    """
    Display the current state of the Kanban board.
    """
    print("Backlog")
    show_list(get_kanban()["backlog"])
    
    print("\nDoing")
    show_list(get_kanban()["doing"])
    
    print("\nReview")
    show_list(get_kanban()["review"])
    
    print("\nDone")
    show_list(get_kanban()["done"])
