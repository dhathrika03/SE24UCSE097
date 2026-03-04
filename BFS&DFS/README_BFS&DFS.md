# Tic-Tac-Toe Search using DFS and BFS

## Overview

This project demonstrates the use of **search algorithms in Artificial Intelligence** to find a winning configuration in a **Tic-Tac-Toe board**.

Two algorithms are implemented:

* **Depth First Search (DFS)**
* **Breadth First Search (BFS)**

Both algorithms start from an **empty Tic-Tac-Toe board** and explore possible moves by placing **'X'** in empty cells until a winning configuration is found.

The program also counts the **number of nodes expanded** during the search process.

---

## Problem Description

The goal of this program is to determine whether a winning board configuration for player **'X'** can be reached starting from an empty board.

The algorithms explore different board states and check if any state satisfies the **Tic-Tac-Toe winning condition**.

A winning state occurs when **three 'X' marks appear in a row, column, or diagonal**.

---

## Board Representation

The Tic-Tac-Toe board is represented as a **list of 9 elements**:

```
Index positions:

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

Each cell contains:

* `'X'` → Move made by player X
* `' '` → Empty cell

Example board:

```
['X', 'X', 'X',
 ' ', ' ', ' ',
 ' ', ' ', ' ']
```

This represents a **winning state**.

---

## Functions Used

### 1. check_winner(board)

This function checks if the current board state contains a **winning combination**.

It verifies all possible winning positions:

* Rows
* Columns
* Diagonals

If three `'X'` symbols are found in any winning position, the function returns **True**.

---

### 2. generate_children(board)

This function generates **all possible next states** of the board.

For every empty cell:

1. A copy of the board is created.
2. `'X'` is placed in that empty position.
3. The new board is added to the list of child states.

This helps the search algorithm explore all possible moves.

---

## Depth First Search (DFS)

DFS explores the **deepest possible board states first** before backtracking.

### Algorithm Steps

1. Initialize a **stack** with the initial board.
2. Remove the top board from the stack.
3. Check if it is a **winning state**.
4. If yes, return the solution.
5. Otherwise generate its **child states**.
6. Push the child states into the stack.
7. Repeat until a solution is found or no states remain.

DFS may reach a solution quickly because it explores deep paths first.

---

## Breadth First Search (BFS)

BFS explores board states **level by level**.

### Algorithm Steps

1. Initialize a **queue** with the initial board.
2. Remove the front board from the queue.
3. Check if it is a **winning state**.
4. If yes, return the solution.
5. Otherwise generate its **child states**.
6. Add the child states to the queue.
7. Repeat until a solution is found.

BFS guarantees the **shortest path to the solution**, but it may explore more states.

---

## Output

The program prints:

* Number of **nodes expanded**
* The **winning board configuration**

Example output:

```
DFS Nodes Expanded: 4
Winning Board: ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']

BFS Nodes Expanded: 4
Winning Board: ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
```

---

## Technologies Used

* **Python 3**
* Basic **Artificial Intelligence Search Algorithms**
* Python **collections library (deque)** for BFS queue

---

## Learning Objectives

This project helps understand:

* State space representation
* Search algorithms in AI
* Difference between **DFS and BFS**
* Node expansion during search
* Basic problem solving using Python

---

## How to Run

1. Install **Python 3**.
2. Save the code in a file, for example:

```
tic_tac_toe_search.py
```

3. Run the program:

```
python tic_tac_toe_search.py
```

The program will display the **winning board state and nodes expanded**.

---

## Conclusion

This project demonstrates how **DFS and BFS algorithms** can be used to explore possible game states in Tic-Tac-Toe.

DFS explores deeper paths first, while BFS explores level by level. Both approaches help understand **search strategies used in Artificial Intelligence**.
