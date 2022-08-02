import sys

def exercise1():
    a = u'abcd'
    print (a)
    # b = unicode('efgh')
    # print (b)
    a = 'abcd'.decode('utf­8')
    print (a)
    b = 'abcd'.decode(sys.getdefaultencoding())
    print (b)

exercise1()
