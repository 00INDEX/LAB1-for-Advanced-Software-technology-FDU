import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class OpenCommand(Command):
    command = 'open'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, bookmark: Bookmark, *args) -> None:
        bookmark.filepath = args[0]
        with open(args[0], mode='r', encoding='utf-8', errors='ignore') as file:
            bookmark.content = file.readlines()
            bookmark.treeview.construct(list(map(lambda x: x.replace('\n', ''), file.readlines())))