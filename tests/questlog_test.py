'''
This is the test file for the QuestLog class
'''

def questlog_test():
    '''Running this function runs a complete test on the functions
    of the questlog class.
    '''
    # This is so I can import obj to the test subfolder
    import sys
    import os
    sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])

    from obj.questlog import QuestLog

    temp = ["Banane", "Haricot", "Figue"]

    # Testing object initialization
    x = QuestLog('Liste de course')

    # Testing Read Functions
    test_read = False
    temp=[]
    test=[]

    x.add_objective("Banane")
    x.add_objective("Meditate a little", desc="Just do it in the evening")
    x.add_objective("Buy oranges", qty=10, desc="It's full of vitamin C !")
    x.add_objective("Buy bananas", qty=5)

    for i in range(4):
        if not x.is_done(i):
            temp.append(True)
        else:
            temp.append(False)
    if all(temp):
        test.append(True)
    else:
        test.append(False)

    if x.read_quantity(2) == [0, 10] and not x.read_quantity(0):
        test.append(True)
    else:
        test.append(False)

    if len(x) == 4:
        test.append(True)
    else:
        test.append(False)

    if x.read_desc(0) == "" and x.read_desc(1) == "Just do it in the evening":
        test.append(True)
    else:
        test.append(False)
    
    if x.read_name() == 'Liste de course':
        test.append(True)
    else:
        test.append(False)

    if x.read_title(0) == "Banane" and x.read_title(1) == "Meditate a little":
        test.append(True)
    else:
        test.append(False)

    if all(test):
        test_read = True

    # Testing Access Functions
    test_access = False
    test=[]
    x.check_objective(0)
    x.change_title(0, "TOMATOES")

    x.change_desc(1, "CHANGED DESC")

    x.change_quantity(2, 10)

    x.change_quantity(3, 4)
    x.change_max_quantity(3, 3)

    if x.is_done(0) and x.read_title(0) == "TOMATOES":
        test.append(True)
    else:
        test.append(False)

    if x.read_desc(1) == "CHANGED DESC":
        test.append(True)
    else:
        test.append(False)

    if x.read_quantity(2) == [10, 10] and x.is_done(2):
        test.append(True)
    else:
        test.append(False)

    if x.read_quantity(3) == [4, 3] and x.is_done(3):
        test.append(True)
    else:
        test.append(False)

    x.change_max_quantity(3, 6)
    if not x.is_done(3):
        test.append(True)
    else:
        test.append(False)

    if all(test) and test_read:
        test_access = True

    # Testing Utils functions
    test_utils = False
    if x.search_log('orang') == 2:
        test_utils = True

    print("test read is", test_read)
    print("test access is ", test_access)
    print("test utils is", test_utils)
    if test_read and test_access and test_utils:
        print("")
        print("QUESTLOG TEST COMPLETE !")
        return True
    return False
