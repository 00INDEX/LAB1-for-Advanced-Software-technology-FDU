from typing import List
from abc import abstractmethod

class TreeView(object):
    
    def __init__(self) -> None:
        self._children: List[TreeView] = []
        # key: str 文件名/书签显示名称
        self._key: str = ""
        # value: str None/书签url
        self._value: str = ""
    
    def display(self, level: int=0, end: bool=False, endRoute: List[bool]=[]) -> None:
        prompt = ""
        if level > 0:
            for i in range(level - 1):
                if endRoute[i + 1]:
                    prompt  = prompt + "   "
                else:
                    prompt  = prompt + "│  "
            prompt  = prompt + ('└─' if end else '├─')
            print(prompt, self._key)
        if len(self._children) == 0:
            return
        for i in range(len(self._children)):
            self._children[i].display(level=level+1, end=(i==(len(self._children)-1)), endRoute=endRoute + [end])
            
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
    def children(self):
        return self._children

    @children.setter
    def children(self, children): # 好像不需要这个
        self._children = children
