from BaseClasses.LogicalConstruct import LogicalConstruct
from UnitTesting import UnitTesting, PassFailType

class LogicalContent(LogicalConstruct):
    """description of class"""
    rawData : str = ""
    content = None

    def __init__(self, *args, **kwargs):
        argc = len(args)
        if argc:
            self.content = args[0]
            try:
                self.rawData = str(args[0])
            except Exception as e:
                pass
        return super(self)

    def __str__(self, *args, **kwargs) -> str:
        return rawData
        
    def runTest(resultsAddFunction) -> None:
        didPass : bool = False
        error : bool = False
        
        pft : PassFailType
        if(error):
            pft = PassFailType.ERROR
        elif(didPass):
            pft = PassFailType.PASS
        else:
            pft = PassFailType.DEFECT

        #NOTE: implement when any interesting functions need testing.
        #resultsAddFunction("<fn>", pft, "text")


