from UnitTesting import UnitTestSuite, UnitTest
from BaseClasses.LogicalConstruct import LogicalConstruct
from BaseClasses.LogicalContent import LogicalContent
from BaseClasses.Proposition import Proposition
from BaseClasses.Operator import Operator
from BaseClasses.Law import Law

def runAllTests(mode : int) -> bool:
    testSuite : UnitTestSuite = UnitTestSuite()
    modules = [LogicalConstruct, LogicalContent, Proposition, Operator, Law]
    unitTests = [UnitTest(module) for module in modules]
    testSuite.setTestList(unitTests)
    return testSuite.runTestSuite()



