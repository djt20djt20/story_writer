import streamlit as st
import time

def toggleable_prompt_button(prompts, session_key="toggleable_prompt"):
    """
    Displays a dropdown to select a prompt, a button to toggle the display of the prompt,
    and dynamically shows/hides the selected prompt.
    
    Args:
        prompts (dict): A dictionary where keys are prompt names and values are prompt descriptions.
        session_key (str): A unique key for managing session state.
    """
    # Initialize session state
    if f"{session_key}_selected_prompt" not in st.session_state:
        st.session_state[f"{session_key}_selected_prompt"] = list(prompts.keys())[0]

    if f"{session_key}_show_prompt" not in st.session_state:
        st.session_state[f"{session_key}_show_prompt"] = False

    # Dropdown menu, fully decoupled from session state initially
    selected = st.selectbox(
        "Select a prompt:",
        options=list(prompts.keys()),
        key=f"{session_key}_selectbox"
    )

    # Only update session state if dropdown selection changes
    if selected != st.session_state[f"{session_key}_selected_prompt"]:
        st.session_state[f"{session_key}_selected_prompt"] = selected
        st.session_state[f"{session_key}_show_prompt"] = False  # Reset visibility

    # Toggle button
    if st.button(
        "Display Prompt",
        help=prompts[st.session_state[f"{session_key}_selected_prompt"]],
        key=f"{session_key}_button"
    ):
        st.session_state[f"{session_key}_show_prompt"] = not st.session_state[f"{session_key}_show_prompt"]

    # Display the prompt
    if st.session_state[f"{session_key}_show_prompt"]:
        st.write(f"Prompt: {prompts[st.session_state[f'{session_key}_selected_prompt']]}")

# Example usage
prompts = {
    "Prompt 1": "This is the first prompt.",
    "Prompt 2": "This is the second prompt.",
    "Prompt 3": "This is the third prompt.",
}

def stream_data(text):
    """Generator to simulate streaming text data."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

def handle_user_input():
    """Handle user input and generate the response from the assistant."""
    if prompt := st.chat_input("You:"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Add user message to chat history and store it in the database
        #st.session_state['messages'].append({"role": "user", "content": prompt})
        #chat.insert_message(st.session_state['chat_id'], "user", prompt)

        # Generate assistant response
        response = f"Echo: {prompt}"

        # Display assistant response with streaming effect
        with st.chat_message("assistant"):
            st.write_stream(stream_data(response))
            #st_copy_to_clipboard(response)

        # Add assistant response to chat history and store it in the database
        #st.session_state['messages'].append({"role": "assistant", "content": response})
        #chat.insert_message(st.session_state['chat_id'], "assistant", response)

        # Update the title dynamically after the first user interaction
        # if len(st.session_state['messages']) == 2:
        #     #conversation.insert_conversation(chat_id=st.session_state['chat_id'], chat_name=prompt)
        #     st.session_state['dynamic_title'] = prompt
        #     st.rerun()  # This will update the displayed title


st.title("Encapsulated Prompt Button Example with Snapback Fix")


toggleable_prompt_button(prompts, session_key="example_prompt")

handle_user_input()

