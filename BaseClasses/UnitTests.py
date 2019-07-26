from UnitTesting import UnitTestSuite, UnitTest
from BaseClasses.LogicalConstruct import LogicalConstruct
from BaseClasses.LogicalContent import LogicalContent
from BaseClasses.Proposition import Proposition
from BaseClasses.Operator import Operator
from BaseClasses.Law import Law

def runAllTests(mode : int) -> bool:
    testSuite : UnitTestSuite = UnitTestSuite()

    modulesToTest = [LogicalConstruct, LogicalContent, Proposition, Operator, Law]
    for module in modulesToTest:
        testSuite.addUnitTest(UnitTest(module()))

    return testSuite.runTestSuite()



