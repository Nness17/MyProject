import streamlit as st

questions = [
    "Sei felice quando sei con i tuoi amici?",
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

def show_question(index):
    question = questions[index]
    answer = st.radio(question, ("Sì", "No"))
    return answer

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
    # Imposta lo sfondo personalizzato
    st.set_page_config(page_title="Test della Personalità per Bambini", page_icon=":smiley:", layout="wide", page_bg_image="https://th.bing.com/th/id/R.4f9864eb5ea2dc0d59a0ad7bbfd7a8be?rik=NLIMA2E3itHFgQ&riu=http%3a%2f%2f3.bp.blogspot.com%2f-WD77vgy7NQo%2fU6EqBvM7K_I%2fAAAAAAAAGVs%2fa9Lw9zv8qRQ%2fs1600%2f10492607_1495485737349775_2397954031421573263_n.jpg&ehk=%2bBo3yyfqgiOhLOQpEa8r6qJI7d1SMFLg%2fDpWj%2fZfOjU%3d&risl=&pid=ImgRaw&r=0")
    
    st.title("Test della Personalità per Bambini")
    st.write("Rispondi alle seguenti domande per scoprire qual è la tua personalità!")
    
    answers = []
    for i, question in enumerate(questions):
        st.write("Domanda", i + 1)
        answer = show_question(i)
        answers.append(answer)
    
    if st.button("Mostra il risultato"):
        result = calculate_result(answers)
        st.session_state["result"] = result
        st.experimental_rerun()

    if "result" in st.session_state:
        st.title("Risultato del Test della Personalità per Bambini")
        result = st.session_state["result"]
        st.image("https://i.imgur.com/WbGTrtF.png", use_column_width=True)
        st.write("Il tuo risultato è:", result)

if __name__ == "__main__":
    main()
