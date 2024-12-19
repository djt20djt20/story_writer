from src.connectors import *
from src.messages import *
import json

class ConversationSummarizer:
    def __init__(self, response_format=None):
        self.summarizing_model = OpenAIModel(response_format = response_format)
        self.summarized_text = None

    def summarize(self, messagelist: MessageList) -> str:
        """Generate a summary of the conversation."""   
        self.summarized_text = self.summarizing_model.generate_response(messages=messagelist)

    def parse_summary_to_json(self) -> dict:
        """Parse a summary string into JSON."""
        if self.summarized_text is not None:
            return json.loads(self.summarized_text)
        else:
            return {}