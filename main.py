_running : bool = False

def RunManipuLogic(doRunUnitTests : bool = False) -> int:

    #Step 1: Setup
    #Prevent multiple instances of ManipuLogic from executing simultaneously on the same machine.
    global _running
    if(_running):
        return 1
    _running = True

    #Step 2: Run UnitTest modules if specificed
    if(doRunUnitTests):
        runUnitTests()
    
    #Step 3: Run ManipuLogic application
    pass

    print("Exiting ManipuLogic")
    return 0;

def runUnitTests():
    from BaseClasses import UnitTests as BaseUnitTests
    from SententialLogic import UnitTests as SententialUnitTests
    from PredicateLogic import UnitTests as PredicateUnitTests
    modules = [BaseUnitTests, SententialUnitTests, PredicateUnitTests]
    results = {}
    mode : int = 0 #run in silent mode
    try:
        for module in modules:
            results[str(module)] = module.runTests(mode)
        keys = results.keys()
        for key in keys:
            printableKey = key[key.find("module ") : key.find(" from")]
            print("Result for {} is: {}".format(printableKey, str(results[key])))
    except Exception as e:
        print("Error encountered while running unit tests")
        print("Internal python exception text: " + str(e))