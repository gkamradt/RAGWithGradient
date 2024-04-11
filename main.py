from gradientai import Gradient
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

gradient = Gradient(
        access_token=os.getenv("GRADIENT_ACCESS_TOKEN"),
        workspace_id=os.getenv("GRADIENT_WORKSPACE_ID")
    )

st.title("AI News Bot")
st.subheader('Pulling data from [AI News](https://buttondown.email/ainews/)')
st.markdown('Using [Gradient](https://gradient.com) for hosted RAG and answer questions about AI News (from [@swyx](https://twitter.com/swyx)). Check out the video [here](https://www.youtube.com/@DataIndependent)')
st.image('data/AINews.png')
st.subheader("", divider='rainbow')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": f"Be concise in your reponse. Give bullet points when possible \n\n User prompt: {prompt}"})

    result = gradient.answer(
        question=prompt,
        source={
            "type": "rag",
            "collectionId" : os.getenv("GRADIENT_RAG_ID")
        }
    )['answer']

    response = f"{result}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})