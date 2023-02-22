import streamlit as st
import random

def generate_random_number():
    return random.randint(1, 10)

def guess_number():
    st.write("Indovina un numero tra 1 e 10")
    random_number = generate_random_number()
    guess = st.text_input("Inserisci il tuo tentativo")
    
    if guess:
        guess = int(guess)
        if guess == random_number:
            st.write("Congratulazioni, hai indovinato!")
        else:
            st.write("Mi dispiace, il numero era", random_number)


def main():
    st.title("Guess the Number")
    guess_number()
    
if __name__ == "__main__":
    main()

















