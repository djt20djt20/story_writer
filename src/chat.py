from src.connectors import *

class Chat():
    def __init__(self):
        self.messages = MessageList()
        self.ai_model = OpenAIModel()
    
    def set_prompt(self, content):
        self.messages.add_or_change_system_message(content)

    def continue_conversation(self):
        print("Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            print(f"You: {user_input}")
            if user_input.lower() == 'exit':
                print("Conversation ended.")
                break
            self.messages.add_human_message(user_input)
            ai_response = self.ai_model.generate_response(self.messages)
            self.messages.add_ai_message(ai_response)
            print(f"AI: {ai_response}")
