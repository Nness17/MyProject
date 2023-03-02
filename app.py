import streamlit as st

# Define the questions for the quiz
questions = [
    {
        'question': 'What is your favorite color?',
        'answers': {
            'Red': 'Iron Man',
            'Blue': 'Captain America',
            'Green': 'Hulk',
            'Yellow': 'Thor',
            'Purple': 'Black Widow'
        }
    },
    {
        'question': 'What is your favorite food?',
        'answers': {
            'Pizza': 'Spider-Man',
            'Tacos': 'Deadpool',
            'Sushi': 'Wolverine',
            'Burgers': 'The Hulk',
            'Pasta': 'Doctor Strange'
        }
    },
    {
        'question': 'What is your favorite hobby?',
        'answers': {
            'Reading': 'Batman',
            'Gaming': 'Iron Man',
            'Sports': 'Captain America',
            'Traveling': 'Thor',
            'Watching movies': 'Black Panther'
        }
    }
]

# Define the function to run the quiz
def run_quiz():
    st.title("Which hero are you?")
    st.write("Answer a few questions to find out which hero you are!")
    
    # Loop through each question and display the answer options
    for i, question in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(question['question'])
        answer_options = list(question['answers'].keys())
        answer = st.radio("", answer_options)
        
        # Save the selected answer
        selected_answer = question['answers'][answer]
        
    # Display the final result
    st.subheader("Result")
    st.write(f"You are {selected_answer}!")
    

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
        
   

# Run the quiz
run_quiz()
