import tkinter as tk

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] and buttons[i][0]["text"] != "":
            return buttons[i][0]["text"]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] and buttons[0][i]["text"] != "":
            return buttons[0][i]["text"]
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] and buttons[0][0]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] and buttons[0][2]["text"] != "":
        return buttons[0][2]["text"]
    return None

def button_click(row, col):
    global turn, game_over
    if buttons[row][col]["text"] == "" and not game_over:
        buttons[row][col]["text"] = "X" if turn else "O"
        winner = check_winner()
        if winner:
            result_label.config(text=f"Player {winner} wins!")
            game_over = True
        elif all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
            result_label.config(text="It's a draw!")
            game_over = True
        else:
            turn = not turn
            result_label.config(text=f"Player {'X' if turn else 'O'}'s turn")

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[tk.Button(root, text="", font=('normal', 40), width=5, height=2, command=lambda r=i, c=j: button_click(r, c)) for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

turn = True
game_over = False
result_label = tk.Label(root, text="Player X's turn", font=('normal', 20))
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
