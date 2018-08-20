#Final Project
#Ryan Sleeper
#This program finds the most cost-effective way to push water through a city, as well as,
#the least cost-effective way to push water through a city.

class Vertex:
    def __init__(self, key):
        self.id = key
        self.color = 'white'
        self.connectedTo = {}
        
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        if len(self.connectedTo.keys()) == 0:
            return None
        else:
            return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
        

def cheapCityTraversal(city, startingPoint, path):
    smallestWeight = 100
    while len(path) < 6:
        for building in startingPoint.getConnections():
            newWeight = startingPoint.getWeight(building)
            if newWeight < smallestWeight and building.getId() not in path:
                smallestWeight = newWeight
                cheapestBuilding = building
        path.append(cheapestBuilding.getId())
        cheapCityTraversal(city, cheapestBuilding, path)
        break
    return path


def expensiveCityTraversal(city, startingPoint, path):
    heavyWeight = 0
    while len(path) < 6:
        for building in startingPoint.getConnections():
            newWeight = startingPoint.getWeight(building)
            if newWeight > heavyWeight and building.getId() not in path:
                heavyWeight = newWeight
                expensiveBuilding = building
        path.append(expensiveBuilding.getId())
        cheapCityTraversal(city, expensiveBuilding, path)
        break
    return path




        
def main():
    city = Graph()
    waterStation = city.addVertex('Water Station')
    buildingA = city.addVertex('A')
    buildingB = city.addVertex('B')
    buildingC = city.addVertex('C')
    buildingD = city.addVertex('D')
    buildingE = city.addVertex('E')
    city.addEdge('Water Station', 'A', 15)
    city.addEdge('Water Station', 'B', 1)
    city.addEdge('Water Station', 'E', 1)
    city.addEdge('A', 'Water Station', 15)
    city.addEdge('A', 'C', 10)
    city.addEdge('A', 'D', 5)
    city.addEdge('B', 'Water Station', 1)
    city.addEdge('B', 'C', 5)
    city.addEdge('B', 'E', 1)
    city.addEdge('C', 'A', 10)
    city.addEdge('C', 'B', 5)
    city.addEdge('C', 'D', 1)
    city.addEdge('C', 'E', 1)
    city.addEdge('D', 'A', 5)
    city.addEdge('D', 'C', 1)
    city.addEdge('D', 'E', 1)
    city.addEdge('E', 'Water Station', 1)
    city.addEdge('E', 'B', 1)
    city.addEdge('E', 'C', 1)
    city.addEdge('E', 'D', 1)
    
    
    print("These are the buildings in the city:")
    print(city.getVertices())
    print()
    print("Here is the list of water pipes connecting the buildings.")
    print("The last number is the price it takes to push the water through that pipe.")
    for vertex in city:
        for edges in vertex.getConnections():
            print("( %s, %s, %s )" % (vertex.getId(), edges.getId(), vertex.getWeight(edges)))
        print()
    print()
    
    cheapPath = []
    cheapPath.append(waterStation.getId())
    cheapPath = cheapCityTraversal(city, waterStation, cheapPath)
    print("The following path is the cheapest way to push water through the city.")
    print(cheapPath)
    print()
    
    expensivePath = []
    expensivePath.append(waterStation.getId())
    expensivePath = expensiveCityTraversal(city, waterStation, expensivePath)
    print("The following path is the most expenisve way to push water through the city.")
    print(expensivePath)
                
    
main()
    

    
    