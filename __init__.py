from sys import argv
from main import RunManipuLogic as runApplication

if __name__ == "__main__":
    doRunUnitTests : bool = True
    try:
        doRunUnitTests = doRunUnitTests or argv[bool(1)]
    except:
        doRunUnitTests = False

    runApplication(doRunUnitTests)
