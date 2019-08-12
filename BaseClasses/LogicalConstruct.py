from UnitTesting import UnitTesting
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
    
    def runTest(resultsAddFunction) -> bool:
        resultsAddFunction("print(): ")
        didPass : bool = False
        old_stdout : object = sys.stdout
        #we'll use try/except to ensure stdout gets re-set no matter what before we exit this
        #function
        try:
            expectedStr : str = self.toString()
            sys.stdout = redirected_stdout = StringIO()
            self.print()
            testStr : str = redirected_stdout.getValue().strip()
            didPass = didPass and (testStr == expectedStr)
        except Exception as e:
            pass
        sys.stdout = old_stdout
        return didPass


