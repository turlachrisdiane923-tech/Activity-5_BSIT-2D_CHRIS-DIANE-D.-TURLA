# Activity-5_BSIT-2D_CHRIS-DIANE-D.-TURLA
# Module 5 - Stacks and Queues

## Project Description
This project demonstrates two fundamental data structures: stacks and queues. It includes array-based and linked-list-based implementations, a menu-driven test program, a balanced-parentheses checker, and a print-queue simulation.

## Project Files
- `array_stack.py` - Array-based stack with push, pop, peek, is_empty, and is_full.
- `linked_stack.py` - Linked-list-based stack.
- `array_queue.py` - Circular array queue.
- `linked_queue.py` - Linked-list-based queue.
- `test_driver.py` - Menu-driven program for testing all implementations and application exercises.
- `analysis.md` - Written answer to the analysis question.\n- `sample_runs.md` - Example tests for underflow, overflow, wrap-around, and application exercises.

## Requirements
- Python 3 installed on your computer.
- No external Python packages are required.

## How to Run
1. Download or clone this repository.
2. Open the project folder in VS Code or a terminal.
3. Run the following command:

   `python test_driver.py`

   On some computers, use:

   `python3 test_driver.py`

4. Follow the menu and enter your choices.

## How to Test the Programs
- Choose **1. Array Stack** to test push, pop, peek, empty, and full operations.
- Choose **2. Linked Stack** to test linked-list stack operations.
- Choose **3. Circular Array Queue** to test enqueue, dequeue, peek front, empty, and full operations. To demonstrate wrap-around, use a small capacity such as 3, enqueue three values, dequeue one or two values, then enqueue additional values.
- Choose **4. Linked Queue** to test linked-list queue operations.
- Choose **5. Balanced Parentheses Exercise** to test strings containing `()`, `[]`, and `{}`.
- Choose **6. Print Queue Simulation** to add print jobs and process them in FIFO order.

## Error Handling
The print queue simulation uses the linked queue implementation to process jobs in FIFO order.\n\nThe program reports stack or queue underflow when a removal or peek operation is attempted on an empty structure. The fixed-size array implementations also report overflow when an insertion is attempted while full.

## Sample Test Cases
- Balanced: `({[]})` -> `Balanced`
- Not balanced: `({[})` -> `Not Balanced`
- Print queue: add jobs `J01`, `J02`, and `J03`; they should be processed in that same order.

## Author
Name: Chris Diane Turla 
Section: BSIT-2D 
