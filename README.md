# ♟️ Chess Game - Hari Edition

A simple Chess Game built using **Python Tkinter** with support for:

* Player vs Player mode
* Player vs CPU mode
* Move validation for all chess pieces
* Check detection
* Checkmate/Game Over detection
* Graphical Chess Board using Unicode chess symbols

---

## 📸 Preview

A GUI-based chess board with clickable pieces and two game modes.

---

## 🚀 Features

* ✅ Full 8x8 chess board
* ✅ Player vs Player mode
* ✅ Player vs CPU mode (Random AI)
* ✅ Legal move validation
* ✅ King check detection
* ✅ Checkmate detection
* ✅ Interactive mouse controls
* ✅ Unicode chess pieces

---

## 🛠 Requirements

* Python 3.x
* Tkinter (usually included with Python)

Check installation:

```bash
python --version
```

```python
import tkinter
print("Tkinter Installed")
```

---

## ▶️ How to Run

1. Download or clone the repository:

```bash
git clone https://github.com/your-username/chess-game.git
```

2. Open the project folder:

```bash
cd chess-game
```

3. Run the program:

```bash
python chess.py
```

---

## 🎮 Controls

* Click a piece to select it.
* Click a destination square to move.
* Red border indicates the selected piece.
* Game ends when the opponent has no legal moves left.

---

## 🧠 CPU Logic

The CPU:

* Plays as Black.
* Generates all legal moves.
* Randomly selects one valid move.
* Avoids moves that leave its king in check.

---

## 📂 Project Structure

```text
chess-game/
│
├── chess.py
├── README.md
└── screenshots/
```

---

## ♜ Supported Pieces

| Piece  | Symbol |
| ------ | ------ |
| King   | ♔ ♚    |
| Queen  | ♕ ♛    |
| Rook   | ♖ ♜    |
| Bishop | ♗ ♝    |
| Knight | ♘ ♞    |
| Pawn   | ♙ ♟    |

---

## 🔮 Future Improvements

* Castling
* En Passant
* Pawn Promotion
* Better AI (Minimax Algorithm)
* Move History
* Undo Button
* Save/Load Game
* Timer Support

---

## 👨‍💻 Author

**Hari Krithick**

Created using Python and Tkinter.


