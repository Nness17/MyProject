import streamlit as st

# definiamo una lista di domande e risposte
questions = [
    {
        "question": "Qual è il tuo colore preferito?",
        "options": ["Rosso", "Blu", "Verde", "Giallo"]
    },
    {
        "question": "Qual è la tua arma preferita?",
        "options": ["Spada", "Arco e Frecce", "Martello", "Lancia"]
    },
    {
        "question": "Qual è il tuo superpotere preferito?",
        "options": ["Superforza", "Volo", "Invisibilità", "Teletrasporto"]
    }
]

# definiamo una lista di possibili eroi e i loro risultati associati
heroes = {
    "Batman": ["Blu", "Martello", "Invisibilità"],
    "Superman": ["Rosso", "Volo", "Superforza"],
    "Wonder Woman": ["Rosso", "Lancia", "Superforza"],
    "Flash": ["Giallo", "Nessuna", "Velocezza"],
}

# definiamo la funzione per calcolare il risultato in base alle risposte date
def calculate_result(answers):
    for hero, criteria in heroes.items():
        if all(answer in criteria for answer in answers):
            return hero
    return "Nessun eroe corrisponde alle tue risposte."

# definiamo l'app Streamlit
def main():
    st.title("Quale eroe sei?")
    st.write("Rispondi alle seguenti domande per scoprire quale eroe sei!")
    st.write(" ")

    # inizializziamo una lista vuota per le risposte
    answers = []

    # cicliamo attraverso tutte le domande e le opzioni
    for i, question in enumerate(questions):
        st.write(f"Domanda {i + 1}: {question['question']}")
        # aggiungiamo un menu a tendina per le opzioni
        answer = st.selectbox("Scegli una risposta:", question["options"])
        # aggiungiamo la risposta alla lista delle risposte
        answers.append(answer)
        st.write(" ")

    # calcoliamo il risultato in base alle risposte date
    result = calculate_result(answers)

    # mostriamo il risultato all'utente
    st.write(f"Sei... {result}!")
    st.write(" ")

if __name__ == "__main__":
    main()
    

with st.sidebar:
    st.title("Welcome to the 'Which hero are you' test! :smile:")
    age = st.slider ('Hi!, How old are you?',
    0, 100)
    if st.button('SUBMIT'):
        if age >=90 or age<=9:
            st.write('Are you sure that this is your age? :bust_in_silhouette:')
            if st.button('You do not believe me? :eyes:'):
                st.write('OkOk I believe you, keep calm I still love you :kiss: ')
                st.write('Welcome! I am glad to know that you are ', age, 'years old! :sunglasses:')
        else:
            st.write('Welcome! I am glad to know that you are ', age, 'years old! :sunglasses:')
            
            
with st.sidebar:
    gender = st.radio("What is your gender?", ('Male', 'Female', 'Other', 'I do not want to specificate'))
    if gender == 'Other':
        other = st.text_input('Write here in what you identify! I will always accept you whatever you are :kiss:')
        st.write('I am glad to know that you identify as: ', other)
        st.title("Lets start the test!!! :boy: :girl:")
    elif gender == 'I do not want to specificate':
        st.write('Do not worry! I will understand!')
        st.title("Lets start the test!!! :boy: :girl:")
    else:
        st.write('So you are a ', gender, 'ok!')
        st.title("Lets start the test!!! :boy: :girl:")
        
   
