import streamlit as st

questions = [
    "Do you like listening to music?",
    "Hai paura dei cani?",
    "Ti piace leggere libri?",
    "Sei bravo/a a fare amicizia?",
    "Ti piace fare sport?",
    "Ti piace la musica?",
    "Hai mai viaggiato in un altro paese?",
    "Ti piace la scuola?",
    "Hai un animale domestico?",
    "Hai un sogno nel cassetto?",
]

def show_questions():
    answers = []
    
    for question in questions:
        answer = st.radio(question, ("Sì", "No"))
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
