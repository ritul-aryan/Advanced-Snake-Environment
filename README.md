# 🐍 Advanced Snake: AI-Ready Pygame Environment

A modernized, highly polished implementation of the classic Snake game, engineered from the ground up in Python. 

Unlike standard single-script arcade games, this project is built using a **Finite State Machine (FSM)** and strictly decoupled Object-Oriented principles. The core game logic, rendering, and asset management are completely isolated. This architecture makes the project an ideal, highly scalable testbed for integrating pathfinding algorithms (A*, BFS) or training Reinforcement Learning / Agentic AI models.

## 🚀 Engineering Highlights & Features

* **Finite State Machine (FSM) Architecture:** Clean separation of game states (`MainMenu`, `Playing`, `GameOver`) ensures seamless transitions and prevents spaghetti code, making the environment highly scalable.
* **Centralized Asset Management:** A dedicated `ResourceManager` pre-loads and caches all sprites and audio files into memory at startup, ensuring zero frame drops or I/O bottlenecks during execution.
* **Modular Entity Design:** Game objects (`Snake`, `Apple`, `ParticleSystem`) handle their own local logic and state independently of the main game engine loop.
* **Data Persistence:** Integrated JSON handling (`highscore.json`) to locally track, save, and update All-Time High Scores across different sessions.
* **"Juice" & Custom Physics Engine:** Implemented a custom particle system for visual feedback, dynamic difficulty scaling (engine clock speed increases as the snake grows), and screen-shake mechanics on wall/body collisions.
* **Risk/Reward Mechanics:** Engineered a probability-based "Golden Apple" system that temporarily spawns high-value targets to force dynamic pathing decisions.

## 📂 Project Structure

The repository follows an industry-standard modular structure:

```text
├── resources/
│   ├── images/          # Sprites and backgrounds (PNG/JPG)
│   └── sounds/          # BGM and SFX (MP3)
├── src/
│   ├── core/            # Engine mechanics
│   │   ├── game_over_state.py
│   │   ├── playing_state.py
│   │   ├── resource_manager.py
│   │   └── state_machine.py
│   ├── entities/        # Independent game objects
│   │   ├── apple.py
│   │   ├── particles.py
│   │   └── snake.py
│   └── settings.py      # Centralized configurations and hyper-parameters
├── main.py              # Application entry point
└── requirements.txt     # Dependency list
