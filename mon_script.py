######################### le jeu en Gomoku (15x15) ##############

import tkinter as tk # Importation du module pour l'interface graphique
import random

#********************* Fonction pour afficher le gagnant *********************
def print_winner():
    global win
    if win is False:
        win = True
        print("Le joueur", current_player, "a gagné le jeu !!!")

#********************* Fonction pour changer de joueur  **********************
def switch_player():
    global current_player
    current_player = 'O' if current_player == 'X' else 'X'

#********************* Fonction pour la DETECTION DE VICTOIRE **********************
def check_win(clicked_row, clicked_col):
    def count_consecutive(dx, dy):
        count = 1
        for direction in (-1, 1):  # Vérifie dans les deux directions
            i, j = clicked_row, clicked_col
            while True:
                i += dx * direction
                j += dy * direction
                if 0 <= i < 15 and 0 <= j < 15 and buttonsStock[i][j]['text'] == current_player:
                    count += 1
                else:
                    break
        return count

    # Vérifier les 4 directions (horizontale, verticale et les 2 diagonales)
    if (count_consecutive(1, 0) >= 5 or  # Horizontal
        count_consecutive(0, 1) >= 5 or  # Vertical
        count_consecutive(1, 1) >= 5 or  # Diagonale principale
        count_consecutive(1, -1) >= 5):  # Diagonale inverse
        print_winner()

#*************************** ON PLACE LES SYMBOLE X ou O *************************
def place_symbol(rowgame, columngame):
    global current_player
    clicked_button = buttonsStock[rowgame][columngame]
    if clicked_button['text'] == "" and not win:
        clicked_button.config(text=current_player)
        check_win(rowgame, columngame)
        switch_player()
        if not win and current_player == 'O':
            ai_move()

# ******************* IA: Choisir un coup aléatoire *****************
def ai_move():
    empty_cells = [(r, c) for r in range(15) for c in range(15) if buttonsStock[r][c]['text'] == ""]
    if empty_cells:
        rowgame, columngame = random.choice(empty_cells)
        place_symbol(rowgame, columngame)


#***************************** Place au dessin de la grille ***************************
def draw_grid():
    global buttonsStock
    buttonsStock = []  # Réinitialisation correcte de la liste
    for rowgame in range(15):
        buttonStock_in_row = []
        for columngame in range(15):
            buttongame = tk.Button(
                windowgame,
                font=("Arial", 12),  # Réduction de la taille pour adapter à 15x15
                width=2, height=1,
                command=lambda r=rowgame, c=columngame: place_symbol(r, c)
            )
            buttongame.grid(row=rowgame, column=columngame)
            buttonStock_in_row.append(buttongame)
        buttonsStock.append(buttonStock_in_row)

#************************************* [STOCKAGE] ******************************
buttonsStock = []
current_player = 'X'
win = False

# ************************************ LA FENETRE *************************
windowgame = tk.Tk()
windowgame.title("Jeu du Gomoku (15x15)")
windowgame.minsize(200, 200)

draw_grid()
print("Fenêtre affichée")
windowgame.mainloop()
