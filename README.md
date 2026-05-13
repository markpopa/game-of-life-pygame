# 🧬 Conway's Game of Life

### 📝 What it is
A high-performance Python implementation of Conway's Game of Life. This project simulates cellular life cycles on an interactive grid, where complex structures emerge from simple survival and reproduction rules.

### 💻 Tech Stack
* **Language:** Python 3.x
* **Core Libraries:**
    * `Pygame`: For real-time graphical rendering and handling user input.
    * `NumPy`: For high-speed matrix operations and efficient neighbor calculations.
    * `Pickle`: Used for the save/load system to persist game states.

### 🚀 Features List
* **Interactive Drawing:** Use your mouse to draw living cells directly onto the grid before or during the simulation.
* **Dynamic Speed Control:** Adjust the simulation tempo on the fly using the Arrow keys (Left/Right).
* **Save & Load System:** * Press `F5` to capture the current board state.
    * Press `F6` to restore your saved pattern instantly.
* **Visual States:** Clear distinction between living cells, empty space, and the "dying" transition state.

### 🧠 What I Learned
* **Array Slicing & Logic:** Optimized the "Sum of Neighbors" calculation using NumPy, avoiding slow triple-nested loops.
* **Event-Driven Programming:** Managed complex keyboard and mouse events in sync with a continuous rendering loop.
* **State Persistence:** Implemented data serialization to save patterns, allowing me to build and test specific "Life" oscillators and spaceships.

### 🛠️ How to run it
1. **Install Requirements:**
   ```bash
   pip install -r requirements.txt

2. **🚀 Launch Simulation**
 **Run the main script from your terminal:**
    ```bash
    python gameoflife.py

3. **Controls:**

*   Mouse (Left Click): Draw cells.

*    Spacebar: Pause / Resume simulation.

*    Left/Right Arrows: Change speed.

*    F5 / F6: Save or Load your pattern.
