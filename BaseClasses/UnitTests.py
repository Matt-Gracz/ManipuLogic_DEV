from UnitTesting import UnitTesting
from BaseClasses.LogicalConstruct import LogicalConstruct
from BaseClasses.LogicalContent import LogicalContent
from BaseClasses.Proposition import Proposition
from BaseClasses.Operator import Operator
from BaseClasses.Law import Law

def runAllTests(mode : int) -> bool:
    return UnitTesting().runTestSuite([LogicalConstruct, LogicalContent, Proposition, Operator, Law])




