import sys
from typing import List, Tuple
from Command import Command, commands
from Bookmark import Bookmark

bookmark = Bookmark()

def getCommand(prompt: str='请输入命令') -> None:
    command: str = input(f'[{prompt}]>')
    args: List[str] = command.split()[1:]
    undo_command : str#记录上次执行的add、del操作
    redo_command : str#记录上次执行的undo操作
    try:
        if(command.split()[0].startswith("Add") or command.split()[0].startswith("Del"))
            undo_command = command
        module: Command = commands[command.split()[0]]()
        
    except Exception as e:
        print('命令错误，请重试')
        
    if(command.split()[0].startswith("Und"))
        args.append(Undo_command)
        redo_command = undo_command
        undo_command = ''
        
    if(command.split()[0].startswith("Red"))
        args.append(redo_command)
        Undo_command = Redo_command
        Redo_command = ''
        
    module.exec(bookmark, *args)

def main() -> None:
    while True:
        getCommand(bookmark.filepath)

if __name__ == '__main__':
    main()
