from typing import List
from pydantic import BaseModel, Field
from legacy.conversations import *
from src.connectors import *
from src.messages import *
import json
from legacy.outline_data_handler import *
import os
import json
from pydantic_core import core_schema

class Agent(BaseModel, ABC):
  @abstractmethod
  def go(self) -> None:
    pass

class ConversationSummarizer:
    def __init__(self, summarizing_model: AIModel):
        self.summarizing_model = summarizing_model

    def summarize(self, conversation: Conversation) -> str:
        """Generate a summary of the conversation."""
        return self.summarizing_model.generate_response(messages=conversation.messagelist)

    @staticmethod
    def parse_summary_to_json(summary: str) -> dict:
        """Parse a summary string into JSON."""
        return json.loads(summary)



class HumanConversationAgent(BaseModel):
    data: DataStore = DataStore()
    chat_bot: AIModel = None
    summarizer: ConversationSummarizer = None 
    model_config = {
        "arbitrary_types_allowed": True
    }

    # === Setup Methods ===
    def set_novel_name(self, name: str) -> None:
        self.data.novel_name = name

    def set_objective(self, new_objective: str = None) -> None:
        if new_objective:
            self.data.objective = new_objective
        else:
            self._prompt_for_objective()

    def _prompt_for_objective(self) -> None:
        print(f'Current objective: {self.objective}')
        user_input = input("New objective (hit enter to keep the current one): ")
        if user_input.strip():
            self.data.objective = user_input.strip()
            print(f'Objective updated to: {self.objective}')
        else:
            print("Objective unchanged.")

    def set_ai_chat_bot(self, chat_bot:AIModel):
        self.chat_bot = chat_bot

    def update_conversation_objective(self) -> None:
        self.data.conversation.replace_conversation_objective(self.data.objective)

    # === Interaction Methods ===
    def start_conversation(self, ai_model: AIModel) -> None:
        self.data.conversation.set_conversation_objective(self.data.objective)
        self.data.conversation.start_conversation(ai_model)

    def show_conversation(self) -> None:
        print(self.data.conversation.messagelist.format_for_human())

    def show_objective(self) -> None:
        print(self.data.objective)

    def delete_conversation(self) -> None:
        self.data.conversation = HumanAIConversation()

    # === Data Management Methods ===
    def save_outline(self, database_connection: NovelDatabase) -> None:
        database_connection.save_new_draft(self.data.novel_name, self.data.objective)

    def load_outline(self, database_connection: NovelDatabase, draft: str = None) -> None:
        return database_connection.load_draft(draft)

    # === Summarization ===
    def set_summarizer(self, summarizer:ConversationSummarizer):
        self.summarizer = summarizer

    def summarise_conversation(self) -> None:
        if not self.summarizer:
            raise ValueError("No summarizer instance provided!") 
        self.data.summary = self.summarizer.summarize(self.data.conversation)
        print("Conversation summarized and added to objective.")

    # === Chat about the summary ===
    def chat_about_the_summary(self, prompt:str):
        conversation = HumanAIConversation()
        conversation.set_conversation_objective(prompt)
        conversation.add_human_message('This is the previous text')
        conversation.add_human_message(json.dumps(self.data.summary))
        conversation.continue_conversation(self.chat_bot)
        self.data.conversation=conversation
        self.summarise_conversation()



#json.dumps(self.summarizer.parse_summary_to_json(summary))