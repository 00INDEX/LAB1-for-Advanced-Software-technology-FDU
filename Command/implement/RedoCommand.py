import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command
from TreeView import FileTreeView

class RedoCommand(Command):
    command = 'redo'
    def __init__(self) -> None:
        super().__init__()
      
    def findnode(treenode: FileTreeView = tree, level: int = 0):
        if level > 0:
            if dkey == treenode.key:
                return [True, True]  # 2个True代表可以删除，并退出程序
        if len(treenode.children) == 0:
            return [False, False]
        for i in range(len(treenode.children)):
            rlist = findnode(treenode.children[i], level=level + 1)
            if rlist[0] == True:
                treenode.children.pop(i)
                return [False, True]  # 第一个false代表不能删除，第二个true代表可以退出
            elif rlist[1] == True:
                return [False, True]
        return [False, False]
    
    def exec(self, instance: Bookmark, *args) -> None:
        if(len(args) != 1):
            print('There is no Add or Del operation to Redo')
            return
        command = args[0]
        args: List[str] = command.split()[1:]
        #command.split()[0]
        
        if(command.split()[0] == "add-title")
            #add-title function
        if(command.split()[0] == "add-bookmark")
            #add-bookmark function
        if(command.split()[0] == "delete-title")
            tree = instance.treeview
            dlist = args[0]
            if len(args) > 1:
                symbol = ' '
                dlist = symbol.join(args)
            dkey = dlist[1:-1]
            findnode()
        if(command.split()[0] == "delete-bookmark")
            tree = instance.treeview
            dlist = args[0]
            if len(args) > 1:
                symbol = ' '
                dlist = symbol.join(args)
            dkey = dlist[1:-1]
            findnode()



            
        return
