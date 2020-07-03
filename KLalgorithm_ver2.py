# KL algorithm
# KL algorithm for weighted, 2n node graph
# 07/01/2020
# Junkyu Kwon
# email: junkyuk1@umbc.edu


# Sample graph using dictionary
g1 = {
    1: [5, 6, 7, 8, 10],
    2: [3, 4],
    3: [2, 6, 8],
    4: [2, 5, 9],
    5: [4, 1],
    6: [1, 3],
    7: [1],
    8: [1, 3],
    9: [4],
    10: [1]
}

# Edges of the Sample graph, using List. This is [Node1, Node2, Weight]
edges1 = [
    [1, 6, 120],
    [2, 3, 80],
    [3, 8, 30],
    [4, 2, 300],
    [5, 4, 100],
    [5, 1, 100],
    [6, 3, 100],
    [7, 1, 100],
    [8, 1, 100],	
    [9, 4, 150],
    [10, 1, 30]
]

#Sample 2
g2 = {
    1: [6, 7, 8],
    2: [3, 4],
    3: [2, 6, 8],
    4: [2, 5],
    5: [4],
    6: [1, 3],
    7: [1],
    8: [1, 3]
}

edges2 = [
	[1, 6, 120],
	[2, 3, 80],
	[3, 8, 30],
	[4, 2, 300],
	[5, 4, 100],
	[6, 3, 100],
	[7, 1, 100],
	[8, 1, 100]	
			]



# Find an element from graph(dictionary)
def findElement(n, graph):
    x = 0;
    for i in graph:
        if n in graph[i]:
            x+=1
    return x

# Find a Weight between two nodes
def getWeight(node1, node2, edges):
    weight = 0;
    for i in range(0,int(len(edges))):
        if node1 == edges[i][0]:
            if node2 == edges[i][1]:
                weight = edges[i][2]
        if node2 == edges[i][0]:
            if node1 == edges[i][1]:
                weight = edges[i][2]

    
    return weight        

# Find D values
def Dvalues(v1, v2, graph):
    D = {};

    E = {};
    I = {};
    
    #find External
    for i in v1:
        E[i] = findElement(i,v2);
    for i in v2:
        E[i] = findElement(i,v1);
    #find Internal
    for i in v1:
        I[i] = findElement(i,v1);
    for i in v2:
        I[i] = findElement(i,v2);

    #D values
    for i in v1:
        D[i] = E.get(i)-I.get(i);
    for i in v2:
        D[i] = E.get(i)-I.get(i);

    return D

# Main KL algorithm
def KL_alg(graph, edges):

    #initial partition
    #only for a graph with 2n nodes
    sizev = len(graph);
    
    g_max = 1;

    #Slice graph(dictionary) in half    
    v1 = dict(list(graph.items())[len(graph)//2:]) 
    v2 = dict(list(graph.items())[:len(graph)//2:]) 
    print ("\nInitial Partition v1: ")
    print(v1)
    print ("\nInitial Partition v2: ")
    print(v2)

    #The main algorithm
    while g_max > 0:
        D = Dvalues(v1,v2, graph);
        gain = {};
        cost = 0;
        
        # gain = Da-Db-2*cost
        for i in v1:
            for j in v2:
                if j in v1.get(i):
                    cost = getWeight(i,j, edges);
                    
                else:
                    cost = 0;
                gain.update({i*sizev+j:D[i]+D[j]-2*cost});
                
        #find g_max
        g_max = max(list(gain.values()))
        
        #get Total weight between v1 and v2
        TotalWeight = 0
        
        for i in v1:
            for j in v2:
                TotalWeight += getWeight(i,j, edges)
        print("Total weight between v1 and v2 is: ")
        print(TotalWeight)
        
        k1 = 0;
        k2 = 0;
        
        for i in v1:
            for j in v2:
                #swap v1[k1] and v2[k2]
                if i*sizev+j in gain:
                    if g_max == gain[i*sizev+j]:
                        k1 = i;
                        k2 = j;
                        tempv1 = v1.pop(k1)
                        tempv2 = v2.pop(k2)
                        v1.update({k2:tempv2})
                        v2.update({k1:tempv1})
                        break

    #main algorithm ends here. This repeats until g_max<=0

    #Final output
    print ("\nFinal Partition v1: ")
    print(v1)
    print ("\nFinal Partition v2: ")
    print(v2)


#Main
KL_alg(g1, edges1)
KL_alg(g2, edges2)