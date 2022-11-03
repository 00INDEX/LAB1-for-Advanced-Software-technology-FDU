import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

class RedoCommand(Command):
    command = 'redo'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        if(len(args) != 1):
            print('There is no Add or Del operation to Redo')
            return
        #args: List[str] = command.split()[1:]
        #command.split()[0]
        
        if(command.split()[0] == "add-title")
            #add-title function
        if(command.split()[0] == "add-bookmark")
            #add-bookmark function
        if(command.split()[0] == "delete-title")
            #del-title function
        if(command.split()[0] == "delete-bookmark")
            #del-bookmark function
            
        return
