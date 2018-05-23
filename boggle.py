from string import ascii_uppercase
from random import choice

def make_grid(cols, rows):
    return {(c, r): choice(ascii_uppercase) 
                    for c in range(cols) 
                    for r in range(rows)}

def get_neighbours(pos):
    col, row = pos
    return [
            (col-1, row-1), 
            (col, row-1),
            (col+1, row-1),
            (col+1, row),
            (col+1, row+1),
            (col, row+1),
            (col-1,row+1),
            (col-1,row),
            ]
            
def all_grid_neighbours(grid):
    return {pos: [ n for n in get_neighbours(pos) if n in grid] for pos in grid}

def path_to_word(grid, path):
    word = ""
    for pos in path:
        word = word + grid[pos]
    return word
#------------------------------------------------------------------------------------------------#
#read word file/list---------------
#Two ways of converting a file full of lowercase words to a list of upper case words
#If you had to pay one penny to convert a string to an upper case string, which of these two versions of #read_wordfile would be more expensive, and by how much?
def read_wordfile(filename):
    #full_words = set()
    #stems = set()
    f = open(filename, "r")
    text = f.read().upper()
    words = text.splitlines()
    f.close()
    
    #for word in full_words:
        #for i in range(1,len(word)):
                   # stems.add(word[:i])
    
    return set(words)
    

# def read_wordfile(filename):
#     f = open(filename, "r")
#     words = f.read().splitlines()
#     words = [ word.upper() for word in words]
#     f.close()
#     return words
#------------------------------------------------------------------------------------------------------#

def search(grid, wordlist):
    all_neighbours = all_grid_neighbours(grid)

    def do_search(path, positions):
        # If no more positions to search, there won't be any more words    
        if positions == []:
            return []
        
        # Extend the path by the first position and check if it's a word    
        this_position = positions[0]
        this_path = path + [this_position]
        this_word = path_to_word(grid, this_path)
        # Either it was a word, or it wasn't
        if this_word in wordlist:
            words = [this_word]
        else:
            words = []

        # Find which neighbours of the current position, have not been used
        # Search on extending the current path by the neighbours
        neighbours = [n for n in all_neighbours[this_position] if n not in path]
        words += do_search(this_path, neighbours)
        
        # Search on from the last path, using the siblings of the current position
        words += do_search(path, positions[1:])
        
        # Return all the words found on this branch
        return words
            
    return do_search([], list(grid.keys()))   



def display(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))

def main():
    grid = make_grid(4, 4)
    dictionary = read_wordfile("bogwords.txt")
    words = set(search(grid, dictionary))
    display(words)

if __name__ == "__main__": 
    main()


