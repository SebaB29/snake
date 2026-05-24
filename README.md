# 🐍 Snake Game

Welcome to **Snake**, a classic arcade game implementation in Python. Navigate the snake, eat fruits to grow, and avoid obstacles in this project built with Object-Oriented Programming (OOP) principles.

# 📸 Demo
<div style="display: flex; gap: 10px;">
    <img alt="Snake Gameplay" src="img/snake.png" width="350px">
    <img alt="Game Over Screen" src="img/gameover.png" width="350px">
</div>

# 📍 Table of Contents
- [📝 Description](#-description)
  - [🧩 Key Features](#-key-features)
  - [🧱 Project Structure](#-project-structure)
  - [🛠️ Technologies](#️-technologies)
- [🚀 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [⚙️ Installation](#️-installation)
- [💡 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

# 📝 Description
This project was developed as a university assignment to demonstrate the use of classes, inheritance, and modular logic in Python. It uses a custom library for graphical rendering and event handling.

## 🧩 Key Features
- **Levels & Difficulty:** Multiple levels with increasing speed and strategic obstacles.
- **Classic Mechanics:** Growing tail system and random fruit spawning.
- **Collision Logic:** Advanced detection for walls, obstacles, and self-collision.
- **Pause System:** Ability to pause the game at any moment.

## 🧱 Project Structure
```text
Snake/
├── graphics/    # Rendering libraries (gamelib & custom)
├── img/         # Demo screenshots
├── resources/   # Configuration files (obstacles.txt)
├── src/         # Core game logic (OOP classes)
│   ├── snake.py
│   ├── fruit.py
│   └── game.py
└── main.py      # Entry point
```

## 🛠️ Technologies
* **Python 3.x**
* **Gamelib**: A lightweight thread-based rendering library for Python interfaces.

# 🚀 Getting Started
## 📋 Prerequisites
* Python 3.10 or higher installed on your system.

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:SebaB29/snake.git
   cd snake
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

# 💡 Usage
To start the game, simply run the main script:
```bash
python main.py
```

## 🎮 Controls
| Key         | Action         |
|-------------|----------------|
| Arrow Up    | Move Up        |
| Arrow Down  | Move Down      |
| Arrow Left  | Move Left      |
| Arrow Right | Move Right     |
| P           | Pause / Resume |

# 🤝 Contributing
1. Fork the project.
2. Create your Feature Branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the Branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
