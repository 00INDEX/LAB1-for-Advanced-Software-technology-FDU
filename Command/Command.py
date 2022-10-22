from abc import ABCMeta, abstractmethod
from importlib import import_module
import sys
sys.path.append("..")
from Bookmark import Bookmark

class Command(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def exec(instance: Bookmark, *args) -> None:
        raise NotImplementedError()