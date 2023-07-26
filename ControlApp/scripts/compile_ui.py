import os
from pathlib import Path
import subprocess

CURRENT = Path(__file__).resolve().parent

Widgets_Folder = CURRENT.parent.joinpath("widgets")
Ui_Folder = Widgets_Folder.joinpath("ui")

ui_files = Ui_Folder.glob("*.ui")
ui_files = list(ui_files)

if __name__ == "__main__":
    os.chdir(Ui_Folder)
    for ui_file in ui_files:
        command = f"pyside2-uic {ui_file} -o ui_{ui_file.stem}.py"
        subprocess.run(command.split(), check=True)
