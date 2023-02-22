import streamlit as st

questions = [
    "Do you like listening to music?",
    "Do you like doing sports?",
    "Do you like reading?",
    "Do you like playing videogames?",
    "Do you like listening to music?",
]

with st.sidebar:
    st.title("Welcome to the 'What hero are you' test! :smile:")
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
    st.title("What kind of hero are you?")
    st.write("Answer to the questions and discover which hero are you!")
    
    answers = show_questions()
    
    if st.button("Lemme see which hero am I!"):
        result = calculate_result(answers)
        st.write("And you areee: ", result)
        st.balloons()
    
if __name__ == "__main__":
    main()
