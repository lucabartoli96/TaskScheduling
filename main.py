from alg import bisection, greedy, optimal

import math

        
def insert_int(msg):
    while(True):
        typed = raw_input(msg)
    
        if typed.isdigit():
            return int(typed)
        else:
            print "Must be a positive integer!"
        
        
def print_schedule(msg, w, schedule):
    
    s = ""
    
    for i in range(len(w)):
        s += str(w[i]) + " "
        if i in schedule :
            s += "| "
    print msg
    print s
    
    
def is_pow_of_two(n):
    return math.log(n, 2) == math.floor(math.log(n, 2))
    
def main(): 

    N = insert_int('N := ')
    m = insert_int('m := ')
    
    while(m < N):
        print "m must be bigger or equal to N"
        m = insert_int('m := ')
    
    w = list()
    for i in range(m):
        w.append(insert_int('t_%d := ' % i))

#    N = 8
#    m = 12
#    w = [2, 3, 4, 1, 1, 3, 4, 5, 6, 9, 2, 4]
#    N = 4
#    m = 9
#    task = [2, 6, 2, 2, 1, 1, 2, 2, 2]
#    N = 3
#    m = 5
#    w = [3, 2, 4, 2, 4]

    if is_pow_of_two(N):
        print_schedule("Bisection Algorithm", w, bisection(N, m, w))

    print_schedule("Greedy Algorithm", w, greedy(N, m, w))

    print_schedule("Static Optimal Algorithm", w, optimal(N, m, w))
    
