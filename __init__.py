from sys import argv
from main import RunManipuLogic as runApplication

if __name__ == "__main__":
    doRunUnitTests : bool = True #force to true for testing unit-test framework
    try:
        doRunUnitTests = doRunUnitTests or bool(argv[1])
    except:
        doRunUnitTests = False

    runApplication(doRunUnitTests)
