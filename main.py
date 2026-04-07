"""
FCFS Disk Scheduling Algorithm - Main Entry Point
A simulation of First Come First Serve disk scheduling for Operating Systems.
Submitted to: Er. Bhuvnesh Kumar

Team Members:
- Lovepreet Singh
- Navjot Singh
- Krish Sharma
- Mandeep Singh
"""

from fcfs import FCFSDiskScheduler
from visualizer import launch_interactive
from stack import Stack


DEFAULT_QUEUE = [98, 183, 37, 122, 14, 124, 65, 67]
DEFAULT_HEAD = 53

scheduler = None


def display_header():
    """
    Display project header with team information.
    """
    print("\n" + "=" * 60)
    print("        FCFS DISK SCHEDULING ALGORITHM SIMULATOR")
    print("=" * 60)
    print("\n  Submitted to: Er. Bhuvnesh Kumar")
    print("\n  Team Members:")
    print("    - Lovepreet Singh")
    print("    - Navjot Singh")
    print("    - Krish Sharma")
    print("    - Mandeep Singh")
    print("\n" + "-" * 60)


def display_menu():
    """
    Display the main CLI menu options.
    """
    print("\n----------- MAIN MENU -----------\n")
    print("  1. Run FCFS with Default Values (Interactive)")
    print("  2. Enter Custom Queue and Head Position")
    print("  3. Display Traversal Stack")
    print("  4. Pop Last Visited Position from Stack")
    print("  5. Reset")
    print("  6. View Current Graph")
    print("  7. Exit")
    print("\n----------------------------------")


def parse_input_list(input_str):
    """
    Parse a string input into a list of integers.
    
    Args:
        input_str (str): String like "[98, 183, 37, 122]"
        
    Returns:
        list: List of integers, or None if invalid.
    """
    try:
        cleaned = input_str.strip()
        if cleaned.startswith('[') and cleaned.endswith(']'):
            cleaned = cleaned[1:-1]
        numbers = [int(x.strip()) for x in cleaned.split(',')]
        return numbers
    except (ValueError, SyntaxError):
        return None


def run_with_defaults():
    """
    Run FCFS algorithm with default values in interactive mode.
    """
    global scheduler
    scheduler = FCFSDiskScheduler(DEFAULT_QUEUE, DEFAULT_HEAD)

    print("\n" + "=" * 55)
    print("         FCFS DISK SCHEDULING - DEFAULT VALUES")
    print("=" * 55)
    print(f"\n  Request Queue: {DEFAULT_QUEUE}")
    print(f"  Initial Head Position: {DEFAULT_HEAD}\n")

    total_movement, hops = scheduler.calculate_fcfs()
    scheduler.print_summary()

    final_queue, final_head = launch_interactive(DEFAULT_QUEUE.copy(), DEFAULT_HEAD)
    scheduler = FCFSDiskScheduler(final_queue, final_head)
    scheduler.calculate_fcfs()
    print(f"\n  Updated values from interactive mode:")
    print(f"  Queue: {final_queue}")
    print(f"  Head: {final_head}")


def run_custom():
    """
    Run FCFS algorithm with user-provided values.
    """
    global scheduler

    print("\n--- Custom Input ---")
    queue_input = input("Enter disk request queue (e.g., [98, 183, 37]): ")
    queue = parse_input_list(queue_input)

    if queue is None:
        print("  Invalid queue format. Please try again.")
        return

    if not queue:
        print("  Queue cannot be empty.")
        return

    try:
        head_input = input("Enter initial head position: ")
        head = int(head_input)
    except ValueError:
        print("  Invalid head position. Please enter an integer.")
        return

    scheduler = FCFSDiskScheduler(queue, head)

    print("\n" + "=" * 55)
    print("         FCFS DISK SCHEDULING - CUSTOM VALUES")
    print("=" * 55)
    print(f"\n  Request Queue: {queue}")
    print(f"  Initial Head Position: {head}\n")

    total_movement, hops = scheduler.calculate_fcfs()
    scheduler.print_summary()

    final_queue, final_head = launch_interactive(queue.copy(), head)
    scheduler = FCFSDiskScheduler(final_queue, final_head)
    scheduler.calculate_fcfs()
    print(f"\n  Updated values from interactive mode:")
    print(f"  Queue: {final_queue}")
    print(f"  Head: {final_head}")


def display_stack():
    """
    Display the current traversal stack contents.
    """
    global scheduler

    if scheduler is None:
        print("\n  No scheduler initialized. Please run Option 1 or 2 first.")
        return

    stack_contents = scheduler.get_traversal_stack()

    if not stack_contents:
        print("\n  Traversal stack is empty.")
        return

    print(f"\n  Traversal Stack (bottom to top):")
    print("  " + "-" * 30)
    for i, item in enumerate(stack_contents):
        print(f"    [{i}]  Cylinder: {item}")
    print("  " + "-" * 30)
    print(f"  Stack size: {len(stack_contents)}")


def pop_from_stack():
    """
    Pop the last visited position from the stack.
    """
    global scheduler

    if scheduler is None:
        print("\n  No scheduler initialized. Please run Option 1 or 2 first.")
        return

    popped, remaining = scheduler.pop_from_stack()

    if popped is None:
        print("\n  Stack is empty. Nothing to pop.")
        return

    print(f"\n  Popped value: {popped}")
    print(f"\n  Updated Traversal Stack:")
    print("  " + "-" * 30)
    for i, item in enumerate(remaining):
        print(f"    [{i}]  Cylinder: {item}")
    print("  " + "-" * 30)
    print(f"  Stack size: {len(remaining)}")


def reset_scheduler():
    """
    Reset the scheduler to initial state.
    """
    global scheduler
    scheduler = None
    print("\n  Scheduler has been reset.")


def view_current_graph():
    """
    View/redraw the current graph based on scheduler state.
    Allows seeing the graph after making CLI changes (pop, reset, etc.)
    """
    global scheduler

    if scheduler is None:
        print("\n  No scheduler initialized. Please run Option 1 or 2 first.")
        return

    queue = scheduler.request_queue
    head = scheduler.head_position

    if not queue:
        print("\n  Request queue is empty. Please add requests first.")
        return

    print("\n" + "=" * 55)
    print("         VIEWING CURRENT GRAPH")
    print("=" * 55)
    print(f"\n  Request Queue: {queue}")
    print(f"  Initial Head Position: {head}\n")

    scheduler.print_summary()

    launch_interactive(queue.copy(), head)
    scheduler.calculate_fcfs()
    print(f"\n  Current values preserved.")


def main():
    """
    Main entry point with CLI menu loop.
    """
    display_header()

    while True:
        display_menu()

        choice = input("  Enter your choice (1-7): ").strip()

        if choice == '1':
            run_with_defaults()
        elif choice == '2':
            run_custom()
        elif choice == '3':
            display_stack()
        elif choice == '4':
            pop_from_stack()
        elif choice == '5':
            reset_scheduler()
        elif choice == '6':
            view_current_graph()
        elif choice == '7':
            print("\n  Thank you for using FCFS Disk Scheduling Simulator!")
            print("  Exiting...\n")
            break
        else:
            print("\n  Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
