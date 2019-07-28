from UnitTesting import UnitTesting
from SententialLogic.ComplexProposition import ComplexProposition
from SententialLogic.SimpleProposition import SimpleProposition

def runAllTests(mode : int) -> bool:
    return UnitTesting().runTestSuite([SimpleProposition, ComplexProposition])
