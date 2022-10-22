from TreeView import FileTreeView

class Bookmark:
    
    
    def __init__(self) -> None:
        self._filepath: str = "未打开工作区"
        self._treeview: FileTreeView = FileTreeView()
        self._content: str = ""
        pass
    
    @property
    def filepath(self):
        return self._filepath
    
    @filepath.setter
    def filepath(self, value):
        self._filepath = value
    
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
    