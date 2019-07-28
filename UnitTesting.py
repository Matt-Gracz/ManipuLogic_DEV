from typing import List, Dict
from enum import Enum

class UnitTest():
    """A single unit test"""
    objectToTest : object = None

    def __init__(self, *args, **kwargs): 
        try:
            self.objectToTest= args[0]()
        except:
            pass
   
    def runTest(self) -> int:
        returnCode = 1
        try:
            UnitTesting().results.setObject(self.objectToTest)
            returnCode = self.objectToTest.runTest(UnitTesting().results.addFunction)
            print(UnitTesting().results)
        except:
            pass
        return returnCode # >0 = failure

    def setObjectToTest(self, objectToTest : object) -> None:
        self.objectToTest = objectToTest

class UnitTestSuite():
    """A singletone/one-off object to do all the work of running unit tests for all of 
       the ManipuLogic program.
    """
    """A linear ordering of unit tests for a given function or class"""
    unitTestList : List = List[UnitTest]

    results = None

    def __init__(self, *args, **kwargs):
        try:
            self.unitTestList = args
        except:
            self.unitTestList = None
            pass
        results = Results()

    def runTestSuite(self, moduleList = None) -> bool:
        if(moduleList is not None):
            self.setTestModules(moduleList)
            return self.runTestSuite(None)
        else:
            return not all([bool(unitTest.runTest()) for unitTest in self.unitTestList]) 

    def setTestList(self, unitTestList : List[UnitTest]) -> None:
        self.unitTestList = unitTestList

    def setTestModules(self, moduleList) -> None:
        self.setTestList([UnitTest(module) for module in moduleList])
            
    def addUnitTest(self, test : UnitTest) -> None:
        if self.unitTestList is None:
            self.unitTestList = List[UnitTest]
        self.unitTestList.append(test)

#Factory function to be used to enforce singleton/one-off object allocation
_TestSuite = None
def UnitTesting(*args, **kw):
    global _TestSuite
    if _TestSuite is None:
        _TestSuite = UnitTestSuite(*args, **kw)
    return _TestSuite

class PassFailType(Enum):
    PASS = "passed"
    DEFECT = "failed due to a functional test case failure"
    ERROR = "ailed due to an internal Python/coding error"
    WARNING = "functionally passed, but warned about e.g., a possible NFR issue"


class Results:
    """A singletone/one-off object that manages the results of ManipuLogic's unit-testing.
    """
    objectName : str
    #funcMapping = {FUNC_NAMWE-->(PASS|FAIL, RESULTS_TEXT)}
    functionMapping : Dict[str, List[str]]

    def __str__(self):
        print("Object Under Test: " + self.objectName)
        for func in self.functionMapping:
            passFail : str = self.functionMapping[func][0]
            resultsText = self.functionMapping[func][1]
            print("    Function {} {} with notes:)".format(func, passFail))
            print("        " + resultsText)

    def setObject(self, object : Object):
        self.objectName = str(object)
        self.functionMapping.clear()

    def addFunction(self, fn : str, passFail : ResultType, results : str):
        if fn not in self.functionMapping.keys():
            self.functionMapping[fn] = []
        self.functionMapping[fn].append([passFail, results])


#Factory function to be used to enforce singleton/one-off object allocation
_Results = None
def TestResults(*args, **kw):
    global _Results
    if _Results is None:
        _Results = Results(*args, **kw)
    return _Results
        




