# FCFS Disk Scheduling Algorithm Simulator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Interactive%20Graphs-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)

**An interactive simulation of the First Come First Serve (FCFS) Disk Scheduling Algorithm for Operating Systems education.**

*Submitted to: **Er. Bhuvnesh Kumar***

**Team Members:**
- Lovepreet Singh
- Navjot Singh
- Krish Sharma
- Mandeep Singh

</div>

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#-features)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [CLI Menu Options](#cli-menu-options)
  - [Interactive Visualizer](#interactive-visualizer)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 About the Project

This project is a **college submission** for the **Operating Systems** course (4th semester, CSE). It implements and visualizes the **First Come First Serve (FCFS) Disk Scheduling Algorithm** - one of the fundamental disk scheduling algorithms used in operating systems.

FCFS is the simplest disk scheduling algorithm that services requests in the order they arrive in the queue, without any optimization for seek time.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔢 **Custom Stack Implementation** | Built-in Stack class for tracking cylinder traversal |
| 📊 **Real-time Visualization** | Interactive matplotlib graph with live updates |
| 🎛️ **Slider Controls** | Adjust head position and queue values dynamically |
| 📝 **Step-by-Step Output** | Detailed CLI output showing each head movement |
| 📋 **Summary Table** | Final summary with total head movement calculation |
| 🔄 **Stack Operations** | Push/Pop functionality to manipulate traversal history |
| 🧹 **Reset Capability** | Reset scheduler to initial state anytime |
| 📥 **Graph Export** | Save graphs as PNG images |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.8 or higher**
- **Matplotlib** (for visualization)
- **NumPy** (for color mapping)
- **Tkinter** (usually comes with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fcfs-disk-scheduling.git
   cd fcfs-disk-scheduling
   ```

2. **Install dependencies**
   ```bash
   pip install matplotlib numpy
   ```

3. **Run the project**
   ```bash
   python3 main.py
   ```

---

## 📖 Usage

### CLI Menu Options

When you run the program, you'll see the following menu:

```
----------- MAIN MENU -----------

  1. Run FCFS with Default Values (Interactive)
  2. Enter Custom Queue and Head Position
  3. Display Traversal Stack
  4. Pop Last Visited Position from Stack
  5. Reset
  6. View Current Graph
  7. Exit
```

| Option | Description |
|--------|-------------|
| **1** | Run with default queue `[98,183,37,122,14,124,65,67]` and head `53` |
| **2** | Enter custom request queue and head position |
| **3** | Display all visited cylinder positions (traversal stack) |
| **4** | Pop the last visited position from the stack |
| **5** | Reset the scheduler to initial state |
| **6** | View/redraw the current graph |
| **7** | Exit the program |

### Interactive Visualizer

The interactive visualizer provides:

```
Controls:
  - Head Position Slider: Change initial head position (0-200)
  - Max Cylinder Slider: Adjust cylinder range (50-500)
  - Add Request Button: Add new request to queue
  - Remove Last Button: Remove last request from queue
  - Clear Queue Button: Clear all requests
  - Reset All Button: Reset to default values
```

**Workflow Example:**
1. Choose Option 1 → Interactive window opens
2. Adjust head position with slider → Graph updates instantly
3. Add/remove requests as needed
4. Close window → Returns to CLI
5. Use Options 3-6 to inspect/modify the state
6. Use Option 6 to view the graph again

---

## 📁 Project Structure

```
fcfs-disk-scheduling/
├── main.py              # Entry point with CLI menu
├── fcfs.py              # FCFS algorithm implementation
├── stack.py             # Custom Stack class
├── visualizer.py        # Interactive matplotlib visualizer
├── fcfs_disk_scheduling.png  # Saved graph output
├── README.md            # Project documentation
└── LICENSE              # MIT License
```

### File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | CLI entry point, menu handling, team info |
| `fcfs.py` | FCFS algorithm, hop calculations, summary table |
| `stack.py` | Custom Stack class with push/pop/peek operations |
| `visualizer.py` | Interactive matplotlib visualization with sliders |

---

## ⚙️ How It Works

### FCFS Algorithm Logic

1. **Input**: Request queue (e.g., `[98, 183, 37, 122, 14]`) and initial head position (e.g., `53`)
2. **Process**: Serves requests in FIFO order (first come, first served)
3. **Output**:
   - Step-by-step head movements with distances
   - Total head movement sum
   - Visual graph of traversal

### Example Calculation

```
Initial Head: 53
Request Queue: [98, 183, 37, 122, 14, 124, 65, 67]

Step 1: 53 → 98  | Distance: 45
Step 2: 98 → 183 | Distance: 85
Step 3: 183 → 37 | Distance: 146
...

Total Head Movement: 640 cylinders
```

### Stack Operations

The project uses a custom Stack to track visited cylinders:

```python
# Each cylinder visited is pushed onto the stack
stack.push(53)   # Initial head
stack.push(98)    # After first request
stack.push(183)   # After second request
# ... and so on

# Pop removes the last visited position
last = stack.pop()  # Returns 67
```

---

## 📸 Screenshots

### CLI Output
```
=======================================================
Step    From      To        Distance  Direction
-------------------------------------------------------
1       53        98        45        →
2       98        183       85        →
3       183       37        146       ←
...
-------------------------------------------------------
TOTAL HEAD MOVEMENT                     640
=======================================================
```

### Interactive Visualizer
- Zigzag line showing head movement path
- Color-coded visit points
- Directional arrows showing movement
- Real-time updates as you adjust sliders

---

## 🔧 Technical Details

### Dependencies

```python
matplotlib>=3.5.0
numpy>=1.20.0
```

### Key Classes

| Class | Location | Description |
|-------|----------|-------------|
| `Stack` | `stack.py` | Custom stack with push, pop, peek, is_empty, display |
| `FCFSDiskScheduler` | `fcfs.py` | Main algorithm implementation |
| `InteractiveFCFSVisualizer` | `visualizer.py` | GUI visualizer with controls |

### Architecture

```
┌─────────────────────────────────────────────────┐
│                    main.py                      │
│                 (CLI Interface)                 │
└─────────────────────┬───────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   ┌─────────┐   ┌─────────┐   ┌─────────────┐
   │ stack.py│   │  fcfs.py│   │ visualizer.py│
   │ (Data) │   │(Algorithm)│  │  (Display)   │
   └─────────┘   └─────────┘   └─────────────┘
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

| Name | Role |
|------|------|
| Lovepreet Singh | Team Lead / Developer |
| Navjot Singh | Developer |
| Krish Sharma | Documentation |
| Mandeep Singh | Testing |

**Faculty:** Er. Bhuvnesh Kumar

---

## 👤 Author

**Lovepreet Singh**
- 📧 Email: [lsgill1231@gmail.com](mailto:lsgill1231@gmail.com)
- 🔗 LinkedIn: [Lovepreet Singh](https://www.linkedin.com/public-profile/settings/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_self_edit_contact_info%3B%2FSGeOKPNTkCHyFIylca1cA%3D%3D)

---

<div align="center">

**Made with ❤️love for Operating Systems Course**

</div>

---

<div align="center">

**Made with ❤️ for Operating Systems Course**

</div>
