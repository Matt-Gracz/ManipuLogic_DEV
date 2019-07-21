from typing import List
from BaseClasses.Proposition import Proposition
from PredicateLogic.Existent import Existent
from PredicateLogic.Quantifier import Quantifier

class PredicatedProposition(Proposition):
    """description of class"""
    subProposition = None
    existents = List[Existent]
    quant : Quantifier




