import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class UndoCommand(Command):
    command = 'undo'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        if len(instance.history) <= 1:
            print('当前没有可以进行撤销的操作')
        else:
            instance.history_setp = instance.history_setp - 1
            instance.treeview = instance.history[instance.history_setp]
