from sys import argv
from main import RunManipuLogic as runApplication

doRunUnitTests : bool = True
try:
    doRunUnitTests = doRunUnitTests or argv[bool(1)]
except:
    pass

runApplication(doRunUnitTests)