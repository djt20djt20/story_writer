import openai
from src.messages import *
from abc import ABC, abstractmethod
from src.connectors import *
from src.messages import *

class Conversation(BaseModel, ABC):
    @abstractmethod
    def start_conversation(self) -> None:
      pass

class HumanAIConversation(Conversation):
    ai_objective: str = Field(default = 'assist the human', description="The objective of the agent")
    messagelist: MessageList = Field(default = MessageList(), description="A list of messages")

    def set_conversation_objective(self, new_objective:str) -> None:
        self.ai_objective = new_objective

    def add_conversation_objective_to_messagelist(self):
        self.messagelist.add_message(SystemMessage(content=(self.ai_objective)))

    def start_conversation(self, ai_model: AIModel):
        if len(self.messagelist)==0:
            self.add_conversation_objective_to_messagelist()
            self.continue_conversation(ai_model)
        else:
            self.continue_conversation(ai_model)

    def continue_conversation(self, ai_model: AIModel):
        print("Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            print(f"You: {user_input}")
            if user_input.lower() == 'exit':
                print("Conversation ended.")
                break
            self.add_human_message(user_input)
            ai_response = ai_model.generate_response(self.messagelist)
            self.add_ai_message(ai_response)
            print(f"AI: {ai_response}")

    def replace_conversation_objective(self, new_message: str) -> None:
        self.messagelist.replace_first_message(new_message)
        self.ai_objective = new_message
    
    def add_human_message(self, message:str):
        self.messagelist.add_message(HumanMessage(content=message))
    
    def add_ai_message(self, message:str):
        self.messagelist.add_message(AIMessage(content=message))
     
     

class AItoAIConversation(Conversation):
    ai_1_objective: str = Field(default = 'assist the human', description="The objective of the agent")
    ai_2_objective: str = Field(default = 'assist the human', description="The objective of the agent")
    messagelist_1: MessageList = Field(default = MessageList(), description="A list of messages")
    messagelist_2: MessageList = Field(default = MessageList(), description="A list of messages")

    def set_conversation_objective_bot_1(self, new_objective:str) -> None:
        self.ai_1_objective = new_objective

    def set_conversation_objective_bot_2(self, new_objective:str) -> None:
        self.ai_2_objective = new_objective

    def add_conversation_objective_to_messagelist_1(self):
        self.messagelist_1.add_message(SystemMessage(content=(self.ai_1_objective)))

    def add_conversation_objective_to_messagelist_2(self):
        self.messagelist_2.add_message(SystemMessage(content=(self.ai_2_objective)))

    def start_conversation(self, ai_model: AIModel, max_conversation_length: int = 5):
         conversation = 1
         while True:
            print(f'------- Mesage {conversation} --------')
            if len(self.messagelist_1)==0:
              self.add_conversation_objective_to_messagelist_1()
              self.add_conversation_objective_to_messagelist_2()
            response_1 = ai_model.generate_response(self.messagelist_1)
            self.messagelist_1.add_message(HumanMessage(content=response_1))
            self.messagelist_2.add_message(AIMessage(content=response_1))
            print(f"AI 1: {response_1}")
            response_2 = ai_model.generate_response(self.messagelist_2)
            self.messagelist_1.add_message(AIMessage(content=response_2))
            self.messagelist_2.add_message(HumanMessage(content=response_2))
            print(f"AI 2: {response_2}")
            conversation += 1
            if conversation >= max_conversation_length:
              print("Conversation ended.")
              break
