from abc import ABC, abstractmethod
import openai
from pydantic import BaseModel, ConfigDict
from src.messages import *
import keys

api_key = keys.keys['open_ai']
model_name = 'gpt-4o'

class AIModel(ABC):
  @abstractmethod
  def generate_response(self, messages: MessageList) -> str:
    pass

class OpenAIModel(AIModel):
    def __init__(self, response_format=None):
        self.client = openai.OpenAI(api_key= api_key)
        self.model_name = model_name
        self.response_format = response_format

    def generate_response(self, messages: MessageList) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages.create_message_dicts(),
            response_format = self.response_format 
        )
        return response.choices[0].message.content

