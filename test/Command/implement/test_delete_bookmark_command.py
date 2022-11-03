import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand
from Command.implement.DeleteBookmarkCommand import DeleteBookmarkCommand

def test_delete_bookmark_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + './test/Command/implement/bookmark.bmk')
    command = DeleteBookmarkCommand()
    command.exec(bookmark, '"书签3"')
    assert len(bookmark.treeview.children[0].children[1].children[1].children) == 0
    
    