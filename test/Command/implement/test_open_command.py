import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR)))
sys.path.append(BASE_DIR)

from Bookmark import Bookmark
from Command.implement.OpenCommand import OpenCommand

def test_open_command():
    bookmark = Bookmark()
    command = OpenCommand()
    command.exec(bookmark, BASE_DIR + '/bookmark.bmk')
    