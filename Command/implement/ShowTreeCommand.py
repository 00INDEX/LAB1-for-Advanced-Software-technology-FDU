import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class ShowTreeCommand(Command):
    command = 'show-tree'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        instance.treeview.display()