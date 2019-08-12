from UnitTesting import PassFailType, UnitTesting
from io import StringIO
import sys

class LogicalConstruct(object):
    """Root class for backend semantics classes."""

    def toString(self) -> str:
        """returns as string reprsentation of an instantiation"""
        pass
    def print(self) -> None:
        """prints to stdout the return value of self.toString()"""
        pass
    
    def runTest(resultsAddFunction) -> None:
        didPass : bool = False
        error : bool = False
        old_stdout : object = sys.stdout
        #we'll use try/except to ensure stdout gets re-set no matter what before we exit this
        #function
        expectedStr : str = ""
        testStr : str = "DIFFERENT"
        try:
            expectedStr = self.toString()
            sys.stdout = redirected_stdout = StringIO()
            self.print()
            testStr = redirected_stdout.getValue().strip()
            didPass = didPass and (testStr == expectedStr)
        except Exception as e:
            error = True
        sys.stdout = old_stdout
        
        pft : PassFailType
        if(error):
            pft = PassFailType.ERROR
        elif(didPass):
            pft = PassFailType.PASS
        else:
            pft = PassFailType.DEFECT

        resultsAddFunction("print()", pft, "expected string: {} printed string: {}".format(expectedStr, testStr))


