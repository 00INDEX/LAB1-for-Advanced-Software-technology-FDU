import sys

from TreeView.implement.DictTreeView import DictTreeView
sys.path.append("..")
from Bookmark import Bookmark
from Command import Command

import os

class LsTreeCommand(Command):
    command = 'ls-tree'
    def __init__(self) -> None:
        super().__init__()
        
    def exec(self, instance: Bookmark, *args) -> None:
        dictTreeView =  DictTreeView()
        dictTreeView.construct(os.path.split(os.path.abspath(instance.filepath))[0])
        dictTreeView.display()