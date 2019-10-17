from BaseClasses.LogicalConstruct import LogicalConstruct
from BaseClasses.LogicalContent import LogicalContent
from BaseClasses.Operator import Operator
from UnitTesting import UnitTesting, PassFailType
from enum import IntEnum

class PropType(IntEnum):
    SIMPLE = 1
    COMPLEX = 2
    FIRSTORDER = 3
    SECONDORDER = 4

class Proposition(LogicalConstruct):
    """description of class"""
    negated : bool = False
    propType : PropType
    content : LogicalContent

    def __init__(self, *args, **kwargs):
        argc = len(args)
        if argc:
            try:
                self.content = args[0].content
            except Exception as e:
                pass
        return super(self)

    def applyOperator(self, op : Operator, prop : object = None) -> object:
        """applies (op, prop) to self to create a new proposition in place.
           E.g., p1.applyOperator(<AND>, p2) would create a new instantiation of Proposition, p3,
           that would be the classical-logical conjunction of p1 and p2.  Similarly for xor, etc...
           
           Note: For unary operators prop = None is the sentinel value signaling to ignore the 
           "prop" parameter.
        """
        newProp : Proposition = None
        newProp = op.applyAllLaws(self) #apply all relevant unary laws
        applyBinaryLaws : bool = (prop is not None)
        if applyBinaryLaws:
            tempProp : Proposition = op.ApplyAllLaws(prop) #apply any additional unary laws
            newProp = op.applyAllLaws(newProp, tempProp) #finally apply all binary laws
        return newProp

    def runTest(self, resultsAddFunction) -> None:
        didPass : bool = False
        error : bool = False
        
        pft : PassFailType
        if(error):
            pft = PassFailType.ERROR
        elif(didPass):
            pft = PassFailType.PASS
        else:
            pft = PassFailType.DEFECT
       

        resultsAddFunction("applyOperator", pft, "text")


