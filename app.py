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
    
PAGE_BG_IMG = "https://th.bing.com/th/id/R.b729d4a5cd253ee7c0207dad3f6330f7?rik=PUpjkGSIZa81vw&pid=ImgRaw&r=0"
RESULT_BG_IMG = "https://th.bing.com/th/id/R.b729d4a5cd253ee7c0207dad3f6330f7?rik=PUpjkGSIZa81vw&pid=ImgRaw&r=0"

def main():
    st.set_page_config(
        page_title="Test della Personalità per Bambini",
        page_icon=":smiley:",
        layout="wide",
        page_bg_image=PAGE_BG_IMG
    )
    
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
        st.balloons()

if __name__ == "__main__":
    main()
