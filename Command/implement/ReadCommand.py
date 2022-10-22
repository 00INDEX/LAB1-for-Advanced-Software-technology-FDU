import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class ReadCommand(Command):
    command = 'read'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        return super().exec(*args)