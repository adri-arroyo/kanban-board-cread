import kanban_manager

def main():
    """
    Main function to test task initialization and manage the Kanban board.
    """
    tasks = [
        "Update UI for main page", "Add darkmode feature", "Update user manual", "Fix bug ticket#214946",
        "Fix bug ticket#214762", "Updating color scheme for login page", "Fix infinite loop in main page",
        "Fix bug ticket#123567", "Updated DB to include birthdates", "Updated modify button",
        "Fix bug ticket#159487", "Update UI to include cancel button", "Revert last update", "Fix bug ticket#214762", 
        "Fix bug ticket#265812", "Add form for soliciting customer support", "Fix bug ticket#126985"
    ]
    
    # Add all the tasks to the Kanban board
    for task in tasks:
        kanban_manager.add_new_task(task)
    
    total_num_tasks = len(tasks)

    # Move tasks to the 'backlog' column
    for position in range(total_num_tasks, 4, -1):
        kanban_manager.move_task_up(position, "backlog")

    # Move tasks to the 'doing' column
    for position in range(total_num_tasks - 4, 3, -1):
        kanban_manager.move_task_up(position, "doing")
        
    # Move tasks to the 'review' column
    for position in range(total_num_tasks - 7, 3, -1):
        kanban_manager.move_task_up(position, "review")

    # Display the current state of the Kanban board
    kanban_manager.show_kanban()

if __name__ == "__main__":
    main()
