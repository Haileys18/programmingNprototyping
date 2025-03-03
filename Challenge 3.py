#Hailey Sooknanan
#Period 5-6
#3/3
#Challenge #3

def do_twice(func, value):
    func(value)
    func(value)

def print_twice(string):
    print(string)
    print(string)

def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)

# Test the functions
do_four(print_twice, 'spam')
