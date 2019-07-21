from enum import IntEnum
from BaseClasses.Operator import Operator
from PredicateLogic.Variable import Variable

class QuantType(IntEnum):
    EXIST = 1
    UNIVERAL = 2

class Quantifier(Operator):
    """description of class"""
    quantifiedVariable : Variable
    quantType : QuantType



