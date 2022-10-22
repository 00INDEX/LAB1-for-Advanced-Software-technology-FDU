from abc import ABCMeta, abstractmethod

class TreeView(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def display(self, level: int=0) -> None:
        raise NotImplementedError()