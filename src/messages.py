from typing import List
from pydantic import BaseModel, Field


class Message(BaseModel):
    name: str = ''
    role: str = ''
    content: str 

    def process(self) -> str:
      return f"{self.role} said: {self.content}"
    
    def model_dump(self) -> dict:
        """Returns a dictionary representation of the message."""
        return {
            "role": self.role,
            "content": self.content,
            "name": self.name if self.name else None
        }
class HumanMessage(Message):
    name: str = 'default_user'
    role: str = 'user'

class AIMessage(Message):
    name: str = 'default_ai'
    role: str = 'assistant'

class SystemMessage(Message):
    name: str = 'default_system'
    role: str = 'system'
    
class MessageList():
    messages: List[Message] = []

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def add_human_message(self, message) -> None:
        self.messages.append(HumanMessage(content=message))

    def add_system_message(self, message) -> None:
        self.messages.append(SystemMessage(content=message))
    
    def add_ai_message(self, message) -> None:
        self.messages.append(AIMessage(content=message))

    def add_list_of_messages(self, messages: List[Message]) -> None:
        self.messages.extend(messages)

    def get_messages(self) -> List[Message]:
        return self.messages

    def format_for_human(self) -> str:
        """Generate a human-readable table of messages."""
        if not self.messages:
            return "No messages available."

        headers = ["Name", "Role", "Message"]
        rows = [
            [message.name, message.role, message.content]
            for message in self.messages
        ]

        col_widths = [max(len(str(item)) for item in col) for col in zip(*([headers] + rows))]

        separator = '-' * (sum(col_widths) + len(col_widths) * 3 - 1)

        header_str = ' | '.join(f"{headers[i].ljust(col_widths[i])}" for i in range(len(headers)))

        row_strs = [
            ' | '.join(f"{str(row[i]).ljust(col_widths[i])}" for i in range(len(row)))
            for row in rows
        ]
        table = [header_str, separator] + row_strs
        return "\n".join(table)

    def process_into_str(self) -> str:
        response = []
        for message in self.messages:
            response.append(message.process())
        return "\n".join(response)

    def __str__(self):
        return self.format_for_human()

    def __repr__(self):
        return self.process_into_str()

    def __len__(self):
        return len(self.messages)

    def __getitem__(self, index):
        return self.messages[index]

    def __iter__(self):
        return iter(self.messages)

    def __contains__(self, item):
        return item in self.messages

    def create_message_dicts(self) -> str:
        return [m.model_dump() for m in self.messages]

    def get_messages_from_name(self, name: str) -> List[Message]:
        return [m for m in self.messages if m.name == name]
    
    def add_or_change_system_message(self, message: str) -> None:
        """Replace the first message in the list with a new message."""
        if len(self.messages) == 0:
            self.add_system_message(message)
        else:
            self.messages[0] = SystemMessage(content=message)

    