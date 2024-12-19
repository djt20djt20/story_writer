import uuid
import sqlite3

class Chat:
    def __init__(self, db_location='data/chat_history.db'):
        self.conn = sqlite3.connect(db_location)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT NOT NULL,
                sender_id TEXT NOT NULL,
                message TEXT NOT NULL,            
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def generate_chat_session_id(self):
        return str(uuid.uuid4())

    def insert_message(self, chat_id, sender_id, message):
        self.cursor.execute('''
            INSERT INTO chat_messages (chat_id, sender_id, message)
            VALUES (?, ?, ?)
        ''', (chat_id, sender_id, message))
        self.conn.commit()

    def get_chat_history(self, chat_id):
        self.cursor.execute('''
            SELECT sender_id, message, timestamp
            FROM chat_messages
            WHERE chat_id = ?
            ORDER BY timestamp
        ''', (chat_id,))
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()