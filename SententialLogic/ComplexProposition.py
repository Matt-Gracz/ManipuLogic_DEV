from BaseClasses.Proposition import Proposition
from BaseClasses.Operator import Operator

class ComplexProposition(Proposition):
    """description of class"""
    LHS : Proposition = None
    RHS : Proposition = None
    op : Operator = None
