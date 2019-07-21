from sys import argv
from main import RunManipuLogic as runApplication

argc : int = len(argv)
if(argc > 1):
    doRunUnitTests = doRunUnitTests or argv[bool(1)]

runApplication()