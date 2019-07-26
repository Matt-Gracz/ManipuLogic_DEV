from UnitTesting import UnitTestSuite, UnitTest
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
from PredicateLogic.SecondOrderLogic.Set import Set

def runAllTests(mode : int) -> bool:
    testSuite : UnitTestSuite = UnitTestSuite()

    modulesToTest = [Existent, Predicate, PredicatedProposition, Quantifier, Variable, ExistQuant, \
        FirstOrderProp, UniversalQuant, Function, SecondOrderProp, Set]
    for module in modulesToTest:
        testSuite.addUnitTest(UnitTest(module()))

    return testSuite.runTestSuite()
