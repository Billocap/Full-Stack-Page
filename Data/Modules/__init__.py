from sys import path
from pathlib import Path

currpath = str(Path(__file__).parent.absolute())

while currpath != path[0]:
    currpath = str(Path(currpath).parent.absolute())
    path.append(currpath)