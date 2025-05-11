import os



def getfiles():
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    print(desktop)

getfiles()