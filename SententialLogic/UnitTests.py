from UnitTesting import UnitTestSuite, UnitTest
from SententialLogic.ComplexProposition import ComplexProposition
from SententialLogic.SimpleProposition import SimpleProposition

def runAllTests(mode : int) -> bool:
    testSuite : UnitTestSuite = UnitTestSuite()

    modulesToTest = [SimpleProposition, ComplexProposition]
    for module in modulesToTest:
        testSuite.addUnitTest(UnitTest(module()))

    return testSuite.runTestSuite()
