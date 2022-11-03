import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand
from Command.implement.AddBookmarkCommand import AddBookmarkCommand

def test_add_bookmark_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + './test/Command/implement/bookmark.bmk')
    command = AddBookmarkCommand()
    command.exec(bookmark, '"书签4"@"https://www.xx.xx"', 'at', '"子子文件夹"')
    assert bookmark.treeview.children[0].children[1].children[1].children[1].key == '书签4'
    
    