import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class AddBookmarkCommand(Command):
    command = 'add-title'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(instance: Bookmark, *args) -> None:
        return super().exec(*args)