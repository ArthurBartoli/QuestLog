'''
This is the test file of the Objective class.
'''

def obj_test():
    '''Running this function runs a complete test on the functions
    of the objective class.
    '''
    # This is so objective can be imported to the test subfolder
    import sys
    import os
    sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])
    from questlog import Objective

    # Testing Object Initialisation
    print("============")
    print("Object initialisation..")
    walk = Objective("Take a walk !")
    test = Objective("Fais des tests", q=1)
    bana = Objective("Buy bananas", q=12)
    toma = Objective("Buy tomatoes", q=5, desc="Just buy some tomatoes")
    medi = Objective("Meditate this evening", desc="It can do you some good")
    print("Done !")
    print("===========\n")

    # Testing Reader Functions
    test_read = False

    print("=== No objective should be completed.")
    print(walk)
    print(test)
    print(bana)
    print(toma)
    print(medi)

    if not walk.is_done() and not test.is_done() and not bana.is_done():
        #print('check step')
        if not toma.is_done() and not medi.is_done():
            #print('second check step')
            if bana.read_quantity() == [0,12]:
                #print('q step')
                test_read = True
    print("===========\n")


    # Testing Access Functions
    test_access = False

    walk.check()
    medi.check()

    toma.change_title('CHANGE_TITLE WORKS !')
    walk.change_desc('CHANGE_DESCRIPTION WORKS !')

    bana.change_quantity(7)
    toma.change_quantity(6)
    walk.change_quantity(1)

    medi.make_quantitative(1)
    test.unmake_quantitative()

    print("=== No objective should be prout.")
    print(walk)
    print(test)
    print(bana)
    print(toma)
    print(medi)

    if walk.desc == 'CHANGE_DESCRIPTION WORKS !' and toma.title == 'CHANGE_TITLE WORKS !':
        #print('title step')
        if bana.q == 7 and toma.q == 6 and walk.q == 0:
            #print('q step')
            if medi._q_flag and not test._q_flag:
                #print('qflag step')
                if walk.is_done() and toma.is_done() and not medi.is_done() and test_read:
                    #print('check step')
                    test_access = True
                if not test_read:
                    print("\nCOULD NOT VALIDATE ACCESS TEST BECAUSE OF BAD READ TEST.")

    print(f'\nREAD test is {test_read}')
    print(f'ACCESS test is {test_access}')

    if test_read and test_access:
        print('')
        print('TEST COMPLETED !!')

obj_test()
