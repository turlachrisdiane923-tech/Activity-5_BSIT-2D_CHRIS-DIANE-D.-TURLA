from linked_stack import LinkedStack
from linked_queue import LinkedQueue

def check_balanced_parentheses(text):
    """Application Exercise 6a: Checks if a string of parentheses is balanced."""
    stack = LinkedStack()
    pairs = {")": "(", "]": "[", "}": "{"}
    
    for char in text:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


def run_print_queue_simulation():
    """Application Exercise 6b: Simulates a printer queue."""
    queue = LinkedQueue()
    print("\n--- Starting Print Queue Simulation ---")
    
    jobs = [("Job_X", 8), ("Job_Y", 3), ("Job_Z", 12)]
    for job_id, pages in jobs:
        queue.enqueue((job_id, pages))
        print(f"Enqueued to print: {job_id} ({pages} pages)")
        
    print(f"Current Queue Status: {queue}")
    
    wait_order = 1
    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        print(f"[Wait Order #{wait_order}] Currently printing {job_id}...")
        wait_order += 1
    print("All print jobs have been processed successfully.\n")
