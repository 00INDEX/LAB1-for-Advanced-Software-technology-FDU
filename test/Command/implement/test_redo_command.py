import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand
from Command.implement.AddBookmarkCommand import AddBookmarkCommand
from Command.implement.UndoCommand import UndoCommand
from Command.implement.RedoCommand import RedoCommand

def test_undo_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + './test/Command/implement/bookmark.bmk')
    bookmark.do()
    command = AddBookmarkCommand()
    command.exec(bookmark, '"书签4"@"https://www.xx.xx"', 'at', '"子子文件夹"')
    bookmark.do()
    assert bookmark.treeview.children[0].children[1].children[1].children[1].key == '书签4'
    command = UndoCommand()
    command.exec(bookmark)
    assert len(bookmark.treeview.children[0].children[1].children[1].children) == 1
    command = RedoCommand()
    command.exec(bookmark)
    assert bookmark.treeview.children[0].children[1].children[1].children[1].key == '书签4'
    