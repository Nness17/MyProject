import streamlit as st

questions = [
    "Do you like listening to music?",
    "Do you like doing sports?",
    "Do you like reading?",
    "Do you like playing videogames?",
    "Do you like listening to music?",
]

with st.sidebar:
    st.title("Welcome to my personality test! :smile:")
    valueof = st.slider ('Hi!, How old are you?',
    0, 100)
    if st.button('SUBMIT'):
        if valueof == 100 || valueof<=9:
            st.write('Are you sure that this is your age? :new_moon_with_face:')
        else:
            st.write('Welcome! I am glad to know that you are ', valueof, 'years old! :sunglasses:')
    
def show_questions():
    answers = []
    
    for question in questions:
        answer = st.radio(question, ("Sì", "No"))
        if question == 4:
            if answer == "Yes":
                st.text("What kind of music do you like?")
                song = st.radio(("Rap", "Hip-Hop", "Classic", "Rock"))
                if song == "Rap":
                    st.video("https://www.youtube.com/results?search_query=veleno+7")
        answers.append(answer)
    return answers

def calculate_result(answers):
    score = 0
    
    for answer in answers:
        if answer == "Sì":
            score += 1
    
    if score <= 3:
        return "Sei una persona timida, ma gentile e dolce."
    elif score <= 7:
        return "Sei una persona estroversa e socievole."
    else:
        return "Sei una persona ambiziosa e determinata."
    
def main():
    st.title("Test della Personalità per Bambini")
    st.write("Rispondi alle seguenti domande per scoprire qual è la tua personalità!")
    
    answers = show_questions()
    
    if st.button("Mostra il risultato"):
        result = calculate_result(answers)
        st.write("Il tuo risultato è:", result)
        st.balloons()
    
if __name__ == "__main__":
    main()
