from task_graph import TaskGraph

import math

def bisection_rec(SUMS, height, p, q, w, LOG):
    
    S = SUMS[q]
    
    if p > 0 :
        S -= SUMS[p-1]
        
    m_idx = None
    m_val = float("inf")
    
    l, u = 0, S
    
    for i in range(p, q):
        
        l += w[i]
        u -= w[i]
        
        cur = math.fabs(l - u)
        if cur < m_val :
            m_idx, m_val = i, cur
            
    result = [m_idx, ]
            
    if height == 0:
        return result
    else:
        left = bisection_rec(SUMS, height - 1, p, m_idx, w, LOG)
        right = bisection_rec(SUMS, height - 1, m_idx + 1, q, w, LOG)
        return left + result + right 

def bisection(N, m, w, LOG):
    SUMS = []
    
    acc = 0
    for w_i in w:
        acc += w_i
        SUMS.append(acc)
    
    return bisection_rec(SUMS, int(math.floor(math.log(N, 2))) - 1, 0, m-1, w, LOG)


def partition(N, m, c, w, LOG):

    i, j, p = 0, -1, 0
    
    schedule = []
    
    while p < N :
        
        S = 0
        while S <= c and j < m - 1 :
            j += 1
            S += w[j]
        
        if S > c :
            j -= 1
            schedule.append(j)
        else:
            return schedule            
            
        i = j + 1
        p += 1
    
    return None

def greedy(N, m, w, LOG):

    w_max = -float("inf")
    w_sum = 0

    for w_i in w:
        w_sum += w_i
        if w_i > w_max:
            w_max = w_i

    p = w_sum/N
    q = p + w_max
    prev_p = None
    
    while p < q or (p == q != prev_p):
        prev_p = p
        c = int(math.floor((p + q)/float(2)))
        schedule = partition(N, m, c, w, LOG)

        if schedule is None:
            p = c + 1
        else:
            q = c
    
    return schedule

def optimal(N, m, w, LOG):
    task_graph = TaskGraph(N, m, w)
    cp = task_graph.critical_path()
    if LOG:
        task_graph.LOG()
    return cp
    