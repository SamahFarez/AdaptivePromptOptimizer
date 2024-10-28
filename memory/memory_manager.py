# memory/memory_manager.py
from langchain.memory import ConversationBufferMemory

class MemoryManager:
    def __init__(self):
        self.memory = ConversationBufferMemory()

    def store_message(self, message):
        self.memory.add_message(message)
        
    def get_history(self):
        return self.memory.get_history()
