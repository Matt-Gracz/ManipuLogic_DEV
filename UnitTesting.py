from typing import List

class UnitTest():
    """A single unit test"""
    objectToTest : object = None

    def __init__(self, *args, **kwargs): 
        try:
            self.objectToTest= args[0]
        except:
            pass
   
    def runTest(self) -> int:
        try:
            return self.objectToTest.runTest()
        except:
            return 1 #>0 = failure

    def setObjectToTest(self, objectToTest : object) -> None:
        self.objectToTest = objectToTest

class UnitTestSuite():
    """A linear ordering of unit tests for a given function or class"""
    unitTestList : List = List[UnitTest]

    def __init__(self, *args, **kwargs):
        try:
            self.unitTestList = args
        except:
            self.unitTestList = None
            pass

    def runTestSuite(self) -> bool:
        return not all([bool(unitTest.runTest()) for unitTest in self.unitTestList])

    def setTestList(self, unitTestList : List[UnitTest]) -> None:
        self.unitTestList = unitTestList
            
    def addUnitTest(self, test : UnitTest) -> None:
        if self.unitTestList is None:
            self.unitTestList = List[UnitTest]
        self.unitTestList.append(test)
        




