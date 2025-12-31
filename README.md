# 🔢 Number Guessing Game (Flask)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A web-based **Two-Player Number Guessing Game** built with Python and Flask. This project uses server-side sessions to manage game state, allowing for a seamless flow without needing a database.

## 📖 About The Project

This application gamifies the classic "High/Low" guessing game. It is designed for two players sharing a screen or taking turns:
1.  **Player 1 (The Host):** Sets a secret number and defines the difficulty (maximum attempts).
2.  **Player 2 (The Guesser):** Tries to find the number using logic and hints provided by the game.

### ✨ Key Features
* **Session Management:** Uses Flask sessions to securely store the secret number and game history.
* **Dynamic Feedback:** Provides real-time "Too High" or "Too Low" hints.
* **Difficulty Settings:** Custom maximum attempt limits set by the user.
* **Game History:** specific tracking of all guesses made during the session.
* **Win/Loss States:** Automatic detection of game-over conditions.

---

## 🛠️ Technologies Used

* **Backend:** [Flask](https://flask.palletsprojects.com/) (Python Microframework)
* **Frontend:** HTML5, CSS3, Jinja2 Templating
---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites
* Python 3.x installed

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/codebyrks/Number_Guessing_Game.git]
    ```

2.  **Install dependencies**
    ```bash
    pip install Flask
    ```
    *(Or if you have a requirements.txt file: `pip install -r requirements.txt`)*

3.  **Run the application**
    ```bash
    python app.py
    ```
---

## 🎮 How to Play

1.  **Setup Phase:**
    * Enter a secret number between **1 and 100**.
    * Set the maximum number of attempts allowed.
    * Click "Start Game".
2.  **Guessing Phase:**
    * Hand the device to Player 2 (or switch roles).
    * Enter a guess.
    * Review the hint (🔼 Too Low / 🔽 Too High).
    * Keep guessing until you win or run out of attempts!

---

## 📂 Project Structure
```
Number_Guessing_Game/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
└── README.md

```
