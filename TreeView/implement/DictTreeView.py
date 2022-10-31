from genericpath import isdir
from .. import TreeView
import sys
sys.path.append("..")
from Bookmark import Bookmark

from typing import List
import os

class DictTreeView(TreeView):
        
    def __init__(self) -> None:
        super().__init__()
    
    def construct(self, root: str):
        items: List(str) = os.listdir(root)
        fileSlice: List(int) = []
        for i in range(len(items)):
            if os.path.isfile(os.path.join(root, items[i])):
                 fileSlice.append(i)
                 self._children.append(DictTreeView())
                 self._children[-1]._key = items[i]
        items = [item for index, item, in enumerate(items) if index not in fileSlice]
        for i in range(len(items)):
            self._children.append(DictTreeView())
            self._children[-1]._key = items[i]
            self._children[-1].construct(os.path.join(root, items[i]))
            
                