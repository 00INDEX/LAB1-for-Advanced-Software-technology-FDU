import sys
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command
from itertools import chain
import re
from TreeView import FileTreeView

class AddBookmarkCommand(Command):
    command = 'add-bookmark'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        tree = instance.treeview
        ilist=list(args)
        new_stuff = []
        for item in ilist:
            new_stuff.extend(item.split('@'))
        ikey=new_stuff[0].replace('"','')
        ivalue=new_stuff[1].replace('"','')
        fkey=new_stuff[3].replace('"','')
        #print(ikey,ivalue,fkey)

        def findnode(treenode: FileTreeView = tree, level: int = 0):
            treeView = FileTreeView(content=[])
            if level > 0:
                if fkey == treenode.key:
                    treeView.key = ikey
                    treeView.value=ivalue
                    treenode.children.append(treeView)
            if len(treenode.children) == 0:
                return
            for i in range(len(treenode.children)):
                findnode(treenode.children[i], level=level + 1)
        findnode()
        #return super().exec(*args)