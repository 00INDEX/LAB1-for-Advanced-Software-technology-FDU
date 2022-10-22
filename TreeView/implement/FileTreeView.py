from .. import TreeView

from typing import List
import re

class FileTreeView(TreeView):
        
    def __init__(self, content: List[str]=[]) -> None:
        super().__init__()
        
        # read: bool 这个书签是否被访问过
        self._read: bool = False
        if len(content) != 0:
            self.construct(content=content)
    
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
    
        
    @property
    def read(self):
        return self._read
    
    @read.setter
    def read(self, value):
        self._read = value