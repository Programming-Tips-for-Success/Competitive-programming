# Argument lists and keyword argument lists
def testArgLists_1(*args, **kwargs):
    print ('args:', args)
    print ('kwargs:', kwargs)
testArgLists_1('aaa', 'bbb', arg1='ccc', arg2='ddd')