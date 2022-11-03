import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command
from .. import commands

class RedoCommand(Command):
    command = 'redo'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        if len(instance.history) == instance.history_setp + 1:
            print('当前没有可以进行重做的操作')
        else:
            instance.history_setp = instance.history_setp + 1
            instance.treeview = instance.history[instance.history_setp]
