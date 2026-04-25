from flask import Flask, render_template, request, jsonify
from problem1_tictactoe.logic import best_move_minimax, best_move_alpha_beta, check_winner

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tic-tac-toe')
def tic_tac_toe():
    return render_template('tictactoe.html')

@app.post('/api/tictactoe/move')
def tictactoe_move():
    data = request.get_json(force=True)
    board = data.get('board', [''] * 9)
    method = data.get('method', 'alphabeta')

    if check_winner(board) or '' not in board:
        return jsonify({'board': board, 'winner': check_winner(board), 'move': None})

    if method == 'minimax':
        result = best_move_minimax(board, ai='O', human='X')
    else:
        result = best_move_alpha_beta(board, ai='O', human='X')

    move = result['move']
    if move is not None:
        board[move] = 'O'

    return jsonify({
        'board': board,
        'move': move,
        'winner': check_winner(board),
        'nodes': result['nodes'],
        'time_ms': round(result['time_ms'], 4),
        'method': method
    })

if __name__ == '__main__':
    app.run(debug=True)
