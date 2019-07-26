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
from PredicateLogic.SecondOrderLogic.LogicSet import LogicSet

def runAllTests(mode : int) -> bool:
    testSuite : UnitTestSuite = UnitTestSuite()
    modules = [Existent, Predicate, PredicatedProposition, Quantifier, Variable, ExistQuant, \
        FirstOrderProp, UniversalQuant, Function, SecondOrderProp, LogicSet]
    unitTests = [UnitTest(module) for module in modules]
    testSuite.setTestList(unitTests)
    return testSuite.runTestSuite()
