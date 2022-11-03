import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand
from Command.implement.ReadCommand import ReadCommand

def test_read_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + './test/Command/implement/bookmark.bmk')
    command = ReadCommand()
    command.exec(bookmark, '书签3')
    assert bookmark.treeview.children[0].children[1].children[1].children[0].read == True
    