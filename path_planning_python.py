import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while nodes:
            smallest = heapq.heappop(nodes)[1] # Vertex in nodes with smallest distance in distances
            if smallest == finish: # If the closest node is our target we're done so print the path
                path = []
                while previous[smallest]: # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize: # All remaining vertices are inaccessible from source
                break
            
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]: # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances
        
    def __str__(self):
        return str(self.vertices)
    
if __name__ == '__main__':
    def d(c, b):
        #print(((c[0] - b[0])**2 +(c[1] - b[1])**2)**0.5)
        return (((c[0] - b[0])**2 +(c[1] - b[1])**2)**0.5) 
    g = Graph()
    a= [[-77.9,-17.59] ,  #0
    [-77.86, 16.80],    #1
[-15.45, 194.16],  #2
[-4.32, 110.51],      #3
[-1.77, -23.78],  #4
[79.56, -7.79],   #5
[230.90,-40.58],  #6
[189.83,-58.67 ], #7
[161.58, -111.42], #8
[17.10, -130.70],  #9
[-9.35, -168.07],  #10
[-44.25, -193.47], #11
[-145.75, -75.70], #12
[-145.47, -7.79],  #13
[-104.58, -0.5] ,  #14
[-52.68, -0.91],   #15
[77.9,135.5],     #16 SECTION1 
[5,196.9],        #17 SECTION2
[82,196.9],       #18 SECTION3
[155,197.2],      #19 SECTION4
[235.7,8.9],      #20 SECTION5
[159.8,2.2],      #21 SECTION6
[153,69.8],       #22 SECTION7
[153,127.2],      #23 SECTION8
[87,132.9],       #24 SECTION9
[83.4,80.8],      #25 SECTION10
[83.4,11.5],      #26 SECTION11
[19.2,0],         #27 SECTION12
[0,19.2],         #28 SECTION13
[-19.2,0],        #29 SECTION14
[0,-19.2],        #30 SECTION15
[-6,-129.2],      #31 SECTION16
[-5.9,-194.2],    #32 SECTION17
[-77,-134.4],     #33 SECTION18
[-145.75,-75.7],  #34 SECTION19
[-0.6,130.2],     #35 SECTION20
[-77.9,-4.3],     #36 SECTION21
[-145.47,-7.79],  #37 SECTION22
[231.8,-51.3],    #38 SECTION23
[174,-66.9]];     #39 SECTION24
    g.add_vertex("SP", {"SECTION21": d(a[0],a[36]),"SECTION18": d(a[0],a[33]) }); 
    g.add_vertex("P1", {"SECTION21": d(a[1],a[36]), "SECTION1": d(a[1],a[36])}); 
    g.add_vertex("P2", {"SECTION2": d(a[2],a[36]), "SECTION1": d(a[2],a[36])}); 
    g.add_vertex("P3", {"SECTION20": d(a[3],a[36]),"SECTION13": d(a[3],a[36])}); 
    g.add_vertex("P4", {"SECTION15": d(a[4],a[36]),"SECTION16": d(a[4],a[36])}); 
    g.add_vertex("P5", {"SECTION12": d(a[5],a[36]), "SECTION11": d(a[5],a[36]), "SECTION6": d(a[5],a[36])}); 
    g.add_vertex("P6", {"SECTION5": d(a[6],a[36]),"SECTION23": d(a[6],a[36])});
    g.add_vertex("P7", {"SECTION23":d(a[7],a[36]),"SECTION24": d(a[7],a[36])});
    g.add_vertex("P8", {"SECTION24": d(a[8],a[36]),"P9": d(a[8],a[36])});    
    g.add_vertex("P9", {"P8": d(a[9],a[36]), "SECTION16": d(a[9],a[36])});  
    g.add_vertex("P10", {"SECTION17": d(a[10],a[36]),"SECTION16": d(a[10],a[36])});   
    g.add_vertex("P11", {"SECTION17": d(a[11],a[36]),"SECTION18": d(a[11],a[36])});   
    g.add_vertex("P12", {"SECTION18": d(a[12],a[36]), "SECTION19": d(a[12],a[36]),"P13": d(a[12],a[36])});  
    g.add_vertex("P13", {"SECTION22": d(a[13],a[36]), "SECTION19":d(a[13],a[36]),"P12": d(a[13],a[36])});
    g.add_vertex("P14", {"SECTION21": d(a[14],a[36]),"SECTION22": d(a[14],a[36])});   
    g.add_vertex("P15", {"SECTION21": d(a[15],a[36]),"SECTION14": d(a[15],a[36])});  
    g.add_vertex("SECTION1", {"P1": d(a[16],a[36]), "SECTION20": d(a[16],a[36]),"P2": d(a[16],a[36]),"SECTION22": d(a[16],a[36])});  
    g.add_vertex("SECTION2", {"P2": d(a[17],a[36]), "SECTION3": d(a[17],a[36]),"SECTION20": d(a[17],a[36])});  
    g.add_vertex("SECTION3", {"SECTION2": d(a[18],a[36]), "SECTION4": d(a[18],a[36]),"SECTION9": d(a[18],a[36])});  
    g.add_vertex("SECTION4", {"SECTION3": d(a[19],a[36]), "SECTION8": d(a[19],a[36])});  
    g.add_vertex("SECTION5", {"P6": d(a[20],a[36]), "SECTION6": d(a[20],a[36])});  
    g.add_vertex("SECTION6", {"SECTION11": d(a[21],a[36]), "SECTION7": d(a[21],a[36]),"SECTION5": d(a[21],a[36]),"P5": 1});  
    g.add_vertex("SECTION7", {"SECTION6": d(a[22],a[36]), "SECTION8": d(a[22],a[36]),"SECTION10": d(a[22],a[36])});  
    g.add_vertex("SECTION8", {"SECTION4": d(a[23],a[36]), "SECTION9": d(a[23],a[36]),"SECTION7": d(a[23],a[36])});
    g.add_vertex("SECTION9", {"SECTION3": d(a[24],a[36]), "SECTION8":d(a[24],a[36]),"SECTION10": d(a[24],a[36]),"SECTION20": d(a[24],a[36])});
    g.add_vertex("SECTION10", {"SECTION7": d(a[25],a[36]), "SECTION9": d(a[25],a[36]),"SECTION11": d(a[25],a[36])});
    g.add_vertex("SECTION11", {"SECTION6": d(a[26],a[36]), "SECTION10": d(a[26],a[36]),"SECTION12": d(a[26],a[36]),"P5": d(a[26],a[36])});
    g.add_vertex("SECTION12", {"SECTION15": d(a[27],a[36]), "SECTION13":d(a[27],a[36]),"SECTION11": d(a[27],a[36]),"P5": d(a[27],a[36])});
    g.add_vertex("SECTION13", {"SECTION14": d(a[28],a[36]), "SECTION12": d(a[28],a[36]),"P3": d(a[28],a[36])});
    g.add_vertex("SECTION14", {"SECTION15": d(a[29],a[36]), "SECTION13": d(a[29],a[36]),"P15": d(a[29],a[36])});
    g.add_vertex("SECTION15", {"SECTION14": d(a[30],a[36]), "SECTION12": d(a[30],a[36]),"P4": d(a[30],a[36])});
    g.add_vertex("SECTION16", {"P4": d(a[31],a[36]), "P10": d(a[31],a[36]),"P9": d(a[31],a[36])});
    g.add_vertex("SECTION17", {"P10": d(a[32],a[36]), "P11": d(a[32],a[36])});
    g.add_vertex("SECTION18",{"P11": d(a[33],a[36]), "SECTION16": d(a[33],a[36]),"SP": d(a[33],a[36]),"P12": d(a[33],a[36])});
    g.add_vertex("SECTION19", {"P12": d(a[34],a[36]), "P13": d(a[34],a[36]),"SECTION21": d(a[34],a[36])});
    g.add_vertex("SECTION20", {"P3": d(a[35],a[36]), "SECTION1": d(a[35],a[36]),"SECTION2": d(a[35],a[36]),"SECTION9": d(a[35],a[36])});
    g.add_vertex("SECTION21", {"SP":d(a[36],a[36]), "P1":d(a[36],a[36]),"P14": d(a[36],a[36]),"P15": d(a[36],a[36])});
    g.add_vertex("SECTION22", {"P14": d(a[37],a[36]), "P13":d(a[37],a[36]),"SECTION1": d(a[37],a[36])});
    g.add_vertex("SECTION23", {"P6": d(a[38],a[36]), "P7": d(a[38],a[36])});
    g.add_vertex("SECTION24", {"P8": d(a[39],a[36]), "P7": d(a[39],a[36])});
    print(g.shortest_path('P2', 'P8'))
