from .. import TreeView

from typing import List
import re

class FileTreeView(TreeView):
        
    def __init__(self, content: List[str]=[]) -> None:
        super().__init__()
        self._children: List[TreeView] = []
        # key: str 文件名/书签显示名称
        self._key: str = ""
        # value: str None/书签url
        self._value: str = ""
        # read: bool 这个书签是否被访问过
        self._read: bool = False
        if len(content) != 0:
            self.construct(content=content)
        
    def display(self, level: int=0) -> None:
        print('--' * level, self._key)
        if len(self._children) == 0:
            return
        for child in self._children:
            child.display(level=level+1)
    
    def construct(self, content: List[str]=[]):
        childrenContent: List = list()
        hasLeaf: bool = True
        if len(content) == 1 and content[0].startswith('['):
            self._key = re.findall(r'\[(.*?)\]', content[0])[0]
            self._value = re.findall(r'\((.*?)\)', content[0])[0]
            return
        if content[0].startswith(' '):
            self._key = content.pop(0)
            self._key = self._key.replace(' ', '')
        for line in content:
            if line.startswith('# '):
                hasLeaf = False
                if len(childrenContent) != 0:
                    self._children.append(FileTreeView(list(map(lambda x: x[1:] if x.startswith('#') else x, childrenContent))))
                    childrenContent = list()
                childrenContent.append(line)
            elif line.startswith('#'):
                hasLeaf = False
                childrenContent.append(line)
            elif hasLeaf and line.startswith('['):
                self._children.append(FileTreeView([line]))
            elif not hasLeaf and line.startswith('['):
                childrenContent.append(line)
            
        if len(childrenContent) != 0:
            self._children.append(FileTreeView(list(map(lambda x: x.replace('#', ''), childrenContent))))
        print(content)
        
    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, value):
        self._key = value
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
        
    @property
    def read(self):
        return self._read
    
    @read.setter
    def read(self, value):
        self._read = value