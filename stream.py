# from dotenv import load_dotenv
# import os
# import streamlit as st
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Set up Streamlit title
# st.title("Agri Bot")

# # Configure Google Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Initialize session state variables
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous messages
# for message in st.session_state.messages:
#     with st.container():
#         if message["role"] == "user":
#             st.text_input("User:", value=message["content"], key=str(message))
#         elif message["role"] == "assistant":
#             st.text_area("Assistant:", value=message["content"], key=str(message))

# # Chat input
# prompt = st.text_input("User:", "What is up?")

# # Add user message to session state
# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})

# # Generate response
# if prompt:
#     messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
#     stream = genai.chat.completions.create(model=st.session_state["openai_model"], messages=messages, stream=True)
#     response = next(stream)
#     st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})








# from dotenv import load_dotenv
# import os
# import streamlit as st
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Set up Streamlit title
# st.title("Agri Bot")

# # Configure Google Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Initialize session state variables
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "text-bison-001"  # Using the "text-bison-001" model

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous messages
# for message in st.session_state.messages:
#     with st.container():
#         if message["role"] == "user":
#             st.markdown(f"**User:** {message['content']}")  # Using markdown for better formatting
#         elif message["role"] == "assistant":
#             st.markdown(f"**Assistant:** {message['content']}")  # Using markdown for better formatting

# # Chat input
# prompt = st.text_input("You:", placeholder="Ask me anything about agriculture...")  # Added a placeholder

# # Add user message to session state
# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})

# # Generate response
# if prompt:
#     messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
#     stream = genai.chat.completions.create(model=st.session_state["openai_model"], messages=messages, stream=True)
#     response = next(stream)
#     st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})

#     # Display the response
#     st.success(response["choices"][0]["message"]["content"])  # Using st.success for better visibility


from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Set up Streamlit title
st.title("Agri Bot")

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "models/text-bison-001"  # Use the "text-bison-001" model

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        conversation_history = "\n".join(
            [f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages]
        )
        response_completion = genai.generate_text(
            model=st.session_state["openai_model"],
            prompt=conversation_history,
        )
        response = response_completion.result

        # Display the response in chunks
        for chunk in response.split("\n\n"):
            st.write(chunk)

        st.session_state.messages.append({"role": "assistant", "content": response})