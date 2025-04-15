import random


# You’re defining a class called Vertex.
# This will represent a single word (or "node") in your Markov chain graph.
class Vertex:

    # This function runs when a new Vertex (word) is created.
    def __init__(self,value):
        # Stores the actual word (like "love" or "you").
        self.value = value

        # This dictionary keeps track of what words come after this word and how often.
        # Example: if self.value == "love" → adjacent = {<Vertex "you">: 3, <Vertex "me">: 1}
        self.adjacent = {}

        # These two lists are used later to store the data in a way that works with random.choices():
        # neighbour = list of possible next words
        # neighbourWeight = how often each next word appeared
        self.neighbour = []
        self.neighbourWeight = []
    
    # This function adds a direct connection from this word to another word (vertex).
    def add_edge_to(self,vertex,weight=0):

        # Sets the number of times that word (vertex) appears after this one.
        self.adjacent[vertex] = weight
    
    # Increments the count of how many times this word is followed by vertex.
    def increment_edge(self,vertex):

        # If vertex is not already connected, it starts at 0.
        # Then it increases the count by 1.
        # Example: if "you" follows "love" three times, weight becomes 3.
        self.adjacent[vertex] = self.adjacent.get(vertex,0)+1

    # This method builds two lists: neighbour and neighbourWeight.
    def getProbabilityMap(self):

        # Loops through each connected word (vertex) and how often it followed this one (weight).
        for vertex,weight in self.adjacent.items():

            # Adds the word to neighbour, and its count to neighbourWeight.
            # Example:
                # self.neighbour = [<Vertex "you">, <Vertex "me">]
                # self.neighbourWeight = [3, 1]
            self.neighbour.append(vertex)
            self.neighbourWeight.append(weight)
            # These lists are now ready for probability-based word picking.
            
    # This returns a word that should come next, based on learned frequencies.
    def next_word(self):

        # random.choices() picks one element from neighbour list,
        # Based on the probability defined in neighbourWeight.
        # The [0] is because random.choices() returns a list (even if you ask for one item), so we get the first item.
        return random.choices(self.neighbour,weights=self.neighbourWeight)[0]

#  ----------------------------------------------------------------------------------------------------------


# You’re defining a class named Graph.
# It will hold all the Vertex objects (i.e. all words in the song/text) and their connections.
class Graph:

    # Initializes an empty dictionary called vertices
    # This dictionary stores all words (as Vertex objects), where:
    # key = word (e.g. "love")
    # value = Vertex("love")
    def __init__(self):
        self.vertices = {}
    
    # Returns a set of all the unique word strings in the graph.
    # Good if you want to see all the words used in the chain.
    def getVerticesValues(self):
        return set(self.vertices.keys())
    
    # Creates a new Vertex (word) and stores it in vertices.
    # Doesn’t check for duplicates — it assumes the caller checks first.
    def add_vertex(self,value):
        self.vertices[value] = Vertex(value)

    # If the word doesn’t exist in the graph, it creates it.
    # Then returns the corresponding Vertex.
    # Used when building the graph word-by-word.
    def getVertex(self,value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]
    

    # Takes a Vertex and gets the next word using its next_word() method.
    # currVertex.value gives the word string, which is used to access the correct Vertex in self.vertices.
    def getNextWord(self,currVertex):
       return  self.vertices[currVertex.value].next_word()
    
    # Loops through all the vertices (words).
    # Calls getProbabilityMap() on each one — this sets up the neighbour and neighbourWeight lists for that word.
    # Basically, it’s preparing all words to be ready for random.choices().
    def generateProbabilityMapping(self):
        for vertex in self.vertices.values():
            vertex.getProbabilityMap()

# ----------------------------------------------------------------------------------------------------
