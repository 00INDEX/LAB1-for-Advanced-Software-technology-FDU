import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand
from Command.implement.ShowTreeCommand import ShowTreeCommand

def test_show_tree_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + './test/Command/implement/bookmark.bmk')
    command = ShowTreeCommand()
    command.exec(bookmark)
    