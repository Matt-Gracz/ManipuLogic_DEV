from UnitTesting import UnitTestSuite, UnitTest
from SententialLogic.ComplexProposition import ComplexProposition
from SententialLogic.SimpleProposition import SimpleProposition

def runAllTests(mode : int) -> bool:
    testSuite : UnitTestSuite = UnitTestSuite()
    modules = [SimpleProposition, ComplexProposition]
    unitTests = [UnitTest(module) for module in modules]
    return testSuite.runTestSuite()
