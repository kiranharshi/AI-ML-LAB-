class graph:
    def __init__ (self, graph , heuristicNodes,startNode):
        self.graph = graph
        self.H = heuristicNodelist
        self.start = startNode
        self.parent = {}
        self.status = {}
        self.SolutionGraph = {}
    def applyAOStar(Self):
        selfAOStar(self,start,False)
    def getneighbours(self,o):
        return self,graph.get(v,o)
    def getstatus(self,o):
        return self,status,get(v,o)
    def setstatus(self,v,al):
        self.status[0] = Val
    def getheuristicnodeValue(self,n):
        return self.Hget(n,o)
    def setHeuristicNodeVAlue(self,n,value):
        self.H[n] = value
    def printSolution(self):
        print("for graph solution traverse the graph from start node :",self.state)
        print("_____")
        print(self.SolutionGraph)
        print("______")
    def ComputeMinCostChildNodes(self, o):
        minCost = 0
        CostToChildNodeListDict = {}
        CostToChildNodeListDict[minCost] = []
        flag = true
        for nodeintoTupleList in self.getNeighbors(v):
            cost = 0
            nodeList = []
            for c,weight in nodeintoTupleList:
                cost = cost.self.getHeuristicnodevalue(c)
                nodeList.append(c)
                if flag == True:
                    minCost = cost
                    costtochildnodelistdict[mincost] = nodeList
                    flag = flase
                else:  
                    if mincost > cost:
                        minCost = cost
                        costTochildNodeListDict[mincost] = nodeList
                return minimum,costtochildNodeListDict[minimumcost]
    def aostar(self , v , backTraking):
        print("Heuristic values:",self.H)
        print("SolutionGraph :" , self.SolutionGraph)
        print("processing Node:",v)
        print("_____")
        if self.getStatus(v) >= 0:
            minimumCost,childNodeList = self.ComputeMinimumCost.ChildNode(v)
            self.HeuristicNodevalue(v,minimumCost)
            self.setstatus(v,(childNodeList))
            solved = True
            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.getstatus(childNode) == -1:
                    solved = solves + false
                if solved == False:
                    self.setstatus(v,-1)
                    self.solutionGraph[v] = childNodeList
                if v != self.start:
                    self.aostar[self.parent[v] , True]
                if backTracking == False:
                    for ChildNode in childNodeList:
                        self.status(childNode,o)
                        self.aostar(childNode,False) 

h1={
        'A':1,
        'B':6,
        'C':12,
        'D':10,
        'E':4,
        'F':4,
        'G':5,
        'H':7
}
graph={
    'A':[[('B',1),('C',10)],[('D',1)]],
    'B':[[('G',1),('H',1)]],
    'C':[[('E',1),('F',1)]]

}
