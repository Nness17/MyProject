def main():
    st.sidebar.title("Seleziona una pagina")
    page = st.sidebar.radio("", ("Domande", "Risultato"))

    if page == "Domande":
        show_questions_page()
    else:
        show_result_page()
        
def show_questions_page():
    st.title("Test della Personalità per Bambini")
    st.write("Rispondi alle seguenti domande per scoprire qual è la tua personalità!")
    
    answers = show_questions()
    
    if st.button("Mostra il risultato"):
        result = calculate_result(answers)
        st.session_state["result"] = result
        st.experimental_rerun()

def show_result_page():
    st.title("Risultato del Test della Personalità per Bambini")
    
    if "result" in st.session_state:
        result = st.session_state["result"]
        st.write("Il tuo risultato è:", result)
    else:
        st.write("Prima devi completare il test!")





