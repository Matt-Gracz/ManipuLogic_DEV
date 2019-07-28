from UnitTesting import UnitTesting
from PredicateLogic.Existent import Existent
from PredicateLogic.Predicate import Predicate
from PredicateLogic.PredicatedProposition import PredicatedProposition 
from PredicateLogic.Quantifier import Quantifier
from PredicateLogic.Variable import Variable
from PredicateLogic.FirstOrderLogic.ExistQuant import ExistQuant
from PredicateLogic.FirstOrderLogic.FirstOrderProp import FirstOrderProp
from PredicateLogic.FirstOrderLogic.UniversalQuant import UniversalQuant
from PredicateLogic.SecondOrderLogic.Function import Function
from PredicateLogic.SecondOrderLogic.SecondOrderProp import SecondOrderProp
from PredicateLogic.SecondOrderLogic.LogicSet import LogicSet

def runAllTests(mode : int) -> bool:
    return UnitTesting().runTestSuite([Existent, Predicate, PredicatedProposition, Quantifier, Variable, ExistQuant, \
        FirstOrderProp, UniversalQuant, Function, SecondOrderProp, LogicSet])
