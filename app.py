import streamlit as st

# definiamo una lista di domande e risposte
questions = [
    {
        "question": "Select your favourite battle guard",
        "options": ["A dragon with 3 heads", "A giant bird that throws fireballs", "An ice guardian", "A giant immortal bear with his unbrokeable shield"]
    },
    {
        "question": "Which is your favourite weapon?",
        "options": ["A fire sword", "A magic bow that throws 3 arrows", "A hammer with lightnings", "A machine-gun"]
    },
    {
        "question": "Which is your favourite superpower?",
        "options": ["Super strenght", "Flight", "Invisibility", "Teleporting"]
    },
    {
        "question": "Where do you want to be?",
        "options": ["In the magic reign of magma", "In the ice galaxy", "In a small cubic planet", "In an infinity spaceship"]
    }
]

# definiamo una lista di possibili eroi e i loro risultati associati
heroes = {
    "The super knight of magma": {
        "criteria": ["A dragon with 3 heads", "A fire sword", "Super strenght", "In the magic reign of magma"],
        "image": "https://example.com/batman.jpg"
    },
    "The super archer of magma": {
        "criteria": ["A dragon with 3 heads", "A magic bow that throws 3 arrows", "Super strenght", "In the magic reign of magma"],
        "image": "https://example.com/superman.jpg"
    },
    "The super paladin of magma ": {
        "criteria": ["A dragon with 3 heads", "A hammer with lightnings", "Super strenght", "In the magic reign of magma"],
        "image": "https://example.com/wonder-woman.jpg"
    },
    "The super gunslinger of magma": {
        "criteria": ["A dragon with 3 heads", "A machine-gun", "Super strenght", "In the magic reign of magma"],
        "image": "https://example.com/flash.jpg"
    },
    "The super knight of magma": {
        "criteria": ["A dragon with 3 heads", "A fire sword", "Super strenght", "In the magic reign of magma"],
        "image": "https://example.com/batman.jpg"
    },
    "The super archer of magma": {
        "criteria": ["A dragon with 3 heads", "A magic bow that throws 3 arrows", "Super strenght", "In the magic reign of magma"],
        "image": "https://example.com/superman.jpg"
    },
    "The super paladin of magma ": {
        "criteria": ["A dragon with 3 heads", "A hammer with lightnings", "Super strenght", "In the magic reign of magma"],
        "image": "https://example.com/wonder-woman.jpg"
    },
    "The super gunslinger of magma": {
        "criteria": ["A dragon with 3 heads", "A machine-gun", "Super strenght", "In the magic reign of magma"],
        "image": "https://example.com/flash.jpg"
    }
}
# definiamo la funzione per calcolare il risultato in base alle risposte date
def calculate_result(answers):
    for hero, data in heroes.items():
        if all(answer in data["criteria"] for answer in answers):
            return hero, data["image"]
    return None, None

# definiamo l'app Streamlit
def main():
    st.title("Which hero are you?")
    st.write("Answer to the following questions and discover it :sunglasses:")
    st.write(" ")

    # inizializziamo una lista vuota per le risposte
    answers = []

    # cicliamo attraverso tutte le domande e le opzioni
    for i, question in enumerate(questions):
        st.write(f"{question['question']}")
        # aggiungiamo un menu a tendina per le opzioni
        answer = st.selectbox("Select an option:", question["options"])
        # aggiungiamo la risposta alla lista delle risposte
        answers.append(answer)
        st.write(" ")
        
        
    
    # calcoliamo il risultato in base alle risposte date
    result, image_url = calculate_result(answers)

    # mostriamo il risultato all'utente
    if result:
        st.write(f"And you aree... {result}!")
        st.write(" ")
        st.image(image_url, caption=result, use_column_width=True)
    else:
        st.write("Nessun eroe corrisponde alle tue risposte.")

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
        
#mostra risultato 
if st.button('Submit your answers'):
        if result:
            st.write(f"And you aree... {result}!")
            st.write(" ")
            st.image(image_url, caption=result, use_column_width=True)
        else:
            st.write("Nessun eroe corrisponde alle tue risposte.")
            
