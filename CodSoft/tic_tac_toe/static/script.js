const boardDiv = document.getElementById('board');
const statusDiv = document.getElementById('status');
const resetBtn = document.getElementById('reset');

let board = Array(9).fill('');
let gameOver = false;

function renderBoard() {
    boardDiv.innerHTML = '';
    board.forEach((cell, i) => {
        const btn = document.createElement('button');
        btn.className = 'cell';
        btn.textContent = cell;
        btn.disabled = cell !== '' || gameOver;
        btn.onclick = () => playerMove(i);
        boardDiv.appendChild(btn);
    });
}

function playerMove(index) {
    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ board, player_move: index })
    })
    .then(res => res.json())
    .then(data => {
        board = data.board;
        renderBoard();
        if (data.winner) {
            statusDiv.textContent = data.winner === 'Draw' ? "It's a draw!" : `${data.winner} wins!`;
            gameOver = true;
        }
    });
}

resetBtn.onclick = () => {
    board = Array(9).fill('');
    gameOver = false;
    statusDiv.textContent = "Your turn (X)";
    renderBoard();
};

renderBoard();