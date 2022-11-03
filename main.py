import sys
from typing import List, Tuple
from Command import Command, commands
from Bookmark import Bookmark

bookmark = Bookmark()

def getCommand(prompt: str='请输入命令') -> None:
    command: str = input(f'[{prompt}]>')
    args: List[str] = command.split()[1:]
    # try:
    if True:
        module: Command = commands[command.split()[0]]()
        module.exec(bookmark, *args)
        if command.split()[0].startswith('add') or command.split()[0].startswith('del'):
            bookmark.do(command)
    # except Exception as e:
    #     print('命令错误，请重试')
    

def main() -> None:
    while True:
        getCommand(bookmark.filepath)

if __name__ == '__main__':
    main()
