import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand
from Command.implement.DeleteTitleCommand import DeleteTitleCommand

def test_delete_title_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + './test/Command/implement/bookmark.bmk')
    command = DeleteTitleCommand()
    command.exec(bookmark, '"子子文件夹"')
    assert len(bookmark.treeview.children[0].children[1].children) == 1
    
    