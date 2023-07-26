from pathlib import Path
import os


class CD:
    def __init__(self, dir) -> None:
        self.cd = os.getcwd()

    def __enter__(self):
        os.chdir(self.cd)

    def __exit__(self, type, value, traceback):
        os.chdir(self.cd)


CURRENT = Path(__file__).resolve().parent

import subprocess
def build_app(filename):
    subprocess.run(f"pyinstaller --onefile {filename}".split(), check=True)


if __name__ == "__main__":
    with CD(CURRENT.parent):
        build_app("gui_app.pyw")
        build_app("gui_app_with_console.py")
