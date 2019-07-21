from BaseClasses.LogicalConstruct import LogicalConstruct
from BaseClasses.LogicalContent import LogicalContent
from BaseClasses.Operator import Operator
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

    def applyOperator(op : Operator) -> None:
        pass


