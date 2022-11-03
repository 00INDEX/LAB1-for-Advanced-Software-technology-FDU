from Command import Command
from Bookmark import Bookmark
from TreeView import TreeView
import sys
sys.path.append("..")

import webbrowser


class ReadCommand(Command):
    command = 'read'

    def __init__(self) -> None:
        super().__init__()

    def exec(self, instance: Bookmark, *args) -> None:
        if len(args)!=1:
            print("Please input a bookmark!!!")
            return
        readObj = args[0]
        
        self._dfs(instance.treeview, readObj)

    def _dfs(self, treeview: TreeView, readObj: str):
        """DFS to search readObj and set read True
        """
        if treeview.key == readObj:
            treeview.read = True
            webbrowser.open(treeview.value)

        for child in treeview.children:
            self._dfs(child, readObj)
