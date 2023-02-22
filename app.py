import streamlit as st

# Creazione del tavolo da gioco
board = [[None for j in range(4)] for i in range(4)]

# Funzione che controlla se c'è un quarto
def check_win():
    for i in range(4):
        # Controllo delle righe
        if all(board[i][j] is not None for j in range(4)) and len(set(board[i])) == 1:
            return True
        # Controllo delle colonne
        if all(board[j][i] is not None for j in range(4)) and len(set([board[j][i] for j in range(4)])) == 1:
            return True
    # Controllo delle diagonali
    if all(board[i][i] is not None for i in range(4)) and len(set([board[i][i] for i in range(4)])) == 1:
        return True
    if all(board[i][3-i] is not None for i in range(4)) and len(set([board[i][3-i] for i in range(4)])) == 1:
        return True
    return False

# Funzione che controlla se la partita è finita
def check_game_over():
    return all(all(row) for row in board) or check_win()

# Creazione dei bottoni per selezionare la pedina da posizionare
available_pieces = [i+1 for i in range(16)]
selected_piece = None

# Creazione dell'interfaccia grafica
st.title("Quarto")

# Creazione del tavolo da gioco
board_elements = []
for i in range(4):
    for j in range(4):
        board_elements.append(st.empty())

# Ciclo di gioco
while not check_game_over():

    # Stampa del tavolo da gioco
    for i in range(4):
        for j in range(4):
            if board[i][j] is None:
                board_elements[i*4+j].markdown("-")
            else:
                board_elements[i*4+j].markdown(f"{board[i][j]}")

    # Selezione della pedina da posizionare
    st.subheader("Seleziona la pedina da posizionare")
    selected_piece = st.radio("", available_pieces) - 1
    available_pieces.remove(selected_piece + 1)

    # Selezione della posizione dove posizionare la pedina
    st.subheader("Seleziona la posizione in cui posizionare la pedina")
    row = st.selectbox("Riga", [0, 1, 2, 3])
    col = st.selectbox("Colonna", [0, 1, 2, 3])

    # Posizionamento della pedina
    board[row][col] = selected_piece

    # Controllo della vittoria
    if check_win():
        st.success("Hai vinto!")
        break

# Stampa del tavolo finale
st.subheader("Tavolo finale")
for i in range(4):
    for j in range(4):
        st.markdown(f"{board[i][j]}")




















