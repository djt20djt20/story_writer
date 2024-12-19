from tinydb import TinyDB, Query
from pydantic import BaseModel, Field

class PromptManager(BaseModel):
    db: TinyDB = Field(init=False)

    class Config:
        arbitrary_types_allowed = True
        
    def insert_prompt_into_prompt_database(self, name:str, prompt:str):
        query = Query()
        if not self.db.contains(query.name == name):
            self.db.insert({'name': name, 'prompt': prompt})
            print(f"User '{name}' added.")
        else:
            print(f"User '{name}' already exists. Nothing added.")
    
    def retieve_prompt_from_database(self, prompt_name):
        query = Query()
        out = self.db.search(query.name == prompt_name)
        return out[0]['prompt']
