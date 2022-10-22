import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class RedoCommand(Command):
    command = 'redo'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(instance: Bookmark, *args) -> None:
        return super().exec(*args)