from collections import defaultdict
import os
from typing import Dict
from importlib import import_module
from .Command import Command

commands: Dict[str, Command] = defaultdict(Command)

for filename in os.listdir(r'./Command/implement/'):
    if filename.endswith('.py'):
        module = import_module(f'.implement.{filename[:-3]}', package='Command')
        if not hasattr(module, filename[:-3]): continue
        module = getattr(module, filename[:-3])
        if hasattr(module, 'command') and not hasattr(commands, module.command):
            commands.setdefault(module.command, module)