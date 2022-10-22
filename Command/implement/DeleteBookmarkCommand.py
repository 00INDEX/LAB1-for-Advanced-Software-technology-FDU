import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class DeleteBookmarkCommand(Command):
    command = 'delete'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(instance: Bookmark, *args) -> None:
        return super().exec(*args)