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
            hostory_command = instance.redo()
            hostory_args = hostory_command.split()[1:]
            if 'add' in hostory_command:
                hostory_command = hostory_command.replace('add', 'delete')
            else:
                hostory_command = hostory_command.replace('delete', 'add')
            module = commands[hostory_command.split()[0]]
            module.exec(instance=instance, *hostory_args)
