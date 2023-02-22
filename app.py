import streamlit as st
import time
import random

# Imposta la dimensione del gioco
dimensione_gioco = (500, 150)

# Imposta la velocità di gioco
velocita_gioco = 0.1

# Inizializza la posizione del dinosauro
posizione_dinosauro = [10, 100]

# Inizializza la posizione dell'ostacolo
posizione_ostacolo = [dimensione_gioco[0], 100]

# Inizializza il punteggio del giocatore
punteggio = 0

# Carica l'immagine del dinosauro
immagine_dinosauro = st.image("https://i.imgur.com/3Hr8dM3.png")

# Funzione per generare un nuovo ostacolo
def genera_ostacolo():
    altezza_ostacolo = random.randint(10, 100)
    larghezza_ostacolo = random.randint(10, 30)
    return [dimensione_gioco[0], 150 - altezza_ostacolo - 10, larghezza_ostacolo, altezza_ostacolo]

# Ciclo di gioco
while True:
    # Aggiorna la posizione del dinosauro
    if st.session_state.tasto_salto:
        posizione_dinosauro[1] = max(posizione_dinosauro[1] - 50, 0)
        st.session_state.tasto_salto = False
    else:
        posizione_dinosauro[1] = min(posizione_dinosauro[1] + 20, 100)

    # Aggiorna la posizione dell'ostacolo
    posizione_ostacolo[0] -= 5
    if posizione_ostacolo[0] < -posizione_ostacolo[2]:
        posizione_ostacolo = genera_ostacolo()

    # Verifica se il dinosauro ha colpito l'ostacolo
    if (posizione_dinosauro[0] + 10 > posizione_ostacolo[0]) and (posizione_dinosauro[0] < posizione_ostacolo[0] + posizione_ostacolo[2]) and (posizione_dinosauro[1] + 10 > posizione_ostacolo[1]):
        st.write("# Game Over!")
        st.write("Punteggio: {}".format(punteggio))
        break

    # Aggiorna il punteggio
    punteggio += 1

    # Aggiorna l'immagine del gioco
    immagine_gioco = st.image("https://i.imgur.com/hlEa19S.png", width=dimensione_gioco[0], height=dimensione_gioco[1])
    immagine_gioco.add_shape(type='rect', x0=posizione_dinosauro[0], y0=posizione_dinosauro[1], x1=posizione_dinosauro[0] + 10, y1=posizione_dinosauro[1]

























