from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def check_winner(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def get_ai_move(board):
    empty = [i for i, cell in enumerate(board) if cell == '']
    return random.choice(empty) if empty else None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data['board']
    board[data['player_move']] = 'X'

    if check_winner(board, 'X'):
        return jsonify({'board': board, 'winner': 'X'})

    ai_index = get_ai_move(board)
    if ai_index is not None:
        board[ai_index] = 'O'
        if check_winner(board, 'O'):
            return jsonify({'board': board, 'winner': 'O'})

    if '' not in board:
        return jsonify({'board': board, 'winner': 'Draw'})

    return jsonify({'board': board, 'winner': None})

if __name__ == '__main__':
    app.run(debug=True)