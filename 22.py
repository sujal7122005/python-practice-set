#  Write a function func1() such that it can accept a variable length of argument and print 
# all arguments value func1(20, 40, 60) func1(80, 100). 

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)