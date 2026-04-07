"""
FCFS Disk Scheduling Algorithm Implementation
First Come First Serve (FCFS) is the simplest disk scheduling algorithm.
Requests are serviced in the order they arrive in the disk queue.
"""

from stack import Stack


class FCFSDiskScheduler:
    """
    Implements the First Come First Serve (FCFS) Disk Scheduling Algorithm.

    Attributes:
        request_queue (list): List of cylinder requests in arrival order.
        head_position (int): Initial head position on the disk.
        traversal_stack (Stack): Custom stack to record visited cylinders.
    """

    def __init__(self, request_queue, head_position):
        """
        Initialize the FCFS Disk Scheduler.

        Args:
            request_queue (list): List of disk cylinder requests.
            head_position (int): Initial head position (starting point).
        """
        self.request_queue = request_queue.copy()
        self.head_position = head_position
        self.traversal_stack = Stack()
        self.hops = []

    def calculate_fcfs(self):
        """
        Process the disk requests using FCFS algorithm.

        Uses the custom Stack to push each visited cylinder position.
        Calculates the distance between consecutive head movements.

        Returns:
            tuple: (total_head_movement, list of hops)
        """
        current_head = self.head_position
        self.traversal_stack.clear()
        self.hops = []

        for step, request in enumerate(self.request_queue, start=1):
            distance = abs(request - current_head)
            direction = "→" if request > current_head else "←"

            hop = {
                "step": step,
                "from": current_head,
                "to": request,
                "distance": distance,
                "direction": direction,
            }
            self.hops.append(hop)

            self.traversal_stack.push(current_head)

            print(
                f"Step {step}: Head moved {current_head} {direction} {request} | Distance: {distance}"
            )

            current_head = request

        self.traversal_stack.push(current_head)

        total_head_movement = sum(hop["distance"] for hop in self.hops)

        return total_head_movement, self.hops

    def print_summary(self):
        """
        Print a formatted summary table of all head movements.
        """
        total = sum(hop["distance"] for hop in self.hops)

        print("\n" + "=" * 55)
        print(f"{'Step':<8}{'From':<10}{'To':<10}{'Distance':<10}{'Direction'}")
        print("-" * 55)

        for hop in self.hops:
            print(
                f"{hop['step']:<8}{hop['from']:<10}{hop['to']:<10}{hop['distance']:<10}{hop['direction']}"
            )

        print("-" * 55)
        print(f"{'TOTAL HEAD MOVEMENT':<40}{total}")
        print("=" * 55)

    def get_traversal_stack(self):
        """
        Get a copy of the traversal stack.

        Returns:
            list: Copy of all visited cylinder positions.
        """
        return self.traversal_stack.display()

    def pop_from_stack(self):
        """
        Pop the last visited position from the traversal stack.

        Returns:
            tuple: (popped_item, remaining_stack)
        """
        if self.traversal_stack.is_empty():
            return None, self.traversal_stack.display()

        popped = self.traversal_stack.pop()
        return popped, self.traversal_stack.display()

    def reset(self):
        """Reset the scheduler to initial state."""
        self.traversal_stack.clear()
        self.hops = []
