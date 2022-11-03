import sys

from TreeView import FileTreeView

sys.path.append("..")
from Bookmark import Bookmark
from Command import Command


class AddTitleCommand(Command):
    command = 'add-title'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        treeView = FileTreeView(content=[])
        tree = instance.treeview
        ilist = list(args)
        ilist[0] = ilist[0].replace('"', '')
        if len(ilist) > 1:
            ilist[2] = ilist[2].replace('"', '')
        if len(ilist) == 1:
            ikey = ilist[0]
            treeView.key = ikey
            tree.children.append(treeView)
        elif len(ilist) == 3:
            fkey = ilist[2]
            ikey = ilist[0]

            def findnode(treenode: FileTreeView = tree, level: int = 0):
                treeView = FileTreeView(content=[])
                if level > 0:
                    if fkey == treenode.key:
                        treeView.key = ikey

                        treenode.children.append(treeView)
                if len(treenode.children) == 0:
                    return
                for i in range(len(treenode.children)):
                    findnode(treenode.children[i], level=level + 1)

            findnode()