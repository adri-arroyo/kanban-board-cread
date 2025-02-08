import todo_list_manager as tlm

# Initialize the todo list
todo_list = ["Clean house", "Take pet to vet", "Cook lunch", "Call mom"]
print("Initial todo list")
tlm.show_list(todo_list)

# Add tasks to the list
print("Adding task 'Call Dad' without position")
tlm.add_task_to_list("Call dad", todo_list)
print("Adding task 'Call son' at position 2")
tlm.add_task_to_list("Call son", todo_list, 2)
print("Adding task 'Dye hair' at position 1")
tlm.add_task_to_list("Dye hair", todo_list, 1)
print("Adding task 'Pick up outfit' at position 8")
tlm.add_task_to_list("Pick up outfit", todo_list, 8)

# Attempt to add tasks at invalid positions
print("Adding task 'Cook dinner' at position 0, should get an error")
try:
    tlm.add_task_to_list("Cook dinner", todo_list, 0)
except IndexError as e:
    print(e)
print("Adding task 'Cook dinner' at position 15, should get an error")
try:
    tlm.add_task_to_list("Cook dinner", todo_list, 15)
except IndexError as e:
    print(e)

# Show the updated todo list
tlm.show_list(todo_list)

# Remove tasks from the list
print("Removing task at position 1 ('Dye hair')")
tlm.remove_task_from_list(1, todo_list)
print("Removing task at position 4 ('Cook lunch')")
tlm.remove_task_from_list(4, todo_list)
print("Removing task at position 2 ('Call son')")
tlm.remove_task_from_list(2, todo_list)

# Attempt to remove tasks at invalid positions
print("Removing task at position 0, should get an error")
try:
    tlm.remove_task_from_list(0, todo_list)
except IndexError as e:
    print(e)
print("Removing task at position 18, should get an error")
try:
    tlm.remove_task_from_list(18, todo_list)
except IndexError as e:
    print(e)

# Show the updated todo list
tlm.show_list(todo_list)

# Move tasks within the list
print("Moving task at position 1 ('Clean house') to position 3")
tlm.move_task(1, 3, todo_list)
print("Moving task at position 5 ('Pickup outfit') to position 1")
tlm.move_task(5, 1, todo_list)

# Attempt to move tasks to invalid positions
print("Moving task at position 0 to 2, should throw an error")
try:
    tlm.move_task(0, 2, todo_list)
except IndexError as e:
    print(e)
print("Moving task at position 17 to 2, should throw an error")
try:
    tlm.move_task(17, 2, todo_list)
except IndexError as e:
    print(e)
print("Moving task at position 2 to 0, should throw an error")
try:
    tlm.move_task(2, 0, todo_list)
except IndexError as e:
    print(e)
print("Moving task at position 1 to 13, should throw an error")
try:
    tlm.move_task(1, 13, todo_list)
except IndexError as e:
    print(e)

# Show the updated todo list
tlm.show_list(todo_list)

# Initialize a second todo list
todo_list2 = ["Mow the lawn", "Pick up dog from puppy daycare", "Pay parking ticket", 
              "Go buy paint at HomeDepot using the giftcard mother in law gave me for christmas."]
print("Show new list with new tasks which are longer.")
tlm.show_list(todo_list2)

# Move tasks between lists
print("Move task 2 ('Take pet to vet') to second list, no position given")
tlm.move_task_to_other_list(2, todo_list, todo_list2)
print("Move task 3 ('Clean house') to second list at position 2")
tlm.move_task_to_other_list(3, todo_list, todo_list2, 2)

# Show both todo lists
print("Show both todo lists")
tlm.show_list(todo_list)
tlm.show_list(todo_list2)

# Get tasks from the lists
print("Getting task at position 3 from first list")
print(tlm.get_task(3, todo_list))
print("Getting task at position 4 from second list")
print(tlm.get_task(4, todo_list2))