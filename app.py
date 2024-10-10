import ollama
import streamlit as st

model = 'qwen2:0.5b-instruct'

# Set the title and logo
st.title('pi LLM')
st.logo('images/raspberry-pi.svg')

# Define the initial system prompt
initial_prompt = "You are a knowledgeable and compassionate medical assistant specializing in gestational diabetes management. Your role is to provide evidence-based information, guidance, and support to pregnant individuals dealing with gestational diabetes. Offer clear and accurate advice on topics such as nutrition, meal planning, blood glucose monitoring, exercise, medication, and lifestyle adjustments. Always communicate in an empathetic and respectful manner. Encourage users to consult their healthcare providers for personalized medical advice and refrain from making diagnoses or prescribing treatments."

# Set the page layout
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add the initial system prompt
    st.session_state.messages.append({"role": "system", "content": initial_prompt})

# Display chat messages from history (excluding system messages)
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("Enter Your Prompt Here")

# Chat with the model
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Prepare the assistant's response container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Stream the response from the model
        response_stream = ollama.chat(
            model=model,
            messages=st.session_state.messages,
            stream=True  # Enable streaming
        )

        # Display the response tokens as they arrive
        for response_chunk in response_stream:
            token = response_chunk['message']['content']
            full_response += token
            message_placeholder.markdown(full_response)
            
        # Append the full response to the chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})