from TreeView import FileTreeView
from typing import List
from copy import deepcopy

class Bookmark:
    
    
    def __init__(self) -> None:
        self._filepath: str = "未打开工作区"
        self._treeview: FileTreeView = FileTreeView()
        self._content: str = ""
        self._history: List[Bookmark] = [FileTreeView([])]
        self._history_setp: int = 0
        pass
    
    def do(self):
        if self._history_setp < len(self._history) - 1:
            self._history = self._history[self._history_setp:]
        self._history.append(deepcopy(self.treeview))
        self._history_setp = self._history_setp + 1
    
    @property
    def filepath(self):
        return self._filepath
    
    @filepath.setter
    def filepath(self, value):
        self._filepath = value
        
    @property
    def history(self):
        return self._history
    
    @history.setter
    def history(self, value):
        self._history = value
        
    @property
    def history_setp(self):
        return self._history_setp
    
    @history_setp.setter
    def history_setp(self, value):
        self._history_setp = value
    
    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, value):
        self._path = value
        
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        self._content = value
        
    @property
    def treeview(self):
        return self._treeview
    
    @treeview.setter
    def treeview(self, value):
        self._treeview = value
    