import unittest
import todo_list_manager as tlm

class TestTodoListManager(unittest.TestCase):
    
    def setUp(self):
        """
        Set up initial conditions for the tests.
        """
        self.todo_list = ["Clean house", "Take pet to vet", "Cook lunch", "Call mom"]
        self.todo_list2 = ["Mow the lawn", "Pick up dog from puppy daycare", "Pay parking ticket", 
                           "Go buy paint at HomeDepot using the giftcard mother in law gave me for christmas."]
        self.todo_list3 = ["Dye hair", "Clean house", "Call son", "Take pet to vet", "Cook lunch", "Call mom", "Call dad", "Pick up outfit"]
        self.todo_list4 = ["Clean house", "Take pet to vet", "Call mom", "Call dad", "Pick up outfit"]
        self.todo_list5 = ["Pick up outfit", "Take pet to vet", "Call mom", "Clean house", "Call dad"]

    def test_add_task_to_list(self):
        """
        Test adding tasks to the list at various positions.
        """
        tlm.add_task_to_list("Call dad", self.todo_list)
        self.assertEqual(self.todo_list[-1], "Call dad")

        tlm.add_task_to_list("Call son", self.todo_list, 2)
        self.assertEqual(self.todo_list[1], "Call son")

        tlm.add_task_to_list("Dye hair", self.todo_list, 1)
        self.assertEqual(self.todo_list[0], "Dye hair")

        tlm.add_task_to_list("Pick up outfit", self.todo_list, 8)
        self.assertEqual(self.todo_list[7], "Pick up outfit")

        with self.assertRaises(IndexError):
            tlm.add_task_to_list("Cook dinner", self.todo_list, 0)

        with self.assertRaises(IndexError):
            tlm.add_task_to_list("Cook dinner", self.todo_list, 15)

    def test_remove_task_from_list(self):
        """
        Test removing tasks from the list at various positions.
        """
        tlm.remove_task_from_list(1, self.todo_list3)
        self.assertNotIn("Dye hair", self.todo_list3)

        tlm.remove_task_from_list(4, self.todo_list3)
        self.assertNotIn("Cook lunch", self.todo_list3)

        tlm.remove_task_from_list(2, self.todo_list3)
        self.assertNotIn("Call son", self.todo_list3)

        with self.assertRaises(IndexError):
            tlm.remove_task_from_list(0, self.todo_list3)

        with self.assertRaises(IndexError):
            tlm.remove_task_from_list(18, self.todo_list3)

    def test_move_task(self):
        """
        Test moving tasks within the same list.
        """
        tlm.move_task(1, 3, self.todo_list4)
        self.assertEqual(self.todo_list4[2], "Clean house")

        tlm.move_task(5, 1, self.todo_list4)
        self.assertEqual(self.todo_list4[0], "Pick up outfit")

        with self.assertRaises(IndexError):
            tlm.move_task(0, 2, self.todo_list4)

        with self.assertRaises(IndexError):
            tlm.move_task(17, 2, self.todo_list4)

        with self.assertRaises(IndexError):
            tlm.move_task(2, 0, self.todo_list4)

        with self.assertRaises(IndexError):
            tlm.move_task(1, 13, self.todo_list4)

    def test_get_task(self):
        """
        Test retrieving tasks from the list.
        """
        self.assertEqual(tlm.get_task(3, self.todo_list), "Cook lunch")
        self.assertEqual(tlm.get_task(4, self.todo_list2), "Go buy paint at HomeDepot using the giftcard mother in law gave me for christmas.")

    def test_move_task_to_other_list(self):
        """
        Test moving tasks from one list to another.
        """
        tlm.move_task_to_other_list(2, self.todo_list5, self.todo_list2)
        self.assertIn("Take pet to vet", self.todo_list2)
        self.assertNotIn("Take pet to vet", self.todo_list5)

        tlm.move_task_to_other_list(3, self.todo_list5, self.todo_list2, 2)
        self.assertEqual(self.todo_list2[1], "Clean house")
        self.assertNotIn("Clean house", self.todo_list5)

if __name__ == '__main__':
    unittest.main()
