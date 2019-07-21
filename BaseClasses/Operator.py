from typing import Dict, List
from enum import IntEnum
from BaseClasses.LogicalConstruct import LogicalConstruct
from BaseClasses.Law import Law

class OpType(IntEnum):
    DISJUNCT = 1
    CONJUCT = 2
    IMPL = 3
    XOR = 4
    BICOND = 5
    #TODO: more optypes?

class Operator(LogicalConstruct):
    """description of class"""
    laws : List[Law]
    lawApplicationRules : Dict
    
    def applyLaw(law : Law) -> None:
        pass