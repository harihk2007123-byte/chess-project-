import tkinter as tk
import random

SIZE = 60

pieces = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}

def reset_board():
    return [
        list("rnbqkbnr"),
        list("pppppppp"),
        list("........"),
        list("........"),
        list("........"),
        list("........"),
        list("PPPPPPPP"),
        list("RNBQKBNR")
    ]

board = reset_board()
selected = None
turn_white = True
vs_cpu = False
game_over = False

def is_white(p): return p.isupper()
def in_bounds(r,c): return 0<=r<8 and 0<=c<8

# ---------------- DRAW ----------------
def draw():
    canvas.delete("all")

    for r in range(8):
        for c in range(8):
            color = "#f0d9b5" if (r+c)%2==0 else "#b58863"
            canvas.create_rectangle(c*SIZE, r*SIZE,
                                    (c+1)*SIZE, (r+1)*SIZE,
                                    fill=color)

            if selected == (r,c):
                canvas.create_rectangle(c*SIZE, r*SIZE,
                                        (c+1)*SIZE, (r+1)*SIZE,
                                        outline="red", width=3)

            p = board[r][c]
            if p != ".":
                canvas.create_text(c*SIZE+30, r*SIZE+30,
                                   text=pieces[p], font=("Arial",32))

    if game_over:
        canvas.create_text(240,240,text="GAME OVER",
                           fill="red",font=("Arial",40,"bold"))

# ---------------- RULES ----------------
def valid_pawn(sr, sc, er, ec, piece):
    direction = -1 if is_white(piece) else 1

    if sc == ec and board[er][ec] == ".":
        if er == sr + direction:
            return True
        if (sr == 6 and is_white(piece)) or (sr == 1 and not is_white(piece)):
            if er == sr + 2*direction and board[sr+direction][sc]==".":
                return True

    if abs(ec-sc)==1 and er==sr+direction:
        return board[er][ec]!="."

    return False

def path_clear(sr, sc, er, ec):
    dr = (er-sr) and (er-sr)//abs(er-sr)
    dc = (ec-sc) and (ec-sc)//abs(ec-sc)
    r, c = sr+dr, sc+dc
    while (r,c)!=(er,ec):
        if board[r][c]!=".":
            return False
        r+=dr; c+=dc
    return True

def valid_move(sr, sc, er, ec):
    if not in_bounds(er,ec): return False

    piece = board[sr][sc]
    target = board[er][ec]

    if target!="." and is_white(piece)==is_white(target):
        return False

    dr, dc = er-sr, ec-sc
    p = piece.lower()

    if p=="p": return valid_pawn(sr,sc,er,ec,piece)
    if p=="r": return (sr==er or sc==ec) and path_clear(sr,sc,er,ec)
    if p=="b": return abs(dr)==abs(dc) and path_clear(sr,sc,er,ec)
    if p=="q": return ((sr==er or sc==ec) or abs(dr)==abs(dc)) and path_clear(sr,sc,er,ec)
    if p=="n": return (abs(dr),abs(dc)) in [(2,1),(1,2)]
    if p=="k": return max(abs(dr),abs(dc))==1

    return False

# ---------------- CHECK ----------------
def find_king(white):
    k = "K" if white else "k"
    for r in range(8):
        for c in range(8):
            if board[r][c]==k:
                return r,c

def in_check(white):
    kr,kc = find_king(white)
    for r in range(8):
        for c in range(8):
            p = board[r][c]
            if p!="." and is_white(p)!=white:
                if valid_move(r,c,kr,kc):
                    return True
    return False

def has_moves(white):
    for sr in range(8):
        for sc in range(8):
            if board[sr][sc]!="." and is_white(board[sr][sc])==white:
                for er in range(8):
                    for ec in range(8):
                        if valid_move(sr,sc,er,ec):
                            temp = board[er][ec]
                            board[er][ec] = board[sr][sc]
                            board[sr][sc] = "."
                            if not in_check(white):
                                board[sr][sc] = board[er][ec]
                                board[er][ec] = temp
                                return True
                            board[sr][sc] = board[er][ec]
                            board[er][ec] = temp
    return False

# ---------------- CPU ----------------
def cpu_move():
    moves = []
    for sr in range(8):
        for sc in range(8):
            if board[sr][sc]!="." and not is_white(board[sr][sc]):
                for er in range(8):
                    for ec in range(8):
                        if valid_move(sr,sc,er,ec):
                            temp = board[er][ec]
                            board[er][ec] = board[sr][sc]
                            board[sr][sc] = "."
                            if not in_check(False):
                                moves.append((sr,sc,er,ec))
                            board[sr][sc] = board[er][ec]
                            board[er][ec] = temp

    if moves:
        sr,sc,er,ec = random.choice(moves)
        board[er][ec] = board[sr][sc]
        board[sr][sc] = "."

# ---------------- CLICK ----------------
def click(e):
    global selected, turn_white, game_over

    if game_over:
        return

    r = e.y//SIZE
    c = e.x//SIZE

    if selected is None:
        if board[r][c]!="." and is_white(board[r][c])==turn_white:
            selected=(r,c)
    else:
        sr,sc = selected

        if valid_move(sr,sc,r,c):
            temp = board[r][c]
            board[r][c] = board[sr][sc]
            board[sr][sc] = "."

            if not in_check(turn_white):
                opponent = not turn_white

                if not has_moves(opponent):
                    game_over = True

                turn_white = opponent

                if vs_cpu and not turn_white and not game_over:
                    root.after(500, cpu_turn)
            else:
                board[sr][sc] = board[r][c]
                board[r][c] = temp

        selected=None
    draw()

def cpu_turn():
    global turn_white
    cpu_move()
    turn_white = True
    draw()

# ---------------- MENU ----------------
def start_game(mode):
    global vs_cpu, canvas
    vs_cpu = (mode=="cpu")
    menu.destroy()

    canvas = tk.Canvas(root, width=480, height=480)
    canvas.pack()
    canvas.bind("<Button-1>", click)

    draw()

root = tk.Tk()
root.title("Chess Game - Hari Edition")

menu = tk.Frame(root)
menu.pack(pady=50)

tk.Label(menu, text="Choose Mode", font=("Arial",20)).pack()

tk.Button(menu, text="Player vs Player",
          command=lambda: start_game("pvp")).pack(pady=10)

tk.Button(menu, text="Player vs CPU",
          command=lambda: start_game("cpu")).pack(pady=10)

root.mainloop()
