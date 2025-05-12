import os
from PIL import Image
import io
import pathlib
from pathlib import Path

def getfiles():
    desktop = os.path.normpath(os.path.expanduser("~/Desktop/DupeRemoverInput"))
    print(desktop)

getfiles()