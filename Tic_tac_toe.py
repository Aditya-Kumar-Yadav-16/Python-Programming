import tkinter as t
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="lightgreen")
            buttons[combo[1]].config(bg="lightgreen")
            buttons[combo[2]].config(bg="lightgreen")
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

def button_click(index):
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Current Player: {current_player}")  

root = t.Tk()
root.title("Tic Tac Toe")

buttons = [t.Button(root, text="", font=("Arial", 25), width=5, height=2,
           command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

current_player = "X"
winner = False

label = t.Label(root, text=f"Current Player: {current_player}", font=("Arial", 15))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()