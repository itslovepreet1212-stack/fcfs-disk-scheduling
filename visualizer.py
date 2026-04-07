"""
Interactive FCFS Disk Scheduling Visualizer
Real-time visualization with sliders and controls.
"""

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox, RadioButtons
import matplotlib.patches as mpatches
import numpy as np
from fcfs import FCFSDiskScheduler


class InteractiveFCFSVisualizer:
    """
    Interactive FCFS Disk Scheduling visualizer with real-time updates.
    Allows adjusting head position and queue values via sliders and text inputs.
    """

    def __init__(self, initial_queue, initial_head):
        """
        Initialize the interactive visualizer.
        
        Args:
            initial_queue (list): Initial disk request queue.
            initial_head (int): Initial head position.
        """
        self.initial_queue = initial_queue
        self.current_head = initial_head
        self.initial_head = initial_head
        self.max_cylinder = 200

        self.fig, self.ax = plt.subplots(figsize=(16, 10))
        self.fig.canvas.manager.set_window_title('FCFS Disk Scheduling - Interactive')

        self._setup_ui()
        self.update(None)

        plt.subplots_adjust(left=0.15, right=0.95, top=0.92, bottom=0.25)

    def _setup_ui(self):
        """Setup the user interface with sliders, buttons, and text inputs."""
        ax_head = plt.axes([0.2, 0.15, 0.65, 0.03])
        self.head_slider = Slider(
            ax=ax_head,
            label='Head Position',
            valmin=0,
            valmax=self.max_cylinder,
            valinit=self.initial_head,
            valfmt='%0.0f'
        )
        self.head_slider.on_changed(self.update)

        self.add_queue_btn = Button(plt.axes([0.05, 0.05, 0.12, 0.04]), 'Add Request')
        self.add_queue_btn.on_clicked(self.add_queue_dialog)

        self.remove_queue_btn = Button(plt.axes([0.18, 0.05, 0.12, 0.04]), 'Remove Last')
        self.remove_queue_btn.on_clicked(self.remove_last)

        self.reset_btn = Button(plt.axes([0.31, 0.05, 0.12, 0.04]), 'Reset All')
        self.reset_btn.on_clicked(self.reset)

        self.clear_queue_btn = Button(plt.axes([0.44, 0.05, 0.12, 0.04]), 'Clear Queue')
        self.clear_queue_btn.on_clicked(self.clear_queue)

        self.queue_display_ax = plt.axes([0.02, 0.22, 0.25, 0.15])
        self.queue_display_ax.axis('off')
        self.queue_text = self.queue_display_ax.text(
            0.05, 0.95, '', transform=self.queue_display_ax.transAxes,
            fontsize=10, verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8)
        )

        self.max_cyl_slider_ax = plt.axes([0.2, 0.10, 0.65, 0.03])
        self.max_cyl_slider = Slider(
            ax=self.max_cyl_slider_ax,
            label='Max Cylinder',
            valmin=50,
            valmax=500,
            valinit=self.max_cylinder,
            valfmt='%0.0f'
        )
        self.max_cyl_slider.on_changed(self.update_max_cylinder)

    def update(self, val):
        """Update the graph with current slider values."""
        self.ax.clear()

        head = int(self.head_slider.val)
        self.current_head = head
        queue = self.get_current_queue()

        if not queue:
            self.ax.text(0.5, 0.5, 'Add requests to visualize FCFS',
                         ha='center', va='center', fontsize=16,
                         transform=self.ax.transAxes)
            self.ax.set_xlim(-5, self.max_cylinder + 10)
            self.ax.set_ylim(-1, 2)
            self._configure_axis(head)
            self.fig.canvas.draw_idle()
            return

        scheduler = FCFSDiskScheduler(queue, head)
        total, hops = scheduler.calculate_fcfs()

        cylinders = [head] + [hop['to'] for hop in hops]
        steps = list(range(len(cylinders)))

        colors = plt.cm.viridis(np.linspace(0, 1, len(cylinders)))

        self.ax.plot(cylinders, steps, 'o-', color='#2E86AB', linewidth=2.5,
                     markersize=12, zorder=3)

        for i in range(len(cylinders) - 1):
            start_x, end_x = cylinders[i], cylinders[i + 1]
            start_y, end_y = steps[i], steps[i + 1]

            self.ax.annotate('',
                           xy=(end_x, end_y),
                           xytext=(start_x, start_y),
                           arrowprops=dict(arrowstyle='->',
                                         color='#E74C3C',
                                         lw=2.5,
                                         mutation_scale=20),
                           zorder=2)

        for i, (cyl, step) in enumerate(zip(cylinders, steps)):
            self.ax.scatter(cyl, step, color=colors[i], s=250, zorder=4,
                          edgecolors='white', linewidth=2)
            self.ax.annotate(f'{cyl}',
                           xy=(cyl, step),
                           xytext=(7, 7),
                           textcoords='offset points',
                           fontsize=11,
                           fontweight='bold',
                           color='#2C3E50',
                           zorder=5)

        self.ax.set_title(f'FCFS Disk Scheduling | Total Head Movement: {total}',
                         fontsize=16, fontweight='bold', pad=15)

        self._configure_axis(head)

        info_text = f'Queue: {queue}\nHead: {head}\nTotal Movement: {total}'
        self.ax.text(0.02, 0.98, info_text,
                    transform=self.ax.transAxes,
                    fontsize=10,
                    verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))

        self.fig.canvas.draw_idle()

    def _configure_axis(self, head):
        """Configure axis labels and grid."""
        self.ax.set_xlabel('Cylinder Number', fontsize=12, fontweight='bold')
        self.ax.set_ylabel('Time Step', fontsize=12, fontweight='bold')
        self.ax.set_xlim(-5, self.max_cylinder + 10)
        self.ax.grid(True, linestyle='--', alpha=0.7, zorder=1)
        self.ax.set_facecolor('#F8F9FA')

    def get_current_queue(self):
        """Get current queue values from the display."""
        return self.initial_queue.copy()

    def add_queue_dialog(self, event):
        """Show dialog to add a new queue value."""
        new_value = self._get_input_value("Enter new cylinder request (0-500):")
        if new_value is not None:
            self.initial_queue.append(new_value)
            self.update_queue_display()
            self.update(None)

    def remove_last(self, event):
        """Remove the last queue value."""
        if self.initial_queue:
            removed = self.initial_queue.pop()
            print(f"Removed: {removed}")
            self.update_queue_display()
            self.update(None)
        else:
            print("Queue is already empty!")

    def clear_queue(self, event):
        """Clear all queue values."""
        self.initial_queue = []
        self.update_queue_display()
        self.update(None)

    def reset(self, event):
        """Reset to initial values."""
        self.initial_queue = [98, 183, 37, 122, 14, 124, 65, 67]
        self.initial_head = 53
        self.head_slider.reset()
        self.max_cylinder = 200
        self.max_cyl_slider.reset()
        self.update_queue_display()
        self.update(None)

    def update_queue_display(self):
        """Update the queue display text."""
        queue_str = str(self.initial_queue) if self.initial_queue else "[]"
        self.queue_text.set_text(f'Request Queue:\n{queue_str}')

    def update_max_cylinder(self, val):
        """Update max cylinder and refresh graph."""
        self.max_cylinder = int(val)
        self.update(val)

    def _get_input_value(self, prompt):
        """Get input value from user via simple dialog."""
        print(prompt)
        try:
            value = int(input("  > "))
            if 0 <= value <= 500:
                return value
            else:
                print("  Value must be between 0 and 500")
                return None
        except ValueError:
            print("  Invalid input. Please enter an integer.")
            return None

    def show(self):
        """Show the interactive window."""
        self.update_queue_display()
        plt.show()


def launch_interactive(queue=None, head=None):
    """
    Launch the interactive FCFS visualizer.
    
    Args:
        queue (list): Initial request queue. Defaults to standard example.
        head (int): Initial head position. Defaults to 53.
    """
    if queue is None:
        queue = [98, 183, 37, 122, 14, 124, 65, 67]
    if head is None:
        head = 53

    print("\n" + "=" * 60)
    print("    INTERACTIVE FCFS DISK SCHEDULING VISUALIZER")
    print("=" * 60)
    print("\n  Controls:")
    print("    - Head Position Slider: Change initial head position")
    print("    - Max Cylinder Slider: Adjust cylinder range")
    print("    - Add Request Button: Add new request to queue")
    print("    - Remove Last Button: Remove last request")
    print("    - Clear Queue Button: Clear all requests")
    print("    - Reset All Button: Reset to defaults")
    print("\n  Graph updates in real-time as you adjust values!")
    print("  Close the graph window to return to CLI menu.")
    print("=" * 60 + "\n")

    visualizer = InteractiveFCFSVisualizer(queue, head)
    visualizer.show()
    plt.close('all')
    return visualizer.initial_queue.copy(), visualizer.current_head
