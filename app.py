from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_game'  # Required for sessions

@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize game state if not present
    if 'secret_number' not in session:
        session['game_phase'] = 'setup'
        session['history'] = []
        session['attempts'] = 0
        session['message'] = ""
        session['msg_type'] = "" # 'success', 'error', 'info'

    if request.method == 'POST':
        action = request.form.get('action')

        # --- PHASE 1: SETUP (Player 1) ---
        if action == 'set_number':
            try:
                secret = int(request.form.get('secret_number'))
                max_attempts = int(request.form.get('difficulty'))
                
                if 1 <= secret <= 100:
                    session['secret_number'] = secret
                    session['max_attempts'] = max_attempts
                    session['game_phase'] = 'playing'
                    session['message'] = "Game Started! Player 2, good luck."
                    session['msg_type'] = "info"
                else:
                    session['message'] = "Number must be between 1-100."
                    session['msg_type'] = "error"
            except ValueError:
                session['message'] = "Invalid input."
                session['msg_type'] = "error"

        # --- PHASE 2: GUESSING (Player 2) ---
        elif action == 'guess':
            try:
                guess = int(request.form.get('guess'))
                session['attempts'] += 1
                remaining = session['max_attempts'] - session['attempts']
                
                # Logic
                if guess == session['secret_number']:
                    session['game_phase'] = 'won'
                    session['message'] = f"🎉 CORRECT! The number was {guess}!"
                elif remaining <= 0:
                    session['game_phase'] = 'lost'
                    session['message'] = f"💀 Game Over! The number was {session['secret_number']}."
                elif guess < session['secret_number']:
                    session['history'].insert(0, {'guess': guess, 'hint': 'Too Low 🔼'})
                    session['message'] = "Too Low! Try Higher."
                    session['msg_type'] = "warning"
                else:
                    session['history'].insert(0, {'guess': guess, 'hint': 'Too High 🔽'})
                    session['message'] = "Too High! Try Lower."
                    session['msg_type'] = "warning"
                    
            except ValueError:
                pass

        # --- RESET ---
        elif action == 'reset':
            session.clear()
            return redirect(url_for('home'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)