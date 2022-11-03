from Command import Command
from Bookmark import Bookmark
from TreeView import TreeView
import sys
sys.path.append("..")


class SaveCommand(Command):
    command = 'save'

    def __init__(self) -> None:
        super().__init__()

    def exec(self, instance: Bookmark, *args) -> None:
        """save bookmark to .bmk file
        """
        lines = self._dfs(instance.treeview, 0)
        with open(instance.filepath, "w", encoding='utf-8') as f:
            f.writelines(lines)

    def _dfs(self, treeview: TreeView, depth: int) -> str:
        if treeview.value == "": #bookmark folder
            if treeview.key=="":
                lines = []
            else:
                lines = [depth*"#"+ " " +treeview.key+"\n"]
        else: #bookmark,leaf node
            lines = f"[{treeview.key}]({treeview.value})\n"
            return lines

        for child in treeview.children:
            subLines = self._dfs(child,depth+1)
            lines.extend(subLines)      

        return lines

