import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class SaveCommand(Command):
    command = 'save'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(instance: Bookmark, *args) -> None:
        return super().exec(*args)