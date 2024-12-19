from tinydb import TinyDB, Query
from typing import Optional, Dict, Any, List

class NovelDatabase:
    def connect(self, db_path: str):
        """
        Initialize the NovelDatabase with the path to the TinyDB JSON file.

        :param db_path: Path to the TinyDB JSON file.
        """
        self.db = TinyDB(db_path)
        self.novel_query = Query()

    def insert_outline(self, name: str, draft: int, details: Dict[str, Any]) -> bool:
        """
        Insert a new novel into the database if it doesn't already exist.

        :param name: Name of the novel.
        :param draft: Draft number of the novel.
        :param details: Dictionary containing novel details.
        :return: True if insertion was successful, False if the novel already exists.
        """
        if self._outline_and_draft_doesnt_exist(name, draft):
            self.db.insert({'name': name, 'draft': draft, 'details': details})
            return True
        return False
    
    def _outline_and_draft_doesnt_exist(self, name, draft):
        return not self.db.contains((self.novel_query.name == name) & (self.novel_query.draft == draft))

    def retrieve_outline(self, name: str, draft: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a novel's details from the database.

        :param name: Name of the novel.
        :param draft: Draft number of the novel.
        :return: Dictionary of novel details if found, None otherwise.
        """
        result = self.db.search((self.novel_query.name == name) & (self.novel_query.draft == draft))
        if result:
            return result[0]['details']
        return None
    
    # Question - do I need this? Can't we just create another draft?
    def update_outline(self, name: str, draft: int, updated_details: Dict[str, Any]) -> bool:
        """
        Update the details of an existing novel.

        :param name: Name of the novel.
        :param draft: Draft number of the novel.
        :param updated_details: Dictionary containing updated novel details.
        :return: True if update was successful, False if the novel does not exist.
        """
        if self._outline_and_draft_does_exist(name, draft):
            self.db.update({'details': updated_details}, (self.novel_query.name == name) & (self.novel_query.draft == draft))
            return True
        return False
    
    def _outline_and_draft_does_exist(self, name, draft):
        return self.db.contains((self.novel_query.name == name) & (self.novel_query.draft == draft))
 
    def delete_outline(self, name: str, draft: int) -> bool:
        """
        Delete a novel from the database.

        :param name: Name of the novel.
        :param draft: Draft number of the novel.
        :return: True if deletion was successful, False if the novel does not exist.
        """
        if self._outline_and_draft_does_exist(self, name, draft):
            self.db.remove((self.novel_query.name == name) & (self.novel_query.draft == draft))
            return True
        return False
    
    def _novel_exists(self, name:str):
        return self.db.contains(self.novel_query.name == name)

    def find_most_recent_draft_number(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Find the most recent draft of a novel by its name.

        :param name: Name of the novel.
        :return: Dictionary of the most recent novel details if found, None otherwise.
        """
        if not self._novel_exists(name):
            return 0
        drafts = self.db.search(self.novel_query.name == name)
        most_recent_draft = max(drafts, key=lambda x: x['draft'])
        return most_recent_draft['draft']
    
    def retrieve_most_recent_outline(self, name:str):
        draft_number = self.find_most_recent_draft_number(name)
        return self.retrieve_outline(name=name, draft=draft_number)
    
    def save_new_draft(self, name:str, draft):
        most_recent_draft = self.find_most_recent_draft_number(name)
        new_draft_number = most_recent_draft + 1
        self.insert_outline(name=name, draft=new_draft_number, details=draft)


