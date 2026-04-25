# AI Problem Solving Assignment

Repository name format required by assignment:

```text
AI_ProblemSolving_<RegisterNumber>
```

This project contains two implemented AI problem-solving systems:

1. **Interactive Game AI - Tic-Tac-Toe System**
2. **Sudoku Solver using CSP**

Both problems are implemented using **Python Flask** with an interactive web interface.

---

## Folder Structure

```text
AI_ProblemSolving_TicTacToe_Sudoku/
│
├── app.py
├── requirements.txt
├── README.md
│
├── problem1_tictactoe/
│   ├── __init__.py
│   └── logic.py
│
├── problem6_sudoku/
│   ├── __init__.py
│   └── logic.py
│
├── templates/
│   ├── index.html
│   ├── tictactoe.html
│   └── sudoku.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        ├── tictactoe.js
        └── sudoku.js
```

---

## Problem 1: Interactive Game AI - Tic-Tac-Toe System

### Problem Description

A web-based Tic-Tac-Toe game is created where the user plays against an AI opponent. The user plays as **X**, and the AI plays as **O**. The AI always selects the best possible move.

### Algorithms Used

#### 1. Minimax Algorithm

The Minimax algorithm checks possible future game states and chooses the move that maximizes the AI score while minimizing the user's score.

#### 2. Alpha-Beta Pruning

Alpha-Beta Pruning is an optimized version of Minimax. It skips branches that cannot affect the final decision, reducing the number of nodes explored.

### Comparison Criteria

The project displays:

- Execution time in milliseconds
- Number of nodes explored
- Selected AI method

### Sample Output

```text
User Move: X at cell 1
AI Move: O at cell 5
Algorithm: Alpha-Beta Pruning
Nodes Explored: 124
Execution Time: 0.42 ms
Result: AI wins / User wins / Match Draw
```

---

## Problem 6: Sudoku Solver using CSP

### Problem Description

Sudoku is a 9×9 logic puzzle. The user can fill the missing cells manually, check the solution, or solve the puzzle automatically using a CSP-based solver.

### Algorithm Used

#### Constraint Satisfaction Problem with Backtracking

The Sudoku grid is treated as a CSP where:

- Variables are empty cells
- Domains are numbers from 1 to 9
- Constraints are row, column, and 3×3 subgrid rules

The solver uses backtracking with MRV-style empty-cell selection to solve the puzzle efficiently.

### Sudoku Constraints

- Each row must contain digits 1 to 9 without repetition
- Each column must contain digits 1 to 9 without repetition
- Each 3×3 box must contain digits 1 to 9 without repetition

### Sample Output

```text
Input Puzzle:
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0

Output:
Solved using CSP Backtracking!
```

---

## Execution Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_ProblemSolving_<RegisterNumber>.git
cd AI_ProblemSolving_<RegisterNumber>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Run the Flask App

```bash
python app.py
```

### 6. Open in Browser

```text
http://127.0.0.1:5000
```

---

```text
Live Website Link: https://aiproblemsolvingra141ra142.vercel.app/
```
