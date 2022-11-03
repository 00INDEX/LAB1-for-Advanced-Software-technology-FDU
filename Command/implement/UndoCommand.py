import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command
from .. import commands

class UndoCommand(Command):
    command = 'undo'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        if len(instance.history) == 0:
            print('当前没有可以进行撤销的操作')
        else:
            hostory_command = instance.undo()
            hostory_args = hostory_command.split()[1:]
            if 'add' in hostory_command:
                hostory_command = hostory_command.replace('add', 'delete')
            else:
                hostory_command = hostory_command.replace('delete', 'add')
            module = commands[hostory_command.split()[0]]
            module.exec(instance=instance, *hostory_args)
