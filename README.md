# 🔢 Number Guessing Game (Flask)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?style=flat-square&logo=flask)

A web-based **Two-Player Number Guessing Game** built using **Python and Flask**.  
The application uses **Flask sessions** to manage game state without requiring a database.

---

## 📖 About the Project

This project is a web version of the classic **High–Low Number Guessing Game**, designed for two players:

1. **Player 1 (Host)**
   - Sets a secret number
   - Defines the maximum number of attempts

2. **Player 2 (Guesser)**
   - Tries to guess the number
   - Receives hints: **Too High** or **Too Low**

---

## ✨ Key Features

- 🔐 Session-based state management
- 🔄 Real-time feedback for guesses
- 🎚️ Custom difficulty (attempt limits)
- 📜 Guess history tracking
- 🏁 Automatic win and loss detection

---

## 🛠️ Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3
- **Templating Engine:** Jinja2

---

## 🚀 Getting Started

Follow the steps below to run the project locally.

### ✅ Prerequisites

- Python 3.x installed
- Git installed

---

### 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/codebyrks/Number_Guessing_Game.git

2.  **Navigate to the project folder**
    ```bash
    cd Number_Game
    ```
3.  **(Optional) Activate virtual environment**
    ```bash
    .venv\Scripts\activate      # Windows
    source .venv/bin/activate  # Linux / Mac
    ```
4.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application**
    ```bash
    python app.py
    ```
5.  **Open in browser**
    ```bash
    http://127.0.0.1:5000
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
    * Game ends when:
        * 🎉 Number is guessed correctly, or
        * ❌ Attempts are exhausted

---

## 📂 Project Structure
```
Number_Game/
├── .venv/              # Virtual environment
├── static/             # CSS and static assets
├── templates/          # HTML templates
├── .gitignore          # Git ignore rules
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

```
