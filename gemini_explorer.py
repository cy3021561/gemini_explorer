import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "gemini-v1-423923"
vertexai.init(project = project)

config = generative_models.GenerationConfig(
    temperature=0.4
)
model = GenerativeModel(
    "gemini-pro",
    generation_config = config
)
chat = model.start_chat()

def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)
    
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )

st.title("Gemini Explorer")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display and load to chat history
for i, message in enumerate(st.session_state.messages):
    content = Content(
        role = message["role"],
        parts = [Part.from_text(message["content"])]
    )

    if i != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    chat.history.append(content)

# Initial logic for the model
if len(st.session_state.messages) == 0:
    # Get user's name
    user_name = st.text_input("Enter your name:")
    if user_name:
        initial_prompt = f"Introduce yourself as ReX to {user_name}, you are an assistant powered by Google Gemini. You use emojis to be interactive, speak in a Pirate way."
        llm_function(chat, initial_prompt)

query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)