import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand
from Command.implement.AddBookmarkCommand import AddBookmarkCommand
from Command.implement.DeleteBookmarkCommand import DeleteBookmarkCommand
from Command.implement.SaveCommand import SaveCommand

def test_save_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + './test/Command/implement/bookmark.bmk')
    command = AddBookmarkCommand()
    command.exec(bookmark, '"书签4"@"https://www.xx.xx"', 'at', '"子子文件夹"')
    command = SaveCommand()
    command.exec(bookmark)
    with open(BASE_DIR + './test/Command/implement/bookmark.bmk', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        assert lines[-1] == '[书签4](https://www.xx.xx)\n'
    command = DeleteBookmarkCommand()
    command.exec(bookmark, '"书签4"')
    command = SaveCommand()
    command.exec(bookmark)
    with open(BASE_DIR + './test/Command/implement/bookmark.bmk', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        assert lines[-1] == '[书签3](https://xx.xx)\n'
    
    