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
        success = 1 # >0 = fail, 0 = success.  Assume failure until proven otherwise.
        try:
            success = self.objectToTest.runTest()
        except:
            success = 1
        return success

    def setObjectToTest(self, objectToTest : object) -> bool:
        try:
            self.objectToTest = objectToTest
            return True
        except:
            return False

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
        try:
            return not all([bool(unitTest.runTest()) for unitTest in self.unitTestList])
        except:
            return False

    def setTestList(self, unitTestList : List[UnitTest]) -> bool:
        try:
            self.unitTestList = unitTestList
            return True
        except:
            return False

    def addUnitTest(self, test : UnitTest) -> bool:
        if self.unitTestList is None:
            self.unitTestList = List[UnitTest]
        try:
            self.unitTestList.append(test)
            return True
        except:
            return False
        




