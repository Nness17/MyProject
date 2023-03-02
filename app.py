import streamlit as st

def quiz():
    st.title("Which hero are you?")
    st.write("Answer to the following questions to discover it!")

    # Qu1
    st.header("Question 1")
    q1 = st.radio("Which weapon do you prefer?", ("Bow", "Sword", "Hammer", "Gun"))
    
    # Qu2
    st.header("Question 2")
    q2 = st.radio("Which is your favourite superpower?", ("Unlimited Power", "Flying", "Invisibility", "Telecinesis"))

    # Qu3
    st.header("Question 3")
    q3 = st.radio("Which battle animal do you prefer?", ("A lion with 3 heads", "A super bird that throws fireballs", "An immortal bear with his super shield", "A giant snake that kills whoever he bites"))
 
    result = ""
    if q1 == "Arco" and q2 == "Invisibilità" and q3 == "Falco":
        result = "sei l'eroe Freccia Verde!"
    elif q1 == "Spada" and q2 == "Forza sovrumana" and q3 == "Leone":
        result = "sei l'eroe Spada di Fuoco!"
    elif q1 == "Martello" and q2 == "Telecinesi" and q3 == "Orso":
        result = "sei l'eroe Martello Telecinetico!"
    elif q1 == "Pistola" and q2 == "Volare" and q3 == "Serpente":
        result = "sei l'eroe Pistola Alata!"
    else:
        result = "mi dispiace, non riesco a identificare quale eroe sei."

    # Visualizzazione del risultato
    st.header("Risultato")
    st.write(result)
    quiz()
    
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
        
   


