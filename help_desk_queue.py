# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value
    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next


    
    


def run_help_desk():
    # Create an instance of the Queue class
    run_help_desk = Queue()
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            run_help_desk.enqueue(name)
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            helped_customer = run_help_desk.dequeue()
            if helped_customer:
                print(f"Helped: {helped_customer}")
            else:
                print("No customer to help")



        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            peek_name = run_help_desk.peek()
            if peek_name:
                print(f"Next customer: {peek_name}")
            else:
                print("No customers in queue")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            run_help_desk.print_queue()
        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

'''
Why is a stack the right choice for undo/redo?
Stack is the right choice for undo/redo because of the principle of Last In First Out, this means that the last value that
the last value added into the stack will be the first one to be modified (undo/redo). Using stacks helps to maintain the order becoming easier to manage.
Why is a queue better suited for the help desk?
Queue is better because insted of being LIFO, it's going to be FIFO. This means First In First Out, this means that the first value that
the first value added into the queue will be the first one to be modified. In the help desk case you need to modify the first person in queue
because you need to help the first person to get to the desk.
How do your implementations differ from Python’s built-in lists?
This node implementation of stack and queue allows faster modification. If you used Python's built-in lists you would need to access elements by index
and it would make less efficient and slower. 
'''