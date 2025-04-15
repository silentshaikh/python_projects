from graph import Graph, Vertex
import string,random,re,os

# This function takes one argument: textPath – the path to a text file (like a song lyrics file).
# It will return a list of cleaned words from that file.
def getWordFromText(textPath):

    # Opens the file at the path textPath in read mode using UTF-8 encoding.
    with open(textPath,"r",encoding="utf-8") as f:
    # f.read() reads the entire file into a variable called text.
        text = f.read() 

        # Removes any content inside square brackets (e.g. [Chorus], [Verse 1]) using a regex.
        # re.sub() replaces anything like [...something...] with just a space.
        text = re.sub(r"\[(.+)\]"," ",text)

        # .split() splits the text into a list of words (removing all extra spaces, tabs, newlines).
        # " ".join(...) joins the words back with just one space between each.
        # So you get a clean, evenly spaced string.
        text  = " ".join(text.split())

        # Converts the whole text to lowercase, so Love and love are treated the same.
        text = text.lower()

        # Removes all punctuation marks (like . , ! ?) from the text.
        # str.maketrans("", "", string.punctuation) tells translate() to delete all characters in string.punctuation.
        text = text.translate(str.maketrans("","",string.punctuation))
    
    # Now splits the cleaned string into a list of individual words.
    word  = text.split()

    # Returns the final list of words (no punctuation, no brackets, all lowercase, all clean).
    return word

# -------------------------------------------------------------------------------------------------------------

# This function takes one argument: words, which is a list of words (already cleaned and split using getWordFromText()).
# It will build a graph where each word is a node, and edges represent which word comes after which — based on the order in the list.
def makeGraph(words):

    # Creates a new instance of your custom Graph class — starts with no vertices (words) yet.
    the_graph = Graph()

    # This is used to remember the word that came before the current one during the loop.
    # At first, there’s no previous word, so it’s set to None.
    previousWord= None

    # Loops through each word in the input list to build connections between them.
    for word in words:

        # If the word already exists in the graph, returns its corresponding Vertex.
        # If the word doesn’t exist, it adds a new Vertex to the graph and returns it.
        wordVertex = the_graph.getVertex(word)

        # If this is not the first word:
        # Adds/increments an edge from previousWord to the current wordVertex.
        # This means: "This word came after the previous one", so the connection is strengthened.
        if previousWord:
            previousWord.increment_edge(wordVertex)
        
        # Updates previousWord to be the current word, so that in the next loop, it knows what came before.
        previousWord = wordVertex
    
    # Once the graph is built, this function goes through all vertices and:
    # Converts their edge weights (how often a word follows another) into a probability mapping.
    # Prepares for random word selection based on actual word frequencies.
    the_graph.generateProbabilityMapping()

    # Returns the fully built graph object — this is now a Markov Chain based on the input words!
    return the_graph

# -------------------------------------------------------------------------------------------------------------


# This function generates a new sequence of words.

# Parameters:
# graph: The Markov Chain graph (built from all the song lyrics or words).
# words: The original word list (used to randomly pick a starting word).
# length: The number of words to generate (default is 50).
def compose(graph,words,length=50):

    # This list will hold the words of the generated composition (the final result).
    composition =[]

    # Randomly picks one word from the input words list.
    # Gets its corresponding Vertex from the graph.
    # This is the starting point of the generated sentence/lyrics.
    word  = graph.getVertex(random.choice(words))

    # Loops length times (default is 50) to generate a chain of words.
    for _ in range(length):

        # Appends the current word's value (the string) to the composition list.
        composition.append(word.value)

        # Picks the next word using the Markov Chain logic:
        # Looks at all words connected to the current word.
        # Chooses the next word based on how often each word appears after the current one (using random.choices() with weights).
        word = graph.getNextWord(word)
    
    # Returns the full list of generated words.
    # Later, you can use " ".join(composition) to turn it into a sentence/lyrics string.
    return composition

#  ----------------------------------------------------------------------------------------------------------


# This defines the main() function.
# It takes artist as an argument, which is the name of the folder containing that artist’s songs.
# Example: "taylor_swift" will look into songs/taylor_swift/.
def main(artist):

    # This is a commented-out line from when the program maybe worked with books or text files instead of songs.
    # It shows you could've used it with other text sources too
    # words = getWordFromText("texts/hp_sorcerer_stone.txt")

    # Initializes an empty list words to collect all the words from every song file of the artist.
    words = []

    # This loops over every file in the directory songs/{artist}.
    # So for "taylor_swift", it will look into the folder: songs/taylor_swift.
    for songFile in os.listdir(f'songs/{artist}'):

        # On Mac, a file called .DS_Store is automatically created by the OS.
        # This line skips that file because it’s not a real song text.
        if songFile == ".DS_Store":
            continue
        
        # Calls your getWordFromText() function on the current song file.
        # It reads the file, cleans the text (removes brackets, punctuation, lowercase), and returns a list of words
        songWords= getWordFromText(f"songs/{artist}/{songFile}")

        # Adds all the words from the current song to the big words list.
        words.extend(songWords)

    # This builds the Markov Chain graph using the words list.
    # Each word becomes a vertex, and it learns which word usually follows which
    the_graph = makeGraph(words)

    # Generates a new song-like sequence of 100 words.
    # Uses the compose() function, powered by your graph.
    composition = compose(the_graph,words,100)

    # Joins all the generated words together with no spaces (⚠️ tiny issue).
    # You might want to use " ".join(composition) instead to add spaces between words.
    return "".join(composition)



# Runs the main() function using "taylor_swift" as the artist folder.
# It prints out a new randomly generated set of lyrics that sound like Taylor Swift (based on her actual lyrics)!
print(main("taylor_swift"))