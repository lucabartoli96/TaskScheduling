# TaskScheduling

The application implements three algorithms for the following problem:

### input: 
* ![equation](http://latex.codecogs.com/gif.latex?N) number of processors
* ![equation](http://latex.codecogs.com/gif.latex?m\&space;\geq\&space;N) number of tasks
* ![equation](http://latex.codecogs.com/gif.latex?t_i\&space;\forall&space;i&space;\in&space;{1,&space;\dots,&space;m-1}), execution time of each task.

Let also be:\
![equation](http://latex.codecogs.com/gif.latex?W(i,\&space;j)\&space;=\&space;\sum_{k=1}^{j}\&space;t_k)

### output:
![equation](http://latex.codecogs.com/gif.latex?schedule\&space;=\&space;<i_0,\&space;i_1,\&space;\dots,\&space;i_k>)
where:
* ![equation](http://latex.codecogs.com/gif.latex?k&space;\leq&space;N)
* ![equation](http://latex.codecogs.com/gif.latex?(i_j,&space;i_{j&plus;1})\&space;\forall&space;j=&space;0,&space;\dots,&space;k-1) is the task chain assigned to the j-th processor

and where:\
![equation](http://latex.codecogs.com/gif.latex?<i_0,&space;i_1,&space;\dots,&space;i_k>&space;=&space;argmin\{\max_{j=0,\dots,k-1}{W(i_j,&space;i_{j&plus;1})}\})

So the schedule is the optimal assignment of the m tasks to the N processors

## Bisection Algorithm

Let ![equation](http://latex.codecogs.com/gif.latex?N&space;=&space;2^k) (indeed the procedure is called only if the number given is a power of two). The method recursively divides the list into two taskchains ![equation](http://latex.codecogs.com/gif.latex?(p,&space;c),(c&plus;1,q)) where ![equation](http://latex.codecogs.com/gif.latex?p) and ![equation](http://latex.codecogs.com/gif.latex?q) are the lower and thew upper bounds of the recursive call, and:\
![equation](http://latex.codecogs.com/gif.latex?c&space;=&space;arg\min_{i=p&plus;1,&space;\dots,&space;q-1}\{|W(p,i)-W(i&plus;1,&space;q)|\})\
The recursion three is binary and has ![equation](http://latex.codecogs.com/gif.latex?k) levels, so that the result task chains are exactly ![equation](http://latex.codecogs.com/gif.latex?2^k&space;=&space;N)\
The cost of the algoritm is ![equation](http://latex.codecogs.com/gif.latex?O(m\log_{2}{N})), but the solution is suboptimal.

## Greedy Algorithm

Let ![equation](http://latex.codecogs.com/gif.latex?W_{sum}) the sum of the execution time of al tasks, ![equation](http://latex.codecogs.com/gif.latex?W_{max) the execution time of the task with the maximum excecution time and ![equation](http://latex.codecogs.com/gif.latex?W_{opt}) the execution time of the heaviest task. Then can be proved that:\
![equation](http://latex.codecogs.com/gif.latex?\frac{W_{sum}}{N}&space;\leq&space;W_{opt}&space;\leq&space;\frac{W_{sum}}{N}&space;&plus;&space;W_{max})\
The algorithm is just a binary search of the lowest execution time ![equation](http://latex.codecogs.com/gif.latex?c) for which exists a partition (or schedule) for which the execution time of the taskchain with the maximum excecution time is lower than ![equation](http://latex.codecogs.com/gif.latex?c) 

## Optimal Static Algorithm

This procedure executes four steps:
#### step 1
It creates the vertex set of a graph, in which every node (except for the two sentinels) are like ![equation](http://latex.codecogs.com/gif.latex?(i,j)), representing a task chain. Vertexes are created and divided in levels:
* **level 0** contains the sentinel node S
* **level 1** contains the nodes ![equation](http://latex.codecogs.com/gif.latex?(0,j)\&space;\forall&space;j=1,\dots,m-N)
* **level k** contains the node ![equation](http://latex.codecogs.com/gif.latex?(i,j)\forall&space;i=k-1,\dots,m-(N-k+1)\&space;\forall&space;j=i,\dots,m-(N-k)) and ![equation](http://latex.codecogs.com/gif.latex?k=2,\dots,N-1)
* **level N** contains the nodes ![equation](http://latex.codecogs.com/gif.latex?(i,m)\&space;\forall&space;j=N,\iots,m)
* **level N+1** contains the sentinel node T
### step 2
Then the edges are created:
* ![equation](http://latex.codecogs.com/gif.latex?S) is connected to all the nodes of the level 1
* ![equation](http://latex.codecogs.com/gif.latex?(i,j)\forall&space;k=1,\dots,N-1) is connected to ![equation](http://latex.codecogs.com/gif.latex?(j+1,q)) of the k+1 level
* ![equation](http://latex.codecogs.com/gif.latex?T) is connected to all the nodes of the level N+1
### step 3
The edges are weighted:
* The weights of the edges from ![equation](http://latex.codecogs.com/gif.latex?S) to the level 1 are 0
* The weight of the edges from ![equation](http://latex.codecogs.com/gif.latex?(i,j)\forall&space;k=1,\dots,N-1) to all the nodes of the level k+1 are ![equation](http://latex.codecogs.com/gif.latex?W(i,\&space;j))

### step 4

Now the aim of the algorithm is looking for the path from S to T in which the weight of the heaviest edge is minimum, called the critical path. The procedure is assigning weights to the nodes:
* ![equation](http://latex.codecogs.com/gif.latex?l(0,&space;j)&space;=&space;0) for all nodes on the level 1
* ![equation](http://latex.codecogs.com/gif.latex?l(i&space;,&space;j)&space;=&space;\infty) for all the other nodes

let's start from the top (level 1), and descend. Taken ![equation](http://latex.codecogs.com/gif.latex?a) (upper) and ![equation](http://latex.codecogs.com/gif.latex?b) (lower), let's update ![equation](http://latex.codecogs.com/gif.latex?l(b)) with the following form:\
![equation](http://latex.codecogs.com/gif.latex?l(b)=\min\(l(b),\max\(w(e),l(a)\)\))
\
where ![equation](http://latex.codecogs.com/gif.latex?e) is the edge between the two nodes, and let's save as the parent of a node, the upper node ![equation](http://latex.codecogs.com/gif.latex?a) that updates the value.\
The critical path is just the path that you get by traversing back the graph, using all the parents dave during the execution, starting from T.

