import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand

def test_open_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + './test/Command/implement/bookmark.bmk')
    assert bookmark.treeview.children[0].key == '文件夹' and bookmark.treeview.children[0].children[1].children[1].children[0].key == '书签3'
    