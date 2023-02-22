import streamlit as st
import random

# Genera un numero casuale compreso tra 1 e 100
numero_da_indovinare = random.randint(1, 100)

# Inizializza il contatore dei tentativi a 0
tentativi = 0

st.write("# Indovina il numero")

# Ciclo di gioco
while True:
    tentativo = st.number_input("Inserisci un numero tra 1 e 100", min_value=1, max_value=100)
    tentativi += 1
    if tentativo < numero_da_indovinare:
        st.write("Il tuo tentativo è troppo basso.")
    elif tentativo > numero_da_indovinare:
        st.write("Il tuo tentativo è troppo alto.")
    else:
        st.write("Hai indovinato il numero in {} tentativi!".format(tentativi))
        break























