
class TaskGraph(object):

    def __init__(self, N, m, w):
    
        Sentinel, TaskChain = self._init_subclasses(w)
        
        self._levels = self._init_levels(N, m, Sentinel, TaskChain)
        self._connect_levels(N, m)
    
    def critical_path(self):
        
        N = len(self._levels)-2
        
        S = self._levels[0][0]
        T = self._levels[N+1][0]
        
        for node in self._levels[1]:
            node.l = 0
            node.parent = S
        
        for i in range(1, len(self._levels)):
            for node in self._levels[i]:
                node.step()
        
        schedule = []
        node = T.parent.parent
        while node != S:
            schedule.insert(0, node.j)
            node = node.parent
            
        return schedule
            
        
    def _init_levels(self, N, m, Sentinel, TaskChain):
        levels = [];
        
        levels.append([Sentinel("S"), ])
        
        level = []
        for j in range(m-N+1):
            level.append(TaskChain(0, j))
        
        levels.append(level)
        
        for k in range(2, N):
            level = []
            lim_sup = m - (N - k)
            for i in range(k-1, lim_sup):
                for j in range(i, lim_sup):
                    level.append(TaskChain(i, j))
            levels.append(level)
        
        level = []
        for i in range(N-1, m):
            level.append(TaskChain(i, m-1))
        
        levels.append(level)
                    
        levels.append([Sentinel("T"), ])
        
        return levels
    
    def _connect_levels(self, N, m):
        
        S = self._levels[0][0]
        
        for node in self._levels[1]:
            S.connect(node)
        
        for k in range(1, N):
            for u in self._levels[k]:
                for v in self._levels[k+1]:
                    if v.i == u.j+1:
                        u.connect(v)
        
        T = self._levels[N+1][0]
        
        for u in self._levels[N]:
            u.connect(T)
            
    
    def LOG(self):
        
        print "\nSTEP 1"
        
        print "\nP_i = 'i-th Processor'"
        print "(i, j) = 'task chain from i to j'\n"
        
        for i, level in enumerate(self._levels):
            str_level = "P_" + str(i) + "-> "
            for node in level:
                str_level += node.name + " "
            print str_level
            
        print "\nSTEP 2-3"
        
        print "\n(i, j) --> [w, (i_1, j_1)], ..., [w, (i_1, j_1)] = "
        print "'edges from the node (i, j) to (i_k, j_k), with k = 1, ..., n, weighted w'\n"
        
        for i, level in enumerate(self._levels):
            print "P_" + str(i)
            for node in level:
                node.printConnected()
                
        print "\nSTEP 4"
        print "\n[l, (i, j)] = 'l is the weight of the node (i, j)'\n"
        
        for i, level in enumerate(self._levels):
            str_level = "P_" + str(i) + "-> "
            for node in level:
                str_level += "[" + str(node.l) + ", " + node.name + "] "
            print str_level
        print ""
    
    def _init_subclasses(self, w):
            
            SUMS = []
            acc = 0 
            for w_i in w:
                acc += w_i
                SUMS.append(acc)
            
            
            class Node(object):
                
                def __init__(self):
                    self._connected = []
                    self._l = float("inf")
                
                @property    
                def name(self):
                    pass
                
                def connect(self, node):
                    self._connected.append(node)
                    
                @property
                def w(self):
                    pass
                
                @property
                def l(self):
                    return self._l
                
                @l.setter
                def l(self, l):
                    self._l = l
                
                def step(self):
                    for node in self._connected:
                        l = max(self.w, self.l)
                        if node.l > l:
                            node.l = l
                            node.parent = self
                
                def printConnected(self):
                    connected = " " + self.name + "-->"
                    if self._connected:
                        for node in self._connected:
                            connected += " [" + str(self.w) + ", " + node.name + "]"
                    else:
                        connected += " None"
                    print connected
            
            
            class Sentinel(Node):
                
                def __init__(self, name):
                    super(Sentinel, self).__init__()
                    self._name = name
                
                @property
                def name(self):
                    return self._name
                
                @property
                def w(self):
                    return 0
                
            
            class TaskChain(Node):
                
                def __init__(self, i, j):
                    super(TaskChain, self).__init__()
                    self._i = i
                    self._j = j
                
                @property
                def name(self):
                    return "(" + str(self.i) + ", " + str(self.j) + ")" 
                
                @property
                def i(self):
                    return self._i
                
                @property
                def j(self):
                    return self._j
                
                @property
                def w(self):
                    w = SUMS[self.j]
                    if self.i != 0 :
                        w -= SUMS[self.i-1]
                    return w

            return Sentinel, TaskChain
                    
                
            