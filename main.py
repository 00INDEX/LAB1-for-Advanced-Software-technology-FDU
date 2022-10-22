import sys
from typing import List, Tuple
from Command import Command, commands
from Bookmark import Bookmark

bookmark = Bookmark()

def getCommand(prompt: str='请输入命令') -> None:
    command: str = input(f'[{prompt}]>')
    args: List[str] = command.split()[1:]
    try:
        module: Command = commands[command.split()[0]]()
        
    except Exception as e:
        print('命令错误，请重试')
    module.exec(bookmark, *args)
    bookmark.treeview.display()

def main() -> None:
    while True:
        getCommand(bookmark.filename)

if __name__ == '__main__':
    main()