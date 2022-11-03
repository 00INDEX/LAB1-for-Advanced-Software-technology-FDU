import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command
from TreeView import FileTreeView

class DeleteBookmarkCommand(Command):
    command = 'delete-bookmark'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        tree = instance.treeview
        dlist = args[0]
        if len(args) > 1:
            symbol = ' '
            dlist = symbol.join(args)
        dkey = dlist[1:-1]

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

        findnode()
